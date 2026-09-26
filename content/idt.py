from _lib import *

SRC = "12.Identification of Microorganisms.pptx"

# ---------------------------------------------------------------- IDT-01
unit("IDT-01", "Phenotypic identification: Bergey's Manual, dichotomous keys, biochemical tests, cell-wall chemistry", "H", 2, 25, SRC + ": slides 1–15",
"""Phòng xét nghiệm nhận một mẫu phân bệnh nhân tiêu chảy, phân lập được một trực khuẩn Gram âm. Là *E. coli* vô hại hay *Salmonella*, *Shigella* gây bệnh? Không cần giải trình tự, chỉ vài ống thử **oxidase, lactose, indole, citrate** là đã thu hẹp đáng kể – đó là **định danh kiểu hình** theo khóa của **Bergey's Manual**.""",
("All Enterobacteriaceae are oxidase-negative. Which test separates Escherichia from Salmonella and Shigella in the lecture?",
 ["Gram stain", "Lactose fermentation with acid and gas", "Oxidase test", "Endospore stain"], 1,
 "Slide 11: *Escherichia, Enterobacter, Citrobacter* **lên men lactose tạo acid và khí**; *Salmonella, Shigella* thì không."),
[
("1. Mục tiêu bài (slide 2–3)", """
- **L.O.1**: giải thích các bước định danh một vi sinh vật dựa trên **đặc điểm hình thái, sinh lý, lý học và hóa học**.
- **L.O.2**: giải thích các bước định danh dựa trên **trình tự nucleotide/protein đặc hiệu** (bài IDT-02).
- Phân biệt: **phân loại (classification)** – sắp xếp vào nhóm; **danh pháp (nomenclature)** – đặt tên; **định danh (identification)** – gắn mẫu chưa biết vào nhóm đã mô tả.
"""),
("2. Bergey's Manual (slide 4–7)", """
**Bergey's Manual of Determinative Bacteriology (1980–1984)** – **4 divisions/phyla**, 4 tập:

| Tập | Nội dung |
|---|---|
| **Volume 1** | **Tất cả vi khuẩn Gram âm** (quan trọng y học và công nghiệp) |
| **Volume 2** | **Tất cả vi khuẩn Gram dương** |
| **Volume 3** | **Các vi khuẩn còn lại**, một số Gram âm và **archaea** |
| **Volume 4** | **Actinomycetes** và các vi khuẩn khác |

- Nhược điểm: **không cung cấp lịch sử tiến hóa rõ ràng** của vi khuẩn (slide 5).
- Trong mỗi division, vi khuẩn chia nhóm theo **kiểu hình (phenotype)** (slide 6): **phản ứng Gram, hình dạng tế bào, cách sắp xếp, nhu cầu oxy, khả năng di động, đặc điểm dinh dưỡng và chuyển hóa**.
- Nhắc lại BAC-07: 4 division theo thành tế bào – **Gracilicutes** (Gram âm, thành mỏng), **Firmicutes** (Gram dương, thành dày), **Tenericutes** (không thành – Mycoplasma), **Mendosicutes** (thành khác thường – archaea).

**Ấn bản mới (current editions): 5 tập**, sắp xếp các ngành theo **quan hệ tiến hóa của trình tự 16S rDNA** (slide 7; đúng tên là *Bergey's Manual of Systematic Bacteriology*, 2nd ed.):

| Tập | Năm | Nội dung |
|---|---|---|
| 1 | **2001** | **Archaea, Actinomycetes & photoautotrophs** (đúng chữ slide) [hiệu chỉnh] – tên thật của tập: *The Archaea and the Deeply Branching and Phototrophic Bacteria* |
| 2 | **2005** | **Proteobacteria** (2A: phương pháp cơ bản; 2B: lớp **Gammaproteobacteria**; 2C: các lớp Proteobacteria khác) |
| 3 | **2009** | **Firmicutes** |
| 4 | **2011** | **Bacteroidetes, Spirochaetes, Tenericutes (Mollicutes)**, Acidobacteria, Fibrobacteres, Fusobacteria, … **Chlamydiae, Planctomycetes** |
| 5 | **2012** | **Actinobacteria** |

- Các lớp Proteobacteria đặt theo chữ Hy Lạp: **Alpha, Beta, Gamma, Delta, Epsilon** (ghi chú slide 9).
"""),
("3. Quan sát hình thái (slide 8–9, 13)", """
- **Hình thái khuẩn lạc (colony morphology)**: **hình dạng khuẩn lạc, màu hệ sợi (mycelium), khả năng tạo bào tử, màu bào tử, khả năng khuếch tán sắc tố vào môi trường**...
- **Hình thái tế bào**: hình dạng tế bào sinh dưỡng, hình dạng bào tử...
- Ví dụ: **Actinomycetes** (slide 8) – vi khuẩn Gram dương tạo **hệ sợi phân nhánh** và bào tử (*Streptomyces*) – vẫn là vi khuẩn dù trông giống nấm; **Firmicutes: *Bacillus*** (slide 9) – trực khuẩn Gram dương tạo nội bào tử.
- **Đặc điểm nuôi cấy** (culture characteristics): nhiệt độ, pH, môi trường sinh trưởng.
"""),
("4. Phép thử sinh hóa & khóa phân đôi (slide 10–12)", """
- **Khóa phân đôi (dichotomous key)**: chuỗi câu hỏi có/không; mỗi kết quả chọn một nhánh cho đến tên loài.
- Ví dụ slide 10: **Gram âm → oxidase dương → không thủy phân urea → indole âm → không tạo acetoin (VP âm)** → *Pasteurella multocida*.

| Phép thử | Phát hiện |
|---|---|
| **Oxidase** | enzyme **cytochrome c oxidase** |
| **Catalase** | phân hủy H₂O₂ → O₂ (sủi bọt) |
| **Lên men lactose** | tạo **acid** (đổi màu chỉ thị) và/hoặc **khí** (ống Durham) |
| **Indole** | chuyển hóa **tryptophan → indole** (thuốc thử Kovac đỏ) |
| **Methyl red (MR)** | lên men acid hỗn hợp, pH < 4,4 |
| **Voges-Proskauer (VP)** | tạo **acetoin** (lên men butanediol) |
| **Citrate** | dùng **citrate làm nguồn C duy nhất** |
| **Urease** | thủy phân **urea → NH₃** |

- **Bộ IMViC** (Indole, Methyl red, Voges-Proskauer, Citrate): *E. coli* **+ + − −**; *Enterobacter aerogenes* **− − + +**. [mở rộng]

**Enterobacteriaceae (slide 11)**:
- **Tất cả không có oxidase (oxidase âm)**: *Escherichia, Enterobacter, Shigella, Citrobacter, Salmonella*.
- ***Escherichia, Enterobacter, Citrobacter*** **lên men lactose tạo acid và khí** → phân biệt với ***Salmonella, Shigella*** (không lên men lactose).
- Các phép thử sinh hóa khác phân biệt các loài giữa các chi.

**Bộ kit nhiều phép thử (slide 12, kiểu API 20E / Enterotube)**: 15 phản ứng chia **nhóm 3**, trọng số **4 – 2 – 1** theo thứ tự in; cộng trọng số của phản ứng dương trong mỗi nhóm → **mã 5 chữ số** → tra bảng. Ví dụ mã **62343** (và 62342) → *Citrobacter freundii* – một loài có thể có hơn một mã.
"""),
("5. Hóa phân loại thành tế bào (slide 13–15)", """
**Thành phần hóa học thành tế bào**: peptidoglycan, glucosamine, **alanine, glutamic acid, glycine, arabinose, galactose**, **LL-α,ε-diaminopimelic acid (LL-DAP)** và **meso-α,ε-DAP (meso-DAP)**...
- DAP và lysine đều có nhóm amin thứ hai, nhưng **DAP có 2 nhóm carboxyl**, lysine có 1 (slide 14).
- **LL-DAP** và **meso-DAP** là **đồng phân lập thể**: ví dụ *Streptomyces* có **LL-DAP** (+ glycine), nhiều actinomycetes khác có **meso-DAP** – dùng để phân biệt các chi actinomycetes (thành tế bào typ I–IV). [mở rộng]
- Đường đặc trưng (arabinose, galactose) trong dịch thủy phân tế bào cũng là dấu ấn phân loại.
"""),
],
[
("Định danh trong phòng xét nghiệm thực tế", """
- **MALDI-TOF MS**: đo phổ khối protein ribosome của khuẩn lạc, so với thư viện → định danh trong vài phút; đang thay thế nhiều phép thử sinh hóa ở bệnh viện lớn.
- Kiểm nghiệm thực phẩm theo ISO: *Salmonella* (tiền tăng sinh → tăng sinh chọn lọc → thạch XLD → khẳng định sinh hóa + huyết thanh), *E. coli* (MPN + indole ở 44 °C) – liên hệ GRO-06.
"""),
],
[
("Bergey's Manual", "**Determinative Bacteriology (1980–1984)**: 4 divisions — Vol 1 Gram-negative; Vol 2 Gram-positive; Vol 3 remaining bacteria, some Gram-negatives and archaea; Vol 4 actinomycetes. Does **not** give a clear evolutionary history. Groups by **Gram reaction, shape, arrangement, O₂ requirement, motility, nutrition/metabolism**. **Current editions: 5 volumes** by **16S rDNA** (2001 Archaea…; 2005 Proteobacteria; 2009 Firmicutes; 2011 Bacteroidetes…; 2012 Actinobacteria).", "4 tập cũ (kiểu hình) vs 5 tập mới (16S)."),
("Enterobacteriaceae", "All members are **oxidase-negative** (*Escherichia, Enterobacter, Shigella, Citrobacter, Salmonella*). *Escherichia, Enterobacter, Citrobacter* **ferment lactose to acid and gas**, distinguishing them from *Salmonella* and *Shigella*.", "Oxidase âm; lactose tách nhóm."),
("Morphology and chemotaxonomy", "Colony morphology (shape, mycelium color, spore formation, spore color, pigment diffusion), cell morphology (vegetative cell and spore shape), **cell-wall chemistry** (peptidoglycan, glucosamine, alanine, glutamic acid, glycine, arabinose, galactose, **LL-DAP vs meso-DAP**), culture characteristics.", "Hình thái + hóa thành tế bào."),
],
["Salmonella ferments lactose", "Enterobacteriaceae are oxidase-positive", "The 1980–84 Bergey's gives a clear evolutionary history"])

