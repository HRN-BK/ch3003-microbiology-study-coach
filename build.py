#!/usr/bin/env python3
"""Load content/*.py, validate, balance mock sets, and inject into app.html -> index.html.
Usage: python3 build.py [--json]   (--json also writes data/db.json for inspection)"""
import json, os, re, sys, importlib
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'content'))

FAMILIES = [
    ('HIS', 'Lịch sử vi sinh'), ('BAC', 'Vi khuẩn & Archaea'), ('FUN', 'Nấm men & nấm mốc'),
    ('CTL', 'Kiểm soát vi sinh vật'), ('GRO', 'Sinh trưởng & nuôi cấy'), ('PRO', 'Nguyên sinh vật'),
    ('VIR', 'Virus, viroid, prion'), ('IDT', 'Định danh'), ('APP', 'Ứng dụng: SCP, ethanol, penicillin'),
]
SHORT = {'HIS': 'Lịch sử', 'BAC': 'Vi khuẩn', 'FUN': 'Nấm', 'CTL': 'Kiểm soát', 'GRO': 'Sinh trưởng', 'PRO': 'Nguyên sinh', 'VIR': 'Virus', 'IDT': 'Định danh', 'APP': 'Ứng dụng'}
MODULES = ['his', 'bac', 'fun', 'ctl', 'gro', 'pro', 'vir', 'idt', 'app']
BLUEPRINT = {'HIS': 4, 'BAC': 8, 'FUN': 7, 'CTL': 6, 'GRO': 8, 'PRO': 5, 'VIR': 5, 'IDT': 3, 'APP': 4}
MOCK_SETS = 3
MIN_CALC, MIN_NOT = 4, 5

SHEET = """
<h3>Sinh trưởng (GRO)</h3><ul>
<li>N<sub>t</sub> = N<sub>0</sub>·2<sup>n</sup> · <b>n = (log N<sub>t</sub> − log N<sub>0</sub>) / 0,301</b> · <b>g = (t − t<sub>0</sub>) / n</b></li>
<li>Pha: tiềm phát (lag) → log → cân bằng → suy vong; thế hệ E. coli ~20 phút</li>
<li>CFU/mL = số khuẩn lạc / (thể tích cấy mL × độ pha loãng) · đếm đĩa 30–300 khuẩn lạc</li>
<li>Hemocytometer: 1 mm² × 0,1 mm = 10<sup>−4</sup> mL · Petroff-Hausser: 1 mm² × 0,02 mm = 2×10<sup>−5</sup> mL</li>
<li>OD = 2 − log %T · OD &gt; 0,7 → pha loãng lại · MPN: 3 hoặc 5 ống lặp → tra bảng</li>
<li>Nhiệt: ưa lạnh &lt;15 °C · ưa ấm 25–40 °C · ưa nhiệt 50–60 °C · cực ưa nhiệt &gt;80 °C · halophile cực đoan 15–30% NaCl</li>
<li>Oxy: hiếu khí bắt buộc (SOD + catalase) · tùy nghi (SOD + catalase) · chịu oxy (SOD) · kỵ khí bắt buộc (không có)</li>
</ul>
<h3>Kiểm soát (CTL)</h3><ul>
<li>D-value = thời gian giảm 90% (1 log) · <b>t = D × (log N<sub>0</sub> − log N)</b> · 12D đồ hộp (C. botulinum)</li>
<li>Autoclave 121 °C · ~15 psi · 15 phút · Tủ sấy 170 °C · 2 h · UV ~260 nm (dimer thymine)</li>
<li>Thanh trùng sữa: 63 °C/30 phút · HTST 72 °C/15 s · UHT 140 °C/&lt;1 s</li>
<li>Lọc 0,22–0,45 μm · HEPA 0,3 μm · Glycerol 10–30% ở −70 đến −95 °C · đông khô ≥10 năm</li>
</ul>
<h3>Vi khuẩn & nấm (BAC, FUN)</h3><ul>
<li>Gram+: peptidoglycan dày, teichoic acid · Gram−: mỏng, màng ngoài LPS (lipid A = nội độc tố), porin, chu chất</li>
<li>Peptidoglycan: NAG–NAM β-1,4 (lysozyme cắt) · tetrapeptide L-Ala, D-Glu, DAP/L-Lys, D-Ala · penicillin chặn transpeptidase</li>
<li>Archaea: pseudomurein (NAT, β-1,3) · lipid liên kết ether · Nội bào tử: dipicolinic acid + Ca²⁺</li>
<li>Nấm men: thành glucan + mannan (+ chitin ở vết chồi) · S. cerevisiae 16 NST · chu trình Krebs/acetyl-CoA: 2 CO₂, 3 NADH, 1 FADH₂, 1 ATP</li>
</ul>
<h3>Virus & định danh (VIR, IDT)</h3><ul>
<li>Chi -virus · họ -viridae · bộ -virales · HHV-1/2 mụn rộp, 3 thủy đậu, 4 mono, 5 CMV, 6/7 roseola, 8 Kaposi</li>
<li>Tan: phage độc (T4) · Tiềm tan: phage ôn hòa (λ) → prophage · viroid RNA trần 300–400 nt · prion = protein</li>
<li>PFU/mL = số plaque / (thể tích × độ pha loãng)</li>
<li>Bergey cũ (1980–84): 4 tập (Gram−, Gram+, còn lại + archaea, actinomycetes) · mới: 5 tập theo 16S</li>
<li>Enterobacteriaceae oxidase âm · Escherichia/Enterobacter/Citrobacter lên men lactose; Salmonella/Shigella không</li>
<li>Marker: 16S (vi khuẩn), 18S (nhân thực), ITS (nấm), rpoB · Identity = giống/độ dài căn chỉnh · Query cover = phủ/độ dài query</li>
</ul>
<h3>Ứng dụng (APP)</h3><ul>
<li>SCP: protein 60–82% · nucleic acid tảo 3–8%, nấm 7–10% · C:N = 10:1 · cơ chất 45–75% chi phí · Pekilo = Paecilomyces variotii</li>
<li>Y<sub>X/S</sub> = ΔX / ΔS · Ethanol: C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂ · lý thuyết 0,511 g/g · % lý thuyết = Y/0,511</li>
<li>Azolla: K. marxianus 26,8 g/L (Y 0,43), dùng cả glucose + xylose · S. cerevisiae chỉ glucose</li>
<li>Penicillin: 6-APA = thiazolidine + β-lactam · phenylacetic acid → penicillin G · fed-batch hiếu khí 25–27 °C · chiết pH 2–2,5 → dung môi → pH 7–7,5</li>
<li>Thu hồi chung = tích hệ số từng bước · khối lượng = nồng độ × thể tích</li>
</ul>
"""