q("IDT-01", "recall", 1, "In Bergey's Manual of Determinative Bacteriology (1980–1984), Volume 1 covers:",
  ["all Gram-positive bacteria", "all Gram-negative bacteria of medical and industrial importance", "actinomycetes", "archaea only"], 1,
  "Slide 4: **Vol 1 – Gram âm**; Vol 2 – Gram dương; Vol 3 – còn lại + archaea; Vol 4 – actinomycetes.",
  ["Vol 2.", "", "Vol 4.", "Sai."], ["Bergey's Manual"], src=SRC + " slide 4")
q("IDT-01", "recall", 1, "Actinomycetes are covered in which volume of the 1980–1984 Bergey's Manual?",
  ["Volume 1", "Volume 2", "Volume 3", "Volume 4"], 3,
  "Slide 4: **Volume 4 – Actinomycetes và các vi khuẩn khác**.",
  ["Gram âm.", "Gram dương.", "Còn lại, archaea.", ""], ["Bergey's Manual", "actinomycetes"], src=SRC + " slide 4")
q("IDT-01", "concept", 2, "What is the main limitation of the older (1980–84) Bergey's Manual noted in the lecture?",
  ["It lacked Gram-negative bacteria", "It does not provide a clear evolutionary history of bacteria", "It only described viruses", "It was based on 16S rDNA"], 1,
  "Slide 5: xếp theo kiểu hình → **không cho thấy lịch sử tiến hóa rõ ràng**.",
  ["Sai.", "", "Sai.", "Đó là ấn bản mới."], ["Bergey's Manual"], "The 1980–84 Bergey's gives a clear evolutionary history", src=SRC + " slide 5")
q("IDT-01", "recall", 1, "The current 5-volume Bergey's Manual organizes bacterial phyla according to:",
  ["Gram stain only", "evolutionary relationships based on 16S rDNA sequences", "colony color", "oxygen requirement"], 1,
  "Slide 7: theo **quan hệ tiến hóa của trình tự 16S rDNA**.",
  ["Kiểu hình (cũ).", "", "Sai.", "Sai."], ["16S rDNA", "Bergey's Manual"], src=SRC + " slide 7")
q("IDT-01", "recall", 1, "In the current Bergey's volumes, Volume 3 (2009) covers:",
  ["Proteobacteria", "Firmicutes", "Actinobacteria", "Archaea"], 1,
  "Slide 7: Vol 3 (2009) – **Firmicutes**. Vol 2 (2005) Proteobacteria; Vol 5 (2012) Actinobacteria; Vol 1 (2001) Archaea.",
  ["Vol 2.", "", "Vol 5.", "Vol 1."], ["Firmicutes"], src=SRC + " slide 7")
q("IDT-01", "recall", 1, "Which is true of ALL members of the family Enterobacteriaceae?",
  ["They are oxidase-positive", "They lack oxidase (oxidase-negative)", "They ferment lactose", "They form endospores"], 1,
  "Slide 11: **tất cả không có oxidase**.",
  ["Ngược.", "", "Salmonella, Shigella không.", "Không."], ["Enterobacteriaceae", "oxidase"], "Enterobacteriaceae are oxidase-positive", src=SRC + " slide 11")
q("IDT-01", "application", 2, "A Gram-negative, oxidase-negative rod from a stool sample does NOT ferment lactose. Based on the lecture, it most likely belongs to:",
  ["Escherichia", "Enterobacter", "Citrobacter", "Salmonella or Shigella"], 3,
  "Slide 11: *Escherichia, Enterobacter, Citrobacter* lên men lactose; **Salmonella, Shigella không**.",
  ["Lên men lactose.", "Lên men lactose.", "Lên men lactose.", ""], ["Enterobacteriaceae", "lactose fermentation"], "Salmonella ferments lactose", src=SRC + " slide 11")
q("IDT-01", "not", 2, "Which is NOT a phenotypic grouping criterion listed in the lecture for Bergey's divisions?",
  ["Gram stain reaction", "Cell shape and arrangement", "Oxygen requirement and motility", "16S rDNA sequence similarity"], 3,
  "Slide 6: Gram, hình dạng, sắp xếp, oxy, di động, dinh dưỡng/chuyển hóa – đều là **kiểu hình**. 16S là **kiểu gene** (ấn bản mới).",
  ["Có.", "Có.", "Có.", ""], ["phenotype"], src=SRC + " slide 6")
q("IDT-01", "recall", 1, "The Voges-Proskauer (VP) test detects:",
  ["indole from tryptophan", "acetoin from butanediol fermentation", "cytochrome c oxidase", "use of citrate as sole carbon source"], 1,
  "**VP** phát hiện **acetoin**.",
  ["Indole test.", "", "Oxidase.", "Citrate test."], ["Voges-Proskauer test"])
q("IDT-01", "concept", 2, "In a dichotomous key, an isolate is Gram-negative, oxidase-positive, urease-negative, indole-negative and VP-negative (no acetoin). The lecture key leads to:",
  ["Escherichia coli", "Pasteurella multocida", "Salmonella", "Bacillus subtilis"], 1,
  "Slide 10: nhánh này dẫn đến ***Pasteurella multocida*** (khóa minh họa).",
  ["Oxidase âm.", "", "Oxidase âm.", "Gram dương."], ["dichotomous key"], src=SRC + " slide 10")
q("IDT-01", "calc", 2, "In a 15-test kit, tests are grouped in threes with weights 4, 2, 1. In one group the first and third tests are positive and the second is negative. What digit is recorded for that group?",
  ["3", "5", "6", "7"], 1,
  "Cộng trọng số dương: 4 + 1 = **5**.",
  ["2 + 1.", "", "4 + 2.", "Cả ba dương."], ["API code"])