def fail(msgs):
    print('BUILD FAILED:')
    for m in msgs[:80]:
        print(' -', m)
    sys.exit(1)


def main():
    import _lib
    for m in MODULES:
        importlib.import_module(m)
    units, qs, voc, fcs, wes = _lib.UNITS, _lib.QS, _lib.VOC, _lib.FC, _lib.WE
    errs, warns = [], []
    fam_ids = [f for f, _ in FAMILIES]
    uids = [u['id'] for u in units]
    if len(set(uids)) != len(uids):
        errs.append('duplicate unit ids')
    uset = set(uids)

    # ids
    cnt = Counter()
    for q in qs:
        cnt[q['unit']] += 1
        q['id'] = f"Q-{q['unit']}-{cnt[q['unit']]:03d}"
    cnt = Counter()
    for f in fcs:
        cnt[f['unit']] += 1
        f['id'] = f"F-{f['unit']}-{cnt[f['unit']]:03d}"

    # vocab: dedupe by term (keep first); warn on collisions
    seen, vv = {}, []
    for v in voc:
        k = v['term'].strip().lower()
        if k in seen:
            warns.append(f"vocab term duplicated: {v['term']} ({seen[k]} vs {v['unit']})")
            continue
        seen[k] = v['unit']
        vv.append(v)
    voc = vv
    allterms = set(seen)
    for v in voc:
        v['aliases'] = [a for a in v.get('aliases', []) if a.strip().lower() not in seen or a.strip().lower() == v['term'].lower()]
        for a in v['aliases']:
            allterms.add(a.strip().lower())

    # questions
    for q in qs:
        i = q['id']
        if len(q['options']) != 4: errs.append(f'{i}: options != 4')
        if len(set(q['options'])) != 4: errs.append(f'{i}: duplicate options')
        if q['answer'] not in (0, 1, 2, 3): errs.append(f'{i}: bad answer')
        if q['unit'] not in uset: errs.append(f'{i}: unknown unit')
        if q['type'] not in ('recall', 'concept', 'application', 'calc', 'data', 'not'): errs.append(f'{i}: bad type {q["type"]}')
        if q['pool'] not in ('learn', 'mock'): errs.append(f'{i}: bad pool')
        if len(q['distractorNotes']) != 4: errs.append(f'{i}: distractorNotes != 4')
        if q['type'] == 'not' and not re.search(r'\bNOT\b', q['stem']): warns.append(f'{i}: type not but no NOT in stem')
        bad = [t for t in q['vocab'] if t.strip().lower() not in allterms]
        if bad: warns.append(f'{i}: vocab tags not found {bad}')
        q['vocab'] = [t for t in q['vocab'] if t.strip().lower() in allterms]
    for f in fcs:
        if f['unit'] not in uset: errs.append(f"{f['id']}: unknown unit")
    for v in voc:
        if v['unit'] not in uset: errs.append(f"vocab {v['term']}: unknown unit")
    for u in units:
        pq = u['predictQuestion']
        if len(pq['options']) != 4 or pq['answer'] not in (0, 1, 2, 3): errs.append(f"{u['id']}: bad predictQuestion")
        if not u['lesson']: errs.append(f"{u['id']}: no lesson")
        if not u['keyCards']: errs.append(f"{u['id']}: no keyCards")
        if u['id'][:3] not in fam_ids: errs.append(f"{u['id']}: unknown family")
        if len([q for q in qs if q['unit'] == u['id'] and q['pool'] == 'learn']) < 5: warns.append(f"{u['id']}: fewer than 5 learn questions")
    wids = [w['id'] for w in wes]
    if len(set(wids)) != len(wids): errs.append('duplicate WE ids')
    for w in wes:
        if w['unit'] not in uset: errs.append(f"{w['id']}: unknown unit")
        for k, s in enumerate(w['steps']):
            if 'answer' not in s: errs.append(f"{w['id']} step {k}: no answer")
            if s['input'] == 'number':
                try: float(s['answer'])
                except Exception: errs.append(f"{w['id']} step {k}: non-numeric answer")
            if s['input'] == 'choice' and s['answer'] not in (s.get('choices') or []) and not isinstance(s['answer'], int):
                errs.append(f"{w['id']} step {k}: choice answer not in choices")

    # mock sets: calc items spread globally, then each family's remaining items to its emptiest set
    mock = [q for q in qs if q['pool'] == 'mock']
    set_total, set_calc, set_not = Counter(), Counter(), Counter()
    fam_set = defaultdict(Counter)
    calc = sorted([q for q in mock if q['type'] == 'calc'], key=lambda q: q['id'])
    for k, q in enumerate(calc):
        s = k % MOCK_SETS + 1
        q['mockSet'] = s; set_calc[s] += 1; set_total[s] += 1; fam_set[q['unit'][:3]][s] += 1
    for f in fam_ids:
        rest = [q for q in mock if q['unit'][:3] == f and q['type'] != 'calc']
        rest.sort(key=lambda q: (q['type'] != 'not', q['id']))
        for q in rest:
            key = (lambda s: (fam_set[f][s], set_not[s], set_total[s], s)) if q['type'] == 'not' else (lambda s: (fam_set[f][s], set_total[s], s))
            s = min(range(1, MOCK_SETS + 1), key=key)
            q['mockSet'] = s; fam_set[f][s] += 1; set_total[s] += 1
            if q['type'] == 'not': set_not[s] += 1
    for f in fam_ids:
        for s in range(1, MOCK_SETS + 1):
            if fam_set[f][s] < BLUEPRINT[f]:
                errs.append(f'mock set {s}: family {f} has {fam_set[f][s]} < {BLUEPRINT[f]}')
    for s in range(1, MOCK_SETS + 1):
        if set_calc[s] < MIN_CALC: errs.append(f'mock set {s}: calc {set_calc[s]} < {MIN_CALC}')
        if set_not[s] < MIN_NOT: errs.append(f'mock set {s}: NOT {set_not[s]} < {MIN_NOT}')
    if len(mock) < 50 * MOCK_SETS: errs.append(f'mock pool {len(mock)} < {50 * MOCK_SETS}')

    bal = Counter(q['answer'] for q in qs)
    print('answer index balance:', dict(sorted(bal.items())))
    print('mock sets: total', dict(set_total), 'calc', dict(set_calc), 'NOT', dict(set_not))
    if warns:
        print(f'{len(warns)} warnings:')
        for m in warns[:40]: print('  ~', m)
    if errs: fail(errs)

    meta = {'version': 1, 'course': 'CH3003 Microbiology', 'defaultExamDate': '2026-10-23', 'startDate': '2026-09-25',
            'dailyMinutes': 150, 'mockMinutes': 70, 'order': uids,
            'families': [{'id': f, 'name': n, 'short': SHORT[f]} for f, n in FAMILIES], 'blueprint': BLUEPRINT, 'sheetHtml': SHEET.strip()}
    db = {'meta': meta, 'units': units, 'vocab': voc, 'questions': qs, 'workedExamples': wes, 'flashcards': fcs}
    if '--json' in sys.argv:
        os.makedirs(os.path.join(HERE, 'data'), exist_ok=True)
        json.dump(db, open(os.path.join(HERE, 'data', 'db.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    payload = json.dumps(db, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    tpl = open(os.path.join(HERE, 'app.html'), encoding='utf-8').read()
    assert tpl.count('/*__DB__*/') == 1
    out = tpl.replace('/*__DB__*/', payload)
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print(f'OK: {len(units)} units, {len(qs)} Q ({len(mock)} mock), {len(voc)} vocab, {len(wes)} WE, {len(fcs)} cards -> index.html ({len(out)//1024} KB)')


if __name__ == '__main__':
    main()