q("IDT-01", "recall", 1, "Which cell-wall component is used as a chemotaxonomic marker to distinguish actinomycete genera?",
  ["Lipid A", "Isomers of diaminopimelic acid (LL-DAP vs meso-DAP)", "Chitin", "Ergosterol"], 1,
  "Slide 13–15: **LL-DAP** và **meso-DAP** (cùng glycine, arabinose, galactose...).",
  ["Gram âm LPS.", "", "Nấm.", "Nấm."], ["diaminopimelic acid", "chemotaxonomy"], src=SRC + " slides 13–15")
q("IDT-01", "recall", 1, "Which genera ferment lactose to produce acid and gas, according to the lecture?",
  ["Salmonella and Shigella", "Escherichia, Enterobacter and Citrobacter", "Bacillus and Clostridium", "Pseudomonas and Vibrio"], 1,
  "Slide 11.",
  ["Không lên men lactose.", "", "Không thuộc slide.", "Không thuộc slide."], ["lactose fermentation"], pool="mock")
q("IDT-01", "recall", 1, "Volume 2 (2005) of the current Bergey's Manual covers:",
  ["Firmicutes", "Proteobacteria", "Actinobacteria", "Spirochaetes"], 1,
  "Slide 7: Vol 2 – **Proteobacteria** (2A, 2B Gammaproteobacteria, 2C).",
  ["Vol 3.", "", "Vol 5.", "Vol 4."], ["Proteobacteria"], pool="mock")
q("IDT-01", "not", 2, "Which is NOT listed in the lecture as a colony morphology feature used for identification?",
  ["Colony shape", "Mycelium color", "Ability to diffuse color into the medium", "16S rRNA gene length"], 3,
  "Slide 13: hình dạng khuẩn lạc, màu hệ sợi, tạo bào tử, màu bào tử, khuếch tán sắc tố.",
  ["Có.", "Có.", "Có.", ""], ["colony morphology"], pool="mock")
q("IDT-01", "application", 2, "IMViC results + + − − (indole +, MR +, VP −, citrate −) for a lactose-fermenting enteric rod best fit:",
  ["Enterobacter aerogenes", "Escherichia coli", "Salmonella", "Shigella"], 1,
  "*E. coli*: **+ + − −**; *Enterobacter aerogenes*: − − + +.",
  ["Ngược.", "", "Không lên men lactose.", "Không lên men lactose."], ["IMViC"], pool="mock")
q("IDT-01", "calc", 2, "Weights are 4-2-1 per group of three. A group with all three tests negative is recorded as:",
  ["0", "1", "4", "7"], 0,
  "Không có phản ứng dương → **0**.",
  ["", "Chỉ test 3 dương.", "Chỉ test 1 dương.", "Cả ba dương."], ["API code"], pool="mock")

v("IDT-01", "identification", "định danh", "Assigning an unknown isolate to a described taxon using evidence.", "Identification uses biochemical tests.")
v("IDT-01", "Bergey's Manual", "Cẩm nang Bergey", "Reference manual for bacterial identification and classification.", "Bergey's Manual has 4 or 5 volumes.", ["Bergey's Manual of Determinative Bacteriology", "Bergey"])
v("IDT-01", "phenotype", "kiểu hình", "Observable traits such as shape, Gram reaction and metabolism.", "Older keys use phenotype.", ["phenotypic"])
v("IDT-01", "dichotomous key", "khóa phân đôi", "A series of either-or choices leading to identification.", "Follow the dichotomous key branch by branch.")
v("IDT-01", "Enterobacteriaceae", "họ vi khuẩn đường ruột", "Oxidase-negative Gram-negative rods including E. coli and Salmonella.", "All Enterobacteriaceae are oxidase-negative.")
v("IDT-01", "oxidase", "oxidase", "Cytochrome c oxidase detected by the oxidase test.", "Pseudomonas is oxidase-positive.", ["oxidase test", "oxidase-negative"])
v("IDT-01", "lactose fermentation", "lên men lactose", "Production of acid (and gas) from lactose.", "E. coli shows lactose fermentation.")
v("IDT-01", "Voges-Proskauer test", "phép thử VP", "Test detecting acetoin.", "Enterobacter is VP-positive.", ["VP", "VP test", "acetoin"])
v("IDT-01", "IMViC", "bộ IMViC", "Indole, methyl red, Voges-Proskauer and citrate tests.", "E. coli IMViC is ++--.")
v("IDT-01", "API code", "mã số bộ kit sinh hóa", "Numeric profile from summing 4-2-1 weights of positive tests per group.", "Code 62343 matches Citrobacter freundii.", ["API 20E"])
v("IDT-01", "chemotaxonomy", "hóa phân loại", "Classification using chemical composition such as cell-wall components.", "DAP isomers are used in chemotaxonomy.")
v("IDT-01", "diaminopimelic acid", "acid diaminopimelic (DAP)", "A peptidoglycan amino acid with LL and meso isomers.", "Streptomyces has LL-DAP.", ["DAP", "meso-DAP", "LL-DAP"])
v("IDT-01", "actinomycetes", "xạ khuẩn", "Gram-positive filamentous, spore-forming bacteria such as Streptomyces.", "Actinomycetes form mycelium.", ["Actinobacteria", "Streptomyces"])

fc("IDT-01", "fact", "Bergey's Determinative (1980–84) volumes?", "1 Gram-negative; 2 Gram-positive; 3 remaining + some Gram-neg + archaea; 4 actinomycetes.")
fc("IDT-01", "fact", "Current Bergey's (5 volumes, 16S)?", "2001 Archaea, Actinomycetes & photoautotrophs (slide wording); 2005 Proteobacteria; 2009 Firmicutes; 2011 Bacteroidetes, Spirochaetes, Tenericutes…; 2012 Actinobacteria.")
fc("IDT-01", "fact", "Enterobacteriaceae key rule?", "All oxidase-negative; Escherichia/Enterobacter/Citrobacter ferment lactose (acid + gas), Salmonella/Shigella do not.")
fc("IDT-01", "fact", "Phenotypic criteria in Bergey's?", "Gram reaction, shape, arrangement, O2 requirement, motility, nutrition/metabolism.")
fc("IDT-01", "number", "Kit code weights?", "4-2-1 per group of three tests; sum positives.")

we("WE-12", "IDT-01", "Computing a biochemical kit profile code",
   "A 15-test kit is read in 5 groups of 3 tests with weights 4, 2, 1. Results (+/−) by group: G1: + + −; G2: + + +; G3: − + +; G4: + − −; G5: − + +. Find the 5-digit code.",
   [S("Group 1 digit (4+2)?", 6), S("Group 2 digit?", 7), S("Group 3 digit?", 3), S("Group 4 digit?", 4), S("Group 5 digit?", 3),
    S("Full code (5 digits as a number)?", 67343)],
   "67343",
   "Mỗi nhóm cộng trọng số của phản ứng dương: 4+2=6; 4+2+1=7; 2+1=3; 4; 2+1=3 → mã 67343 rồi tra bảng của bộ kit. Không cộng gộp cả 15 phản ứng thành một số.")

# ---------------------------------------------------------------- IDT-02
unit("IDT-02", "Molecular identification: 16S/18S/ITS markers, PCR, sequencing, BLAST and phylogenetic trees", "H", 2, 25, SRC + ": slides 16–22",
"""Bạn phân lập được một xạ khuẩn tạo kháng sinh từ đất rừng Cát Tiên. Muốn công bố, bạn phải biết nó là loài gì. Hình thái và sinh hóa chỉ cho biết "có thể là *Streptomyces*". Giải trình tự **16S rDNA** rồi **BLAST** cho kết quả 471/471 nucleotide trùng khớp 100% với *Streptomyces flaveus* – đã đủ gọi tên loài chưa?""",
("Which gene is most commonly sequenced to identify bacteria?",
 ["18S rDNA", "16S rDNA", "ITS", "Actin"], 1,
 "Slide 17: **16S rDNA** (tiểu đơn vị nhỏ ribosome prokaryote). 18S cho nhân thực; ITS cho nấm."),
[
("1. Quy trình định danh phân tử (slide 17)", """
1. **Chọn gene đặc hiệu**: **16S rDNA, 23S rDNA, 18S rDNA, ITS (Internal Transcribed Spacer), 25S rDNA, rpoB**, …
2. **Thiết kế mồi (primer design) & PCR** – khuếch đại vùng gene đích.
3. **Giải trình tự đoạn PCR** (PCR fragment sequencing).
4. **Tìm kiếm độ tương đồng trình tự trên cơ sở dữ liệu** (homology; **BLASTN** – nucleotide; **BLASTP** – protein).
5. **Xây dựng cây phát sinh chủng loại (phylogenetic tree)**:
   - **Sắp gióng đa trình tự (multiple sequence alignment)**;
   - **Chọn mô hình tiến hóa và phương pháp dựng cây** (neighbor-joining, maximum likelihood… [mở rộng]);
   - **Đánh giá độ tin cậy của cây** (bootstrap).
"""),
("2. Chọn marker gene", """
| Marker | Dùng cho | Ghi chú |
|---|---|---|
| **16S rDNA** | **vi khuẩn, archaea** | ~1500 bp; có vùng bảo tồn (gắn mồi chung) + vùng biến đổi V1–V9 (phân biệt) |
| **23S rDNA** | vi khuẩn | tiểu đơn vị lớn |
| **18S rDNA** | **nhân thực** (nấm, protist) | tiểu đơn vị nhỏ nhân thực |
| **ITS** | **nấm** (mã vạch chuẩn) | vùng đệm giữa 18S–5.8S–28S, biến đổi mạnh |
| **25S/26S rDNA** (D1/D2) | **nấm men** | tiểu đơn vị lớn |
| **rpoB** | vi khuẩn | gene mã hóa protein (tiểu đơn vị β RNA polymerase), phân giải tốt hơn 16S giữa loài gần |

- Marker tốt: **có vùng bảo tồn** (để so sánh, gắn mồi) **và vùng biến đổi** (để phân biệt).
- \"S\" = **Svedberg** (hệ số lắng), không phải số nucleotide.
- Hai loài gần có thể có 16S **giống hệt** → 16S đôi khi chỉ đủ đến **chi**. [mở rộng]
"""),
("3. BLAST – Basic Local Alignment Search Tool (slide 18–22)", """
- **BLAST** tìm các đoạn **căn chỉnh cục bộ** giữa **query** (trình tự của mình) và **subject** (trình tự trong cơ sở dữ liệu, vd NCBI GenBank).
- Các cột kết quả:

| Trường | Ý nghĩa |
|---|---|
| **Query length** | độ dài trình tự đưa vào |
| **Query cover** | % độ dài query được căn chỉnh phủ |
| **Percent identity** | % vị trí **giống hệt** trong đoạn căn chỉnh |
| **Score / bit score** | điểm chất lượng căn chỉnh |
| **E-value** | số kết quả có điểm tương đương kỳ vọng xuất hiện **ngẫu nhiên** – càng nhỏ càng có ý nghĩa (0.0 = rất nhỏ) |
| **Accession** | mã bản ghi, vd JX293177.1 |

> **Identity = số vị trí giống / độ dài căn chỉnh × 100%**; **Query cover = độ dài query được phủ / độ dài query × 100%**.

**Ví dụ slide 20–22**: query **471 nt**, BLASTN; nhiều hit **100% query cover, 100% identity, E-value 0.0, score 870**. Hit đầu: ***Streptomyces flaveus* strain X418** (JX293177.1, subject dài **1503 nt**); đoạn subject **29–499** khớp query **1–471** (499 − 29 + 1 = 471); **Identities 471/471 (100%)**, **Gaps 0/471**, **Strand Plus/Plus**. Hit kế: *Streptomyces* sp. NEAU-P17 cũng 100%.

**Kết luận đúng mức**: đoạn 16S 471 nt phù hợp với chi ***Streptomyces***; **chưa phân biệt được loài** vì nhiều loài/chủng cùng 100%. Cần trình tự dài hơn, gene khác (rpoB…) hoặc bằng chứng kiểu hình.

- Ngưỡng tham khảo [mở rộng]: 16S **≥ 98,7%** thường xem là cùng loài; **≥ 94,5%** cùng chi.
"""),
("4. Cây phát sinh chủng loại", """
- **Multiple sequence alignment**: xếp các vị trí tương đồng của nhiều trình tự vào cùng cột (Clustal, MUSCLE). [mở rộng]
- **Mô hình tiến hóa** mô tả cách thay thế nucleotide (Jukes–Cantor, Kimura 2-parameter); **phương pháp** dựng cây: **neighbor-joining, maximum likelihood, maximum parsimony**. Phần mềm: **MEGA**.
- **Độ tin cậy**: **bootstrap** – lấy mẫu lại các cột căn chỉnh (vd 1000 lần), dựng lại cây; giá trị 90 ở một nút = nhánh xuất hiện ở 90% lần lặp (**không** phải giống nhau 90%).
- Đọc cây: độ gần = **độ dài nhánh** theo thước đo (substitutions/site), không phải vị trí trên/dưới trang. Nên đưa **chủng chuẩn (type strain)** vào cây.
"""),
],
[
("Metagenomics và giám sát", """
- Giải trình tự **16S amplicon** trực tiếp từ mẫu (đất, ruột, nước thải) cho biết thành phần cộng đồng vi sinh **không cần nuôi cấy** – phần lớn vi khuẩn chưa nuôi cấy được.
- Giải trình tự toàn bộ bộ gene (WGS) để truy vết dịch bệnh do thực phẩm (Listeria, Salmonella) và phát hiện gene kháng thuốc.
- Trong công nghiệp: định danh chủng sản xuất (nấm men bia, xạ khuẩn kháng sinh, *Aspergillus*) bằng ITS/16S trước khi đăng ký chủng.
"""),
],
[
("Molecular workflow", "Choose specific genes (**16S, 23S, 18S rDNA, ITS, 25S rDNA, rpoB**); **primer design & PCR**; **sequence** the PCR fragment; search databases for similarity (**BLASTN, BLASTP**); build a **phylogenetic tree** (multiple sequence alignment, choose evolutionary model/method, determine reliability).", "Gene → PCR → giải trình tự → BLAST → cây."),
("Markers", "**16S rDNA**: bacteria/archaea (conserved + variable regions). **18S rDNA**: eukaryotes. **ITS**: fungi. **25S rDNA**: yeasts (large subunit). **rpoB**: protein-coding marker with higher resolution.", "Chọn marker theo nhóm."),
("Reading BLAST", "**Percent identity** = identical positions / alignment length; **query cover** = % of query aligned; **E-value** = expected random hits (smaller = more significant). Slide example: 471/471 (100%) to *Streptomyces flaveus* X418 and *Streptomyces* sp. — supports the **genus**, not necessarily the species. **Bootstrap** measures branch support.", "Identity ≠ định danh loài chắc chắn."),
],
["100% identity over 471 nt proves the species", "ITS is the main bacterial marker", "Bootstrap 90 means 90% similarity", "BLASTP compares nucleotide sequences"])

q("IDT-02", "recall", 1, "Which marker is most commonly used for identifying fungi?",
  ["16S rDNA", "ITS (internal transcribed spacer)", "rpoB", "23S rDNA"], 1,
  "**ITS** là mã vạch chuẩn cho nấm; 16S, 23S, rpoB cho vi khuẩn.",
  ["Vi khuẩn.", "", "Vi khuẩn.", "Vi khuẩn."], ["ITS"], "ITS is the main bacterial marker", src=SRC + " slide 17")
q("IDT-02", "recall", 1, "18S rDNA is used mainly to identify:",
  ["bacteria", "eukaryotes (e.g., fungi, protists)", "viruses", "archaea only"], 1,
  "**18S** = tiểu đơn vị nhỏ ribosome **nhân thực**; 16S cho prokaryote.",
  ["16S.", "", "Virus không có ribosome.", "16S."], ["18S rDNA"])
q("IDT-02", "recall", 1, "Put the molecular identification steps in the correct order:",
  ["BLAST → PCR → sequencing → primer design", "Primer design & PCR → sequencing → database search (BLAST) → phylogenetic tree", "Phylogenetic tree → PCR → BLAST", "Sequencing → primer design → PCR → tree"], 1,
  "Slide 17: chọn gene → **primer & PCR → giải trình tự → BLAST → cây phát sinh**.",
  ["Sai thứ tự.", "", "Sai.", "Sai."], ["PCR", "BLAST"], src=SRC + " slide 17")
q("IDT-02", "concept", 2, "Why is 16S rDNA a good marker for bacterial identification?",
  ["It is absent in most bacteria", "It contains conserved regions for universal primers and variable regions that distinguish taxa", "It codes for toxins", "It changes every generation"], 1,
  "Có **vùng bảo tồn** (mồi chung, căn chỉnh) và **vùng biến đổi** (phân biệt).",
  ["Mọi vi khuẩn đều có.", "", "Sai.", "Tiến hóa chậm."], ["16S rDNA"])
q("IDT-02", "calc", 2, "A BLAST alignment has 396 identical positions over an alignment length of 400 nt, and the query is 471 nt long (the alignment covers 400 nt of it). What are the percent identity and query cover?",
  ["99% identity; 84.9% query cover", "84.9% identity; 99% query cover", "100% identity; 100% query cover", "99% identity; 100% query cover"], 0,
  "Identity = 396/400 = **99%**; query cover = 400/471 = **84,9%**. Hai cột có mẫu số khác nhau.",
  ["", "Đảo hai cột.", "Sai.", "Quên query dài 471."], ["percent identity", "query cover"])
q("IDT-02", "concept", 2, "In the lecture example, a 471-nt 16S query shows 100% identity and 100% query cover to several Streptomyces records (S. flaveus and Streptomyces sp.). The best conclusion is:",
  ["The isolate is certainly S. flaveus strain X418", "The isolate belongs to the genus Streptomyces; this fragment alone cannot resolve the species", "The isolate is a fungus", "The whole genome is identical to S. flaveus"], 1,
  "Nhiều hit đồng hạng 100% → chỉ chắc cấp **chi**; chỉ so 471 nt, không phải toàn gene/bộ gene.",
  ["Quá mức.", "", "Streptomyces là vi khuẩn.", "Chỉ 471 nt."], ["BLAST"], "100% identity over 471 nt proves the species", src=SRC + " slides 20–22")
q("IDT-02", "concept", 2, "What does a smaller E-value in a BLAST result indicate?",
  ["A longer sequence", "The match is less likely to occur by chance (more significant)", "Lower identity", "The species is more common"], 1,
  "E-value = số hit tương đương kỳ vọng xuất hiện **ngẫu nhiên**; càng nhỏ càng có ý nghĩa.",
  ["Sai.", "", "Sai.", "Sai."], ["E-value"])
q("IDT-02", "recall", 1, "Which BLAST program compares a protein query with a protein database?",
  ["BLASTN", "BLASTP", "PCR", "Clustal"], 1,
  "**BLASTP** – protein; **BLASTN** – nucleotide.",
  ["Nucleotide.", "", "Không phải BLAST.", "Căn chỉnh đa trình tự."], ["BLAST"], "BLASTP compares nucleotide sequences")
q("IDT-02", "concept", 2, "A node on a phylogenetic tree has a bootstrap value of 90. This means:",
  ["the sequences are 90% identical", "the clade appeared in 90% of the resampled trees", "90% of the species are correct", "the branch length is 0.90"], 1,
  "Bootstrap = % lần lặp lấy mẫu lại có xuất hiện nhánh đó – đo **độ tin cậy** của nhánh.",
  ["Không phải độ giống.", "", "Sai.", "Độ dài nhánh khác."], ["bootstrap", "phylogenetic tree"], "Bootstrap 90 means 90% similarity")
q("IDT-02", "recall", 1, "Which of the following is a protein-coding gene used as an identification marker in the lecture list?",
  ["16S rDNA", "ITS", "rpoB", "25S rDNA"], 2,
  "**rpoB** mã hóa tiểu đơn vị β của RNA polymerase; các marker còn lại là rRNA/vùng đệm.",
  ["rRNA.", "Vùng đệm.", "", "rRNA."], ["rpoB"], pool="mock")
q("IDT-02", "not", 2, "Which is NOT a step in constructing a phylogenetic tree according to the lecture?",
  ["Multiple sequence alignment", "Choosing evolutionary models and methods", "Determining the reliability of the tree", "Gram staining the isolate"], 3,
  "Slide 17: căn chỉnh đa trình tự, chọn mô hình/phương pháp, đánh giá độ tin cậy.",
  ["Có.", "Có.", "Có.", ""], ["phylogenetic tree"], pool="mock")
q("IDT-02", "calc", 2, "In the lecture BLAST hit, the subject region 29–499 aligns to the query 1–471. How many positions does the subject region span?",
  ["470", "471", "499", "528"], 1,
  "499 − 29 + **1** = **471** (tính cả hai đầu).",
  ["Quên +1.", "", "Sai.", "Sai."], ["BLAST"], pool="mock")
q("IDT-02", "concept", 2, "What is the role of primers in molecular identification?",
  ["They stain the cells", "They define and allow PCR amplification of the target gene region", "They digest DNA", "They sequence proteins"], 1,
  "Primer gắn hai đầu vùng đích → **PCR** khuếch đại vùng đó.",
  ["Sai.", "", "Enzyme giới hạn.", "Sai."], ["primer", "PCR"], pool="mock")
q("IDT-02", "not", 2, "Which gene is NOT listed in the lecture as a specific gene sequence for identification?",
  ["16S rDNA", "ITS", "rpoB", "Insulin gene"], 3,
  "Slide 17: 16S, 23S, 18S, ITS, 25S, rpoB.",
  ["Có.", "Có.", "Có.", ""], ["16S rDNA"], pool="mock")

v("IDT-02", "16S rDNA", "gene 16S rDNA", "Gene for the small-subunit rRNA of bacteria and archaea, used for identification.", "16S rDNA sequencing identified the isolate.", ["16S rRNA", "16S"])
v("IDT-02", "18S rDNA", "gene 18S rDNA", "Small-subunit rRNA gene of eukaryotes.", "18S rDNA identifies protists.", ["18S"])
v("IDT-02", "ITS", "vùng ITS", "Internal transcribed spacer between rRNA genes; fungal barcode.", "ITS sequencing identified the mold.", ["internal transcribed spacer"])
v("IDT-02", "rpoB", "gene rpoB", "Gene for the RNA polymerase beta subunit, a protein-coding marker.", "rpoB resolves close species.")
v("IDT-02", "primer", "đoạn mồi", "A short oligonucleotide that starts DNA synthesis in PCR.", "Universal primers bind conserved 16S regions.", ["primers", "primer design"])
v("IDT-02", "PCR", "phản ứng chuỗi polymerase", "Polymerase chain reaction that amplifies a DNA region.", "PCR amplified the 16S gene.")
v("IDT-02", "BLAST", "công cụ BLAST", "Basic Local Alignment Search Tool for sequence similarity searches.", "BLASTN compares nucleotide sequences.", ["BLASTN", "BLASTP"])
v("IDT-02", "query", "trình tự truy vấn", "The sequence submitted to BLAST.", "The query was 471 nt.", ["subject"])
v("IDT-02", "percent identity", "phần trăm giống hệt", "Identical positions divided by alignment length × 100%.", "The hit had 100% percent identity.", ["identity"])
v("IDT-02", "query cover", "độ phủ truy vấn", "Percentage of the query length covered by the alignment.", "Query cover was 100%.", ["query coverage"])
v("IDT-02", "E-value", "giá trị E", "Expected number of chance hits with at least this score.", "An E-value of 0.0 is highly significant.")
v("IDT-02", "accession", "mã truy cập", "Database identifier of a sequence record.", "JX293177.1 is an accession.", ["accession number"])
v("IDT-02", "phylogenetic tree", "cây phát sinh chủng loại", "A diagram hypothesizing evolutionary relationships.", "MEGA builds a phylogenetic tree.", ["phylogenetic trees"])
v("IDT-02", "multiple sequence alignment", "sắp gióng đa trình tự", "Alignment placing homologous positions of many sequences in columns.", "Multiple sequence alignment precedes tree building.")
v("IDT-02", "bootstrap", "bootstrap", "Resampling test of support for tree branches.", "A bootstrap of 95 is strong support.")
v("IDT-02", "homology", "tương đồng (cùng nguồn gốc)", "Similarity due to shared ancestry.", "BLAST searches for homology.")

fc("IDT-02", "fact", "Molecular identification steps?", "Specific gene → primer design & PCR → sequencing → BLAST → phylogenetic tree (MSA, model/method, reliability).")
fc("IDT-02", "fact", "Marker by group?", "Bacteria: 16S, 23S, rpoB. Eukaryotes: 18S. Fungi: ITS; yeasts: 25S (D1/D2).")
fc("IDT-02", "fact", "Identity vs query cover?", "Identity = identical/alignment length; query cover = aligned query length/query length.")
fc("IDT-02", "fact", "Lecture BLAST example?", "471 nt query; 100% identity & cover to Streptomyces flaveus X418 (1503 nt subject, 29–499) and Streptomyces sp. → genus-level conclusion.")
fc("IDT-02", "trap", "TRUE/FALSE: bootstrap 90 = 90% sequence similarity.", "FALSE – clade present in 90% of resampled trees.")

we("WE-13", "IDT-02", "Reading a BLAST alignment",
   "A 16S query is 520 nt long. The best hit aligns query positions 21–520 (no gaps) with 495 identical positions. Compute the alignment length, query cover and percent identity.",
   [S("Alignment length (nt) = 520 − 21 + 1?", 500),
    S("Query cover (%) = 500/520 × 100?", 96.15),
    S("Percent identity (%) = 495/500 × 100?", 99),
    S("Is 99% identity over 96% cover enough to name the species with certainty?", "no", input="choice", choices=["yes", "no"])],
   "Alignment 500 nt; query cover ≈ 96.2%; identity 99%; species not certain",
   "Độ dài căn chỉnh tính cả hai đầu. Identity và query cover có mẫu số khác nhau. 99% trên 16S thường chỉ gợi ý chi/loài gần – cần so với chủng chuẩn, gene khác và kiểu hình.")
