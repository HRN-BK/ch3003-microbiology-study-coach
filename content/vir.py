from _lib import *

SRC = "11.Viruses_Viroids_Prions.pptx"

# ---------------------------------------------------------------- VIR-01
unit("VIR-01", "Virions, virus classification and nomenclature (Herpesviridae)", "H", 1, 20, SRC + ": slides 1–11",
"""Thủy đậu hồi nhỏ, bệnh zona lúc về già, mụn rộp ở môi, u Kaposi ở bệnh nhân AIDS – nghe như 4 bệnh chẳng liên quan, nhưng đều do các thành viên của **một họ virus: Herpesviridae**. Muốn đọc được tên virus (chi, họ, bộ) và hiểu vì sao chúng "cùng họ", cần học quy tắc phân loại virus.""",
("A virus name ends in -viridae. Which taxonomic rank is this?",
 ["Genus", "Family", "Order", "Species"], 1,
 "Hậu tố **-viridae** = **họ (family)**; **-virus** = **chi (genus)**. (Slide 7 in nhầm \"-viridar\".)"),
[
("1. Virion là gì? (slide 4)", """
- **Virion** là **hạt virus hoàn chỉnh, phát triển đầy đủ, có khả năng lây nhiễm**, gồm **nucleic acid** được bao bởi **vỏ protein** (capsid) – vỏ **bảo vệ** genome khỏi môi trường và là **phương tiện truyền** từ tế bào chủ này sang tế bào chủ khác.
- Virus **không có cấu tạo tế bào**, **không có ribosome**, không tự chuyển hóa → **ký sinh nội bào bắt buộc**; chỉ nhân lên **bên trong tế bào chủ**.
- Kích thước rất nhỏ (khoảng **20–1000 nm**) – phần lớn chỉ thấy bằng **kính hiển vi điện tử**. [fig, mở rộng]

| Đặc điểm | Vi khuẩn | Virus |
|---|---|---|
| Cấu tạo tế bào | có | **không** |
| Nucleic acid | **cả DNA và RNA** | **DNA hoặc RNA** (một loại) |
| Ribosome | có | **không** |
| Nhân lên | phân đôi | **lắp ráp** từ các thành phần mới tổng hợp |
| Nhạy kháng sinh | thường có | **không** |
"""),
("2. Tiêu chí phân loại virus (slide 5–6)", """
Virus được phân loại dựa trên:
1. **Triệu chứng bệnh** (disease symptoms)
2. **Vật chủ bị nhiễm** (infected hosts: động vật, thực vật, vi khuẩn – phage)
3. **Hình thái virus** (viral morphology)
4. **Loại vật chất di truyền** (DNA/RNA, sợi đơn/kép)
5. **Cơ chế sao chép vật chất di truyền** (→ **hệ thống Baltimore**, slide 6)

**Hệ Baltimore** – mọi virus đều phải tạo **mRNA** để ribosome chủ dịch mã [fig]:

| Nhóm | Genome | Đường đến mRNA | Ví dụ |
|---|---|---|---|
| I | **dsDNA** | phiên mã trực tiếp | Herpes, Adeno, phage T4 |
| II | **ssDNA** | → dsDNA → mRNA | Parvovirus |
| III | **dsRNA** | RdRp của virus | Reovirus (rotavirus) |
| IV | **(+)ssRNA** | genome **chính là mRNA** | Polio, coronavirus |
| V | **(−)ssRNA** | RdRp tạo (+)mRNA | cúm, sởi, dại |
| VI | ssRNA-RT | RNA → DNA (**phiên mã ngược**) → mRNA | **HIV** (retrovirus) |
| VII | dsDNA-RT | qua RNA trung gian | viêm gan B |
"""),
("3. Quy tắc đặt tên (slide 7)", """
| Bậc | Hậu tố | Ví dụ |
|---|---|---|
| **Bộ (order)** | **-virales** (slide ghi \"-ales\") | *Herpesvirales* |
| **Họ (family)** | **-viridae** (slide in nhầm \"-viridar\") | *Herpesviridae* |
| **Chi (genus)** | **-virus** | *Simplexvirus* |

- **Loài virus (viral species)**: nhóm virus **có cùng thông tin di truyền và cùng ổ sinh thái (phạm vi vật chủ – host range)**.
- Loài virus được gọi bằng **tên thông thường mô tả** (vd human immunodeficiency virus); **phân loài** (nếu có) đánh **số** (HIV-1, HIV-2; HHV-1...).
"""),
("4. Herpesviridae – ví dụ họ virus (slide 9)", """
| Tên | Chi (genus) | Bệnh |
|---|---|---|
| **HHV-1 & HHV-2** | *Simplexvirus* | **mụn rộp môi (cold sores)**; HHV-2 chủ yếu herpes sinh dục |
| **HHV-3** | *Varicellovirus* | **thủy đậu (chickenpox)** (tái hoạt → zona) |
| **HHV-4** (Epstein-Barr) | *Lymphocryptovirus* | **tăng bạch cầu đơn nhân nhiễm trùng (infectious mononucleosis)** |
| **HHV-5** | *Cytomegalovirus* | **bệnh thể vùi CMV** |
| **HHV-6** | *Roseolovirus* | **roseola** (sốt phát ban trẻ nhỏ) |
| **HHV-7** | *Roseolovirus* | nhiễm hầu hết trẻ sơ sinh, **phát ban giống sởi** |
| **HHV-8** | *Rhadinovirus* | **u Kaposi (Kaposi's sarcoma)**, chủ yếu ở bệnh nhân **AIDS** |

Mẹo: 1-2 môi, 3 thủy đậu, 4 \"hôn\" (mono = bệnh nụ hôn), 5 CMV, 6-7 Roseolo, 8 Kaposi.
"""),
],
[
("Virus và thuốc", """
- Kháng sinh **không** diệt virus (không có thành peptidoglycan, ribosome riêng). Thuốc kháng virus nhắm enzyme đặc hiệu của virus: **acyclovir** (DNA polymerase của herpes), **thuốc ức chế reverse transcriptase và protease** (HIV), **oseltamivir** (neuraminidase cúm).
- Vaccine: thủy đậu (HHV-3), zona; ngừa HPV – liên hệ Jenner (HIS-04).
"""),
],
[
("Virion", "A **virion** is a complete, fully developed, **infectious** viral particle of **nucleic acid** surrounded by a **protein coat** that protects it and serves as a vehicle of transmission between host cells.", "Hạt virus hoàn chỉnh, lây nhiễm."),
("Classification and naming", "Viruses are classified by disease symptoms, hosts, morphology, type of genetic material and its replication mechanism (Baltimore). Genus **-virus**, family **-viridae**, order **-virales** (slide: -ales). A **viral species** shares the same genetic information and ecological niche (**host range**); common names, subspecies numbered.", "Chi -virus, họ -viridae."),
("Herpesviridae", "HHV-1/2 *Simplexvirus* (cold sores); HHV-3 *Varicellovirus* (chickenpox); HHV-4 *Lymphocryptovirus* (infectious mononucleosis); HHV-5 *Cytomegalovirus* (CMV inclusion disease); HHV-6/7 *Roseolovirus* (roseola; measles-like rashes in infants); HHV-8 *Rhadinovirus* (**Kaposi's sarcoma**, AIDS patients).", "HHV-1 → HHV-8."),
],
["-virus is the family suffix", "Viruses contain both DNA and RNA", "HHV-8 causes chickenpox"])

q("VIR-01", "recall", 1, "The suffix used for virus genus names is:",
  ["-viridae", "-virus", "-virales", "-virinae"], 1,
  "Slide 7: chi **-virus**; họ **-viridae**; bộ **-virales** (slide ghi -ales).",
  ["Họ.", "", "Bộ.", "Phân họ (không học)."], ["genus"], "-virus is the family suffix", src=SRC + " slide 7")
q("VIR-01", "recall", 1, "A complete, fully developed, infectious viral particle is called a:",
  ["capsomere", "virion", "prion", "viroid"], 1,
  "Slide 4: **virion**.",
  ["Đơn vị capsid.", "", "Protein gây bệnh.", "RNA trần."], ["virion"], src=SRC + " slide 4")
q("VIR-01", "recall", 1, "According to the lecture, a viral species is a group of viruses sharing:",
  ["the same capsid shape only", "the same genetic information and ecological niche (host range)", "the same disease symptoms only", "the same size"], 1,
  "Slide 7: **cùng thông tin di truyền và ổ sinh thái (phạm vi vật chủ)**.",
  ["Chưa đủ.", "", "Chưa đủ.", "Sai."], ["viral species", "host range"], src=SRC + " slide 7")
q("VIR-01", "recall", 1, "Which human herpesvirus causes Kaposi's sarcoma, primarily in AIDS patients?",
  ["HHV-3", "HHV-4", "HHV-6", "HHV-8"], 3,
  "Slide 9: **HHV-8**, chi *Rhadinovirus*.",
  ["Thủy đậu.", "Mono.", "Roseola.", ""], ["Herpesviridae"], "HHV-8 causes chickenpox", src=SRC + " slide 9")
q("VIR-01", "recall", 1, "HHV-3 (genus Varicellovirus) causes:",
  ["cold sores", "chickenpox", "infectious mononucleosis", "roseola"], 1,
  "Slide 9: HHV-3 → **thủy đậu**.",
  ["HHV-1/2.", "", "HHV-4.", "HHV-6."], ["Herpesviridae"], src=SRC + " slide 9")
q("VIR-01", "not", 2, "Which is NOT one of the criteria for classifying viruses in the lecture?",
  ["Disease symptoms", "Infected hosts", "Genetic material replication mechanisms", "Gram stain reaction"], 3,
  "Slide 5: triệu chứng, vật chủ, hình thái, loại vật chất di truyền, cơ chế sao chép. **Nhuộm Gram** dùng cho vi khuẩn.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["classification"], src=SRC + " slide 5")
q("VIR-01", "concept", 2, "Why does a (+)ssRNA virus not need to carry an RNA polymerase inside the virion to begin infection, while a (−)ssRNA virus does?",
  ["(+)RNA can act directly as mRNA; (−)RNA must first be copied into (+)mRNA by an RNA-dependent RNA polymerase", "(−)RNA is DNA", "(+)RNA viruses have no proteins", "(−)RNA can be read directly by ribosomes"], 0,
  "Hệ Baltimore: (+)RNA = mRNA → dịch mã ngay; (−)RNA cần RdRp của virus để tạo mRNA (ribosome chủ không đọc được).",
  ["", "Sai.", "Sai.", "Ngược."], ["Baltimore classification"])
q("VIR-01", "concept", 2, "HIV has an RNA genome but makes a DNA copy in the host cell. In the Baltimore system it is a:",
  ["dsDNA virus", "(−)ssRNA virus", "ssRNA-RT (retrovirus)", "dsRNA virus"], 2,
  "HIV là **retrovirus** (nhóm VI): RNA → DNA bằng **reverse transcriptase**.",
  ["Sai.", "Sai.", "", "Sai."], ["Baltimore classification", "retrovirus"])
q("VIR-01", "recall", 1, "Which pair is correctly matched?",
  ["HHV-4 – infectious mononucleosis", "HHV-5 – cold sores", "HHV-1 – Kaposi's sarcoma", "HHV-6 – chickenpox"], 0,
  "Slide 9: **HHV-4 (Lymphocryptovirus) – mono**. HHV-5: CMV; HHV-1: mụn rộp; HHV-6: roseola.",
  ["", "Sai.", "Sai.", "Sai."], ["Herpesviridae"], pool="mock")
q("VIR-01", "recall", 1, "Family names of viruses end in:",
  ["-virus", "-viridae", "-ales", "-aceae"], 1,
  "Họ: **-viridae**.",
  ["Chi.", "", "Bộ (slide).", "Họ vi khuẩn/thực vật."], ["family"], pool="mock")
q("VIR-01", "not", 2, "Which statement about viruses is NOT correct?",
  ["They contain either DNA or RNA", "They lack ribosomes", "They can multiply only inside host cells", "They reproduce by binary fission"], 3,
  "Virus nhân lên bằng **tổng hợp thành phần rồi lắp ráp**, không phân đôi.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["virion"], "Viruses contain both DNA and RNA", pool="mock")

v("VIR-01", "virion", "hạt virus (virion)", "A complete, fully developed, infectious viral particle.", "The virion carries the genome between cells.", ["virions"])
v("VIR-01", "virus", "virus", "An acellular obligate intracellular parasite with a DNA or RNA genome.", "Viruses lack ribosomes.", ["viruses", "viral"])
v("VIR-01", "Baltimore classification", "phân loại Baltimore", "Grouping of viruses by genome type and route to mRNA.", "HIV is group VI in the Baltimore classification.")
v("VIR-01", "viral species", "loài virus", "Viruses sharing the same genetic information and host range.", "Each viral species has a common name.")
v("VIR-01", "host range", "phạm vi vật chủ", "The range of hosts or cells a virus can infect.", "Phages have narrow host ranges.")
v("VIR-01", "Herpesviridae", "họ Herpes", "The herpesvirus family, HHV-1 to HHV-8.", "Herpesviridae includes Varicellovirus.", ["herpesviruses", "HHV"])
v("VIR-01", "genus", "chi", "Taxonomic rank; virus genus names end in -virus.", "Simplexvirus is a genus.")
v("VIR-01", "family", "họ", "Taxonomic rank; virus family names end in -viridae.", "Herpesviridae is a family.")
v("VIR-01", "Kaposi's sarcoma", "u Kaposi", "Cancer caused by HHV-8, mainly in AIDS patients.", "HHV-8 causes Kaposi's sarcoma.")
v("VIR-01", "chickenpox", "bệnh thủy đậu", "Disease caused by HHV-3 (Varicellovirus).", "Chickenpox is caused by HHV-3.")

fc("VIR-01", "fact", "Virus naming suffixes?", "Genus -virus; family -viridae; order -virales (slide: -ales).")
fc("VIR-01", "fact", "HHV-1 to HHV-8?", "1-2 cold sores (Simplex); 3 chickenpox (Varicello); 4 mono (Lymphocrypto); 5 CMV; 6 roseola; 7 measles-like rash infants (Roseolo); 8 Kaposi's sarcoma (Rhadino).")
fc("VIR-01", "fact", "Five virus classification criteria?", "Disease symptoms, hosts, morphology, genetic material type, replication mechanism.")
fc("VIR-01", "trap", "Slide typo: family suffix?", "-viridae (slide printed -viridar).")

# ---------------------------------------------------------------- VIR-02
unit("VIR-02", "Virus structure: genome, capsid, capsomeres, envelope and spikes; phages", "H", 1, 20, SRC + ": slides 12–19",
"""Vì sao rửa tay bằng xà phòng diệt được virus cúm và SARS-CoV-2 khá tốt, nhưng lại kém với norovirus gây ngộ độc thực phẩm? Câu trả lời nằm ở **cấu trúc hạt virus**: loại có **vỏ bao lipid (envelope)** thì xà phòng, cồn phá được lớp màng; loại **trần** chỉ có capsid protein thì bền hơn nhiều.""",
("Which structure is present in ALL virions?",
 ["Envelope", "Spikes", "Capsid (protein coat) around the nucleic acid", "Tail fibers"], 2,
 "Mọi virion có **nucleic acid + capsid**. Envelope, spike, đuôi chỉ có ở một số virus."),
[
("1. Nucleic acid (slide 12)", """
Genome virus có thể là:
- **DNA hoặc RNA** (không bao giờ cả hai trong virion);
- **sợi đơn (ss) hoặc sợi kép (ds)**;
- **thẳng (linear) hoặc vòng (circular)**;
- gồm **một hoặc nhiều nhiễm sắc thể** (phân đoạn – vd cúm có 8 đoạn RNA).
"""),
("2. Capsid và capsomere (slide 13–14)", """
- **Capsid**: **vỏ protein bao quanh genome** virus.
- Hình dạng capsid: **hình que/xoắn (rod-shaped/helical)** (virus khảm thuốc lá, dại), **đa diện (polyhedral)** – thường là **khối 20 mặt (icosahedron)** (adenovirus, polio), **phức tạp (complex)** (phage T4, poxvirus).
- Capsid gồm các **tiểu đơn vị protein gọi là capsomeres**. Một capsomere có thể **gồm một hoặc nhiều protein**. **Cách sắp xếp capsomere là đặc trưng cho từng virus**.
- **Nucleocapsid** = nucleic acid + capsid. [mở rộng]
"""),
("3. Envelope và spikes (slide 15–17)", """
- **Envelope (vỏ bao)**: lớp **bao ngoài capsid**, thường gồm **lipid, protein và carbohydrate**.
- Envelope có thể có **nguồn gốc từ tế bào chủ** (lipid lấy từ màng chủ khi **nảy chồi**) **hoặc do virus mã hóa** (các protein virus).
- Tùy loài, envelope có thể được phủ **phức hợp protein–carbohydrate gọi là spikes (gai)** – vd **hemagglutinin (H)** và **neuraminidase (N)** của cúm → tên H1N1, H5N1. [mở rộng]
- Virus **không có envelope** = **virus trần (non-enveloped/naked)** – vẫn có capsid.

| | Virus có envelope | Virus trần |
|---|---|---|
| Lớp ngoài cùng | màng lipid + spikes | capsid protein |
| Xà phòng, cồn, dung môi lipid | **dễ bất hoạt** | **bền hơn** |
| Ví dụ | cúm, HIV, herpes, SARS-CoV-2 | norovirus, polio, adenovirus |
"""),
("4. Chức năng capsid và envelope (slide 18)", """
- **Giúp virus tiếp xúc và tấn công tế bào** (gắn thụ thể – \"ổ khóa – chìa khóa\").
- **Bảo vệ nucleic acid** của virus (khỏi enzyme nuclease, môi trường).
"""),
("5. Virus phức tạp – bacteriophage (slide 19)", """
- **Bacteriophages (phage)**: virus **tấn công tế bào vi khuẩn**; đặt tên **Type 1 (T1), T2, … T7**.
- **Phage T-chẵn (T2, T4, T6)** có cấu trúc phức tạp: **đầu (head)** đa diện chứa **dsDNA**; **cổ (collar)**; **bao đuôi (tail sheath)** co rút; **lõi đuôi (tail core)**; **tấm đáy (base plate)**; **sợi đuôi (tail fibers)** gắn vào thụ thể trên thành vi khuẩn. [fig]
"""),
],
[
("Ứng dụng: phage trong công nghiệp và y học", """
- **Nhiễm phage** là tai họa lớn trong nhà máy **sữa chua, phô mai** (phage *Lactococcus* làm hỏng mẻ lên men) → luân phiên chủng khởi động, vệ sinh CIP.
- **Liệu pháp phage (phage therapy)** được thử nghiệm để trị vi khuẩn **đa kháng kháng sinh**.
- Phage lambda, M13 là công cụ **vector nhân dòng** và **phage display** (Nobel Hóa 2018).
"""),
],
[
("Genome", "Viral nucleic acid is **DNA or RNA**, **single- or double-stranded**, **linear or circular**, and consists of **one or more chromosomes**.", "DNA hoặc RNA."),
("Capsid", "The **capsid** is the protein coat around the genome; shape **rod-shaped (helical), polyhedral or complex**. It is built of protein subunits called **capsomeres** (one or more proteins each); their arrangement is **specific to each virus**.", "Capsid từ capsomeres."),
("Envelope and spikes", "An **envelope** covers the capsid; lipids, proteins and carbohydrates; of **host cell origin or virally encoded**. May bear **spikes** (protein–carbohydrate complexes). Functions: **contact/attack the cell** and **protect the nucleic acid**. Complex viruses: **bacteriophages** T1–T7.", "Envelope, spikes, phage."),
],
["Naked viruses have no capsid", "A capsomere is always a single protein", "Envelopes are made entirely by the virus"])

q("VIR-02", "recall", 1, "The protein subunits that make up a viral capsid are called:",
  ["spikes", "capsomeres", "prions", "nucleocapsids"], 1,
  "Slide 13: capsid gồm các tiểu đơn vị protein gọi là **capsomeres**.",
  ["Trên envelope.", "", "Protein gây bệnh.", "Capsid + nucleic acid."], ["capsomere"], src=SRC + " slide 13")
q("VIR-02", "recall", 1, "The three capsid shapes listed in the lecture are:",
  ["coccus, bacillus, spiral", "rod-shaped, polyhedral, complex", "haploid, diploid, polyploid", "linear, circular, segmented"], 1,
  "Slide 13: **rod-shaped, polyhedral, complex**.",
  ["Hình dạng vi khuẩn.", "", "Sai.", "Dạng genome."], ["capsid"], src=SRC + " slide 13")
q("VIR-02", "concept", 2, "According to the lecture, the viral envelope may be:",
  ["always made entirely by the virus", "of host cell origin or virally encoded", "made of peptidoglycan", "absent in all animal viruses"], 1,
  "Slide 16: envelope **có thể có nguồn gốc tế bào chủ hoặc do virus mã hóa**.",
  ["Sai.", "", "Sai.", "Sai."], ["envelope"], "Envelopes are made entirely by the virus", src=SRC + " slide 16")
q("VIR-02", "recall", 1, "Protein–carbohydrate complexes that project from the envelope of some viruses are:",
  ["capsomeres", "spikes", "pili", "fimbriae"], 1,
  "Slide 17: **spikes**.",
  ["Đơn vị capsid.", "", "Vi khuẩn.", "Vi khuẩn."], ["spikes"], src=SRC + " slide 17")
q("VIR-02", "not", 2, "Which statement about viral nucleic acid is NOT correct?",
  ["It may be DNA or RNA", "It may be single- or double-stranded", "It may be linear or circular", "Every virion contains both DNA and RNA"], 3,
  "Slide 12: DNA **hoặc** RNA.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["nucleic acid"], src=SRC + " slide 12")
q("VIR-02", "application", 2, "Hand sanitizer (70% alcohol) inactivates influenza virus much more easily than norovirus. The best explanation is:",
  ["Influenza has an envelope (lipid membrane) that alcohol disrupts; norovirus is naked", "Norovirus has an envelope", "Influenza has no capsid", "Alcohol destroys only DNA"], 0,
  "Virus **có envelope lipid** dễ bị cồn/xà phòng phá; **virus trần** chỉ có capsid bền hơn (liên hệ CTL-04).",
  ["", "Ngược.", "Virus nào cũng có capsid.", "Sai."], ["envelope"])
q("VIR-02", "concept", 2, "Which is a function of the capsid and envelope given in the lecture?",
  ["Producing ATP", "Helping the virus contact and attack the cell, and protecting the viral nucleic acid", "Synthesizing proteins", "Replicating the genome outside cells"], 1,
  "Slide 18: **giúp tiếp xúc, tấn công tế bào** và **bảo vệ nucleic acid**.",
  ["Virus không tạo ATP.", "", "Cần ribosome chủ.", "Không thể."], ["capsid"])
q("VIR-02", "recall", 1, "Bacteriophages are viruses that attack:",
  ["plant cells", "animal cells", "bacterial cells", "fungal cells"], 2,
  "Slide 19: phage tấn công **vi khuẩn**.",
  ["Sai.", "Sai.", "", "Sai."], ["bacteriophage"], pool="mock")
q("VIR-02", "concept", 2, "A capsomere, according to the lecture:",
  ["is always one protein molecule", "can be made up of one or more proteins, and the arrangement of capsomeres is specific to each virus", "is a lipid unit", "is found only in enveloped viruses"], 1,
  "Slide 13: capsomere **một hoặc nhiều protein**; sắp xếp **đặc trưng từng virus**.",
  ["Sai.", "", "Sai.", "Mọi virus."], ["capsomere"], "A capsomere is always a single protein", pool="mock")
q("VIR-02", "not", 2, "Which statement about viral envelopes is NOT correct?",
  ["They cover the capsid", "They are commonly composed of lipids, proteins and carbohydrates", "They may carry spikes", "They are present in every virus"], 3,
  "Virus **trần** không có envelope.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["envelope"], "Naked viruses have no capsid", pool="mock")

v("VIR-02", "capsid", "vỏ capsid", "The protein coat surrounding a viral genome.", "The capsid protects viral nucleic acid.", ["capsids"])
v("VIR-02", "capsomere", "capsomere (đơn vị vỏ)", "Protein subunit of a capsid.", "Capsomeres assemble into the capsid.", ["capsomeres"])
v("VIR-02", "envelope", "vỏ bao ngoài", "A lipid-protein-carbohydrate layer covering the capsid of some viruses.", "Influenza has an envelope.", ["enveloped"])
v("VIR-02", "spikes", "gai (spike)", "Protein-carbohydrate projections on a viral envelope.", "Spikes bind host receptors.", ["spike"])
v("VIR-02", "nucleocapsid", "nucleocapsid", "The viral nucleic acid plus its capsid.", "The nucleocapsid lies inside the envelope.")
v("VIR-02", "polyhedral", "đa diện", "Capsid shape with many faces, often an icosahedron.", "Adenovirus is polyhedral.", ["icosahedral"])
v("VIR-02", "bacteriophage", "thể thực khuẩn (phage)", "A virus that infects bacteria.", "T4 is a bacteriophage.", ["bacteriophages", "phage", "phages"])
v("VIR-02", "tail fibers", "sợi đuôi", "Phage structures that attach to bacterial receptors.", "Tail fibers bind E. coli.", ["tail fiber"])
v("VIR-02", "naked virus", "virus trần", "A virus without an envelope.", "Norovirus is a naked virus.", ["non-enveloped"])

fc("VIR-02", "fact", "Viral genome possibilities?", "DNA or RNA; ss or ds; linear or circular; one or more chromosomes.")
fc("VIR-02", "fact", "Capsid shapes?", "Rod-shaped (helical), polyhedral, complex.")
fc("VIR-02", "fact", "Envelope composition and origin?", "Lipids, proteins, carbohydrates; host cell origin or virally encoded; may carry spikes.")
fc("VIR-02", "trap", "TRUE/FALSE: a naked virus has no capsid.", "FALSE – it lacks only an envelope.")

# ---------------------------------------------------------------- VIR-03
unit("VIR-03", "Viral multiplication: animal viruses, HIV, lytic and lysogenic phage cycles", "H", 2, 30, SRC + ": slides 20–34",
"""Vì sao một tế bào vi khuẩn bị phage T4 tấn công lại vỡ tung sau khoảng 25 phút, giải phóng ~200 phage con; còn tế bào mang phage lambda thì vẫn sống, phân chia bình thường nhiều thế hệ – cho tới khi bị chiếu UV thì đột ngột vỡ hàng loạt? Đó là khác biệt giữa **chu trình tan** và **chu trình tiềm tan**.""",
("Why can viruses multiply only inside host cells?",
 ["They are too small", "They lack ribosomes and metabolic machinery", "They are killed by oxygen", "They have no nucleic acid"], 1,
 "Slide 20: virus **không có ribosome** → không thể tự tổng hợp protein, không thể nhân lên ngoài tế bào chủ."),
[
("1. Nguyên tắc chung (slide 20–21)", """
- Virus **chỉ nhân lên trong tế bào chủ**; **không có ribosome** nên không thể nhân lên bên ngoài.
- Nhận biết tế bào chủ theo cơ chế **\"ổ khóa – chìa khóa\" (lock & key)**: **protein bề mặt virus** khớp với **phân tử thụ thể đặc hiệu** trên tế bào chủ → giải thích **phạm vi vật chủ** và **tính hướng mô**.
- Cách xâm nhập phụ thuộc loại virus và tế bào:
  - **Phage T-chẵn**: dùng **bộ máy đuôi** phức tạp **chọc thủng thành vi khuẩn**, bơm DNA vào (capsid ở ngoài).
  - Một số virus vào bằng **nhập bào (endocytosis)**.
  - **Virus có envelope**: **hòa màng (fusion)** với màng sinh chất chủ.
"""),
("2. Các bước nhân lên của virus (slide 24–27)", """
**Bám (attachment) → xâm nhập (penetration/entry) → tháo vỏ (uncoating) → tổng hợp (biosynthesis) → lắp ráp (assembly/maturation) → giải phóng (release)**

- Trong tế bào, **protein virus điều khiển tế bào chủ**, tái lập trình để **sao chép nucleic acid virus** và **tạo protein virus**.
- **Tế bào chủ cung cấp**: **nucleotide** (tạo nucleic acid virus), **enzyme, ribosome, tRNA, amino acid, ATP** và các thành phần khác để làm protein virus.
- **Virus DNA** dùng **DNA polymerase của tế bào chủ** để tổng hợp genome từ khuôn DNA virus (theo slide; một số virus DNA lớn như herpes, pox mã hóa polymerase riêng).
- **Virus RNA** dùng **polymerase của virus** (RNA-dependent RNA polymerase – RdRp) để sao chép genome từ khuôn RNA (tế bào chủ không có enzyme này).
- Sau khi nucleic acid và capsomere được tạo ra, chúng **lắp ráp ngay** thành virus mới (slide 25).
- Giải phóng: **ly giải** (virus trần) hoặc **nảy chồi (budding)** – virus có envelope lấy màng chủ làm envelope.
"""),
("3. HIV – retrovirus (slide 29)", """
1. **gp120** (spike) gắn **thụ thể CD4** (và đồng thụ thể CCR5/CXCR4) trên **tế bào T hỗ trợ**.
2. **Hòa màng** → capsid vào tế bào chất, tháo vỏ.
3. **Reverse transcriptase** (phiên mã ngược): **RNA → DNA** (sợi kép).
4. DNA vào nhân, **integrase** chèn vào nhiễm sắc thể chủ → **provirus** (có thể tiềm ẩn nhiều năm).
5. Phiên mã → mRNA và RNA genome mới; dịch mã → protein; **protease** cắt protein tiền thân.
6. Lắp ráp, **nảy chồi** qua màng → virion có envelope.

Các thuốc ARV nhắm đúng các enzyme: **ức chế reverse transcriptase, integrase, protease**. [mở rộng]
"""),
("4. Chu trình tan – lytic cycle (slide 30–31)", """
- **Phage vào tế bào, nhân lên và phá hủy tế bào chủ** để phage mới thoát ra.
- Mỗi phage mới lại tấn công tế bào khác → vài chu trình tan tiếp theo **phá hủy toàn bộ quần thể tế bào chủ chỉ trong vài giờ**.
- Phage **chỉ nhân lên bằng chu trình tan** = **phage độc (virulent phage)** (vd T4).

Ví dụ T4 ở *E. coli* [fig]: (1) **bám** – sợi đuôi gắn thụ thể; (2) **xâm nhập** – lysozyme đuôi làm yếu thành, bao đuôi co, lõi đuôi bơm DNA; (3) **sinh tổng hợp** – DNA chủ bị phân hủy, tổng hợp DNA và protein phage; (4) **trưởng thành** – lắp đầu, đuôi, DNA; (5) **giải phóng** – **lysozyme** phá thành → ly giải.
"""),
("5. Chu trình tiềm tan – lysogenic cycle (slide 32–34)", """
- **Phage lambda (λ)**: **phage ôn hòa (temperate phage)** – nhân lên được **cả bằng chu trình tan và tiềm tan**. Cấu trúc giống T4 nhưng đuôi chỉ có **một sợi đuôi ngắn**.
- Trong tiềm tan: phage vào tế bào, **genome phage được sao chép nhưng tế bào chủ không bị phá hủy**.
- Các bước: DNA λ vòng hóa → **tích hợp vào nhiễm sắc thể vi khuẩn** thành **prophage** → nhân đôi cùng NST chủ khi tế bào phân chia → quần thể **tế bào tiềm tan (lysogen)**.
- **Cảm ứng (induction)**: tác nhân gây tổn thương DNA (UV, hóa chất) → prophage **cắt ra** → vào **chu trình tan**.
- Hệ quả [mở rộng]: **miễn dịch với phage cùng loại**; **chuyển đổi tiềm tan (lysogenic conversion)** – gene phage làm vi khuẩn độc hơn (độc tố bạch hầu, độc tố tả, độc tố Shiga); **tải nạp chuyên biệt**.

| | Tan (lytic) | Tiềm tan (lysogenic) |
|---|---|---|
| Kết cục tế bào chủ | **bị phá hủy** | **sống**, phân chia |
| DNA phage | nhân lên, lắp hạt | **prophage** tích hợp, sao chép cùng NST |
| Loại phage | độc (T4) và ôn hòa | chỉ **ôn hòa** (λ) |
| Chuyển sang | – | tan khi **cảm ứng** |
"""),
],
[
("Đếm phage bằng plaque assay", """
Trộn phage pha loãng với vi khuẩn chủ trên thạch → mỗi phage tạo một **vết tan (plaque)** trong thảm vi khuẩn → đếm **PFU (plaque-forming units)**.

> Công thức: **PFU/mL = số plaque ÷ (thể tích cấy mL × độ pha loãng)** – giống CFU (GRO-06).

Ví dụ: 0,1 mL dịch pha loãng 10⁻⁶ cho 150 plaque → 150 / (0,1 × 10⁻⁶) = **1,5 × 10⁹ PFU/mL**.
"""),
("Nhiễm virus tiềm ẩn ở người", """
Herpes cũng có trạng thái **tiềm ẩn (latency)** trong tế bào thần kinh – giống ý tưởng tiềm tan: HHV-3 gây thủy đậu lúc nhỏ, nằm im ở hạch thần kinh, tái hoạt khi miễn dịch giảm → **zona**. HIV ở dạng provirus trong tế bào T nghỉ là lý do chưa chữa khỏi hoàn toàn.
"""),
],
[
("Host dependence and entry", "Viruses multiply only inside host cells; they **lack ribosomes**. Recognition by **lock & key**: viral surface proteins match specific host receptors. **T-even phages** puncture cell walls with their tail; some viruses enter by **endocytosis**; **enveloped viruses** enter by **fusion** with the plasma membrane.", "Ổ khóa – chìa khóa."),
("Biosynthesis and assembly", "Host provides **nucleotides, enzymes, ribosomes, tRNAs, amino acids, ATP**. **DNA viruses use host DNA polymerase**; **RNA viruses use viral polymerase**. Nucleic acids and capsomeres **assemble** into new virions. HIV: **reverse transcriptase** RNA → DNA, integration as **provirus**, budding.", "Chủ cung cấp nguyên liệu."),
("Lytic vs lysogenic", "**Lytic**: phage multiplies and **destroys** the host; successive cycles destroy a population in hours; **virulent phages** only lytic. **Lysogenic**: genome replicated but host **not destroyed** (**prophage**). **Phage lambda** is **temperate** (both cycles); like T4 but tail has **one short tail fiber**.", "Tan vs tiềm tan."),
],
["RNA viruses use host RNA polymerase to copy their genome", "Temperate phages can only undergo the lytic cycle", "In lysogeny the host cell is lysed immediately"])

q("VIR-03", "recall", 1, "Viruses recognize host cells by:",
  ["random collision followed by phagocytosis", "a lock & key match between viral surface proteins and specific host receptor molecules", "chemotaxis with flagella", "attraction to host DNA"], 1,
  "Slide 20: cơ chế **\"lock & key\"**.",
  ["Sai.", "", "Virus không có roi.", "Sai."], ["lock and key", "receptor"], src=SRC + " slide 20")
q("VIR-03", "recall", 1, "Enveloped animal viruses typically enter host cells by:",
  ["puncturing the cell wall with a tail", "fusion with the host plasma membrane", "conjugation", "binary fission"], 1,
  "Slide 21: virus có envelope **hòa màng** với màng sinh chất chủ.",
  ["Phage T-chẵn.", "", "Vi khuẩn.", "Sai."], ["fusion", "envelope"], src=SRC + " slide 21")
q("VIR-03", "concept", 2, "According to the lecture, RNA viruses replicate their genomes using:",
  ["host DNA polymerase", "viral polymerase using RNA templates", "host ribosomes", "reverse transcriptase always"], 1,
  "Slide 24: **virus RNA dùng polymerase của virus** dựa trên khuôn RNA; virus DNA dùng DNA polymerase chủ.",
  ["Virus DNA.", "", "Ribosome dịch mã protein.", "Chỉ retrovirus."], ["RNA-dependent RNA polymerase"], "RNA viruses use host RNA polymerase to copy their genome", src=SRC + " slide 24")
q("VIR-03", "not", 2, "Which component is NOT supplied by the host cell for viral multiplication, according to the lecture?",
  ["Nucleotides", "Ribosomes and tRNAs", "ATP and amino acids", "The viral genome template"], 3,
  "Slide 24: chủ cung cấp nucleotide, enzyme, ribosome, tRNA, amino acid, ATP; **khuôn genome** do virus mang vào.",
  ["Chủ cung cấp.", "Chủ cung cấp.", "Chủ cung cấp.", ""], ["host cell"], src=SRC + " slide 24")
q("VIR-03", "recall", 1, "Phages that can multiply only through lytic cycles are called:",
  ["temperate phages", "virulent phages", "prophages", "lysogens"], 1,
  "Slide 30: **virulent phages**.",
  ["Cả tan và tiềm tan.", "", "DNA phage tích hợp.", "Tế bào mang prophage."], ["virulent phage", "lytic cycle"], src=SRC + " slide 30")
q("VIR-03", "recall", 1, "Phage lambda is described as a temperate phage because it:",
  ["only undergoes lysis", "can multiply through both lytic and lysogenic cycles", "has no tail", "infects only animal cells"], 1,
  "Slide 32: **temperate** = nhân lên được bằng **cả chu trình tan và tiềm tan**.",
  ["Phage độc.", "", "Có đuôi.", "Nhiễm vi khuẩn."], ["temperate phage", "lambda"], "Temperate phages can only undergo the lytic cycle", src=SRC + " slide 32")
q("VIR-03", "concept", 2, "In the lysogenic cycle:",
  ["the host cell is destroyed immediately", "the phage genome is replicated but the host cell is not destroyed", "no phage DNA enters the cell", "the phage divides by fission"], 1,
  "Slide 33: genome phage **được sao chép nhưng tế bào không bị phá hủy** (prophage).",
  ["Đó là tan.", "", "Sai.", "Sai."], ["lysogenic cycle", "prophage"], "In lysogeny the host cell is lysed immediately", src=SRC + " slide 33")
q("VIR-03", "recall", 1, "Compared with T4, the tail of phage lambda has:",
  ["six long tail fibers", "only one short tail fiber", "no tail at all", "a contractile sheath with pili"], 1,
  "Slide 32: cấu trúc giống T4 nhưng đuôi chỉ có **một sợi đuôi ngắn**.",
  ["T4.", "", "Sai.", "Sai."], ["lambda"], src=SRC + " slide 32")
q("VIR-03", "concept", 2, "Which HIV enzyme converts the viral RNA genome into DNA?",
  ["Integrase", "Protease", "Reverse transcriptase", "RNA polymerase II"], 2,
  "**Reverse transcriptase** (phiên mã ngược) RNA → DNA; integrase chèn DNA vào NST chủ; protease cắt protein.",
  ["Tích hợp.", "Cắt protein.", "", "Enzyme chủ tạo mRNA."], ["reverse transcriptase", "HIV"])
q("VIR-03", "application", 3, "A lysogenic E. coli culture is exposed to UV light. Soon after, many cells lyse and release phages. What happened?",
  ["UV killed the phages", "UV induced the prophage to excise and enter the lytic cycle", "The cells formed endospores", "UV converted lambda into a virulent T4 phage"], 1,
  "Tổn thương DNA do UV **cảm ứng (induction)** prophage → cắt ra → chu trình tan.",
  ["Ngược.", "", "E. coli không tạo nội bào tử.", "Sai."], ["prophage", "induction"])
q("VIR-03", "calc", 2, "0.1 mL of a 10^-6 dilution of a phage lysate produces 150 plaques on a bacterial lawn. What is the phage titer?",
  ["1.5 × 10^7 PFU/mL", "1.5 × 10^8 PFU/mL", "1.5 × 10^9 PFU/mL", "1.5 × 10^10 PFU/mL"], 2,
  "PFU/mL = 150 / (0,1 × 10⁻⁶) = **1,5 × 10⁹**.",
  ["Quên chia 0,1 và sai mũ.", "Quên chia cho 0,1 mL.", "", "Sai mũ."], ["plaque"])
q("VIR-03", "concept", 2, "How do T-even phages deliver their DNA into bacteria?",
  ["By endocytosis", "By membrane fusion", "By using their elaborate tail apparatus to puncture the bacterial cell wall", "By conjugation pili"], 2,
  "Slide 21: phage T-chẵn dùng **bộ máy đuôi** chọc thủng thành vi khuẩn.",
  ["Tế bào động vật.", "Virus có envelope.", "", "Sai."], ["bacteriophage"], pool="mock")
q("VIR-03", "not", 2, "Which statement about the lytic cycle is NOT correct?",
  ["The phage multiplies and destroys the host cell", "New phages can attack other host cells", "Successive lytic cycles can destroy a host population within hours", "The phage genome integrates as a prophage and the host survives"], 3,
  "Prophage là đặc trưng của **tiềm tan**.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["lytic cycle"], pool="mock")
q("VIR-03", "concept", 2, "Why can't viruses multiply outside a host cell, according to the lecture?",
  ["They have no nucleic acid", "They do not have ribosomes", "They have cell walls", "They need light"], 1,
  "Slide 20: **không có ribosome**.",
  ["Có.", "", "Không có thành.", "Sai."], ["virus"], pool="mock")
q("VIR-03", "calc", 2, "0.2 mL of a 10^-5 dilution gives 84 plaques. Phage titer (PFU/mL) is:",
  ["4.2 × 10^6", "4.2 × 10^7", "8.4 × 10^6", "1.68 × 10^6"], 1,
  "PFU/mL = 84 / (0,2 × 10⁻⁵) = 84 / (2 × 10⁻⁶) = 42 × 10⁶ = **4,2 × 10⁷**.",
  ["Sai một bậc 10.", "", "Quên chia cho 0,2 mL (và sai mũ).", "Nhân với 0,2 thay vì chia."], ["plaque"], pool="mock")

v("VIR-03", "lock and key", "cơ chế ổ khóa – chìa khóa", "Matching of viral surface proteins with specific host receptors.", "Host recognition works by lock and key.")
v("VIR-03", "receptor", "thụ thể", "A host surface molecule bound by a virus.", "HIV binds the CD4 receptor.", ["receptors"])
v("VIR-03", "endocytosis", "nhập bào", "Uptake of particles by membrane invagination.", "Some viruses enter by endocytosis.")
v("VIR-03", "fusion", "hòa màng", "Merging of the viral envelope with the host membrane.", "Enveloped viruses enter by fusion.")
v("VIR-03", "uncoating", "tháo vỏ", "Release of the viral genome from the capsid.", "Uncoating follows entry.")
v("VIR-03", "budding", "nảy chồi (virus)", "Release of enveloped viruses through a host membrane.", "HIV is released by budding.")
v("VIR-03", "RNA-dependent RNA polymerase", "RNA polymerase phụ thuộc RNA", "Viral enzyme that copies RNA from an RNA template.", "RNA viruses carry their own polymerase.", ["RdRp", "viral polymerase"])
v("VIR-03", "reverse transcriptase", "enzyme phiên mã ngược", "Enzyme that makes DNA from an RNA template.", "HIV reverse transcriptase makes DNA.")
v("VIR-03", "HIV", "HIV", "Human immunodeficiency virus, a retrovirus.", "HIV infects CD4 T cells.", ["retrovirus"])
v("VIR-03", "provirus", "tiền virus", "Viral DNA integrated into a host chromosome.", "HIV persists as a provirus.")
v("VIR-03", "lytic cycle", "chu trình tan", "Phage cycle ending in lysis of the host cell.", "T4 follows the lytic cycle.", ["lytic", "lysis"])
v("VIR-03", "lysogenic cycle", "chu trình tiềm tan", "Phage cycle in which the genome is maintained without killing the host.", "Lambda can enter the lysogenic cycle.", ["lysogeny", "lysogenic", "lysogen"])
v("VIR-03", "virulent phage", "phage độc", "A phage that multiplies only by the lytic cycle.", "T4 is a virulent phage.", ["virulent phages"])
v("VIR-03", "temperate phage", "phage ôn hòa", "A phage able to undergo both lytic and lysogenic cycles.", "Lambda is a temperate phage.", ["temperate"])
v("VIR-03", "prophage", "prophage (tiền phage)", "Phage DNA integrated into the bacterial chromosome.", "The prophage replicates with the host chromosome.")
v("VIR-03", "lambda", "phage lambda", "A temperate E. coli phage with one short tail fiber.", "Lambda integrates as a prophage.", ["phage lambda", "λ"])
v("VIR-03", "induction", "cảm ứng (prophage)", "Excision of a prophage triggered by DNA damage, starting the lytic cycle.", "UV causes induction.")
v("VIR-03", "plaque", "vết tan", "A clear zone in a bacterial lawn formed by phage lysis.", "Plaques are counted as PFU.", ["PFU", "plaques"])

fc("VIR-03", "fact", "Three entry mechanisms (lecture)?", "T-even phage tail punctures wall; endocytosis; fusion (enveloped viruses).")
fc("VIR-03", "fact", "DNA vs RNA virus genome replication (lecture)?", "DNA viruses: host DNA polymerase. RNA viruses: viral polymerase on RNA templates.")
fc("VIR-03", "fact", "Virulent vs temperate phage?", "Virulent: lytic only (T4). Temperate: lytic and lysogenic (lambda).")
fc("VIR-03", "fact", "HIV key steps?", "gp120–CD4 binding, fusion, reverse transcription, integration (provirus), transcription/translation, protease, budding.")
fc("VIR-03", "trap", "Lambda tail vs T4 tail?", "Lambda: one short tail fiber; T4: several long tail fibers.")

we("WE-11", "VIR-03", "Phage titer by plaque assay",
   "A phage lysate is serially diluted. 0.1 mL of the 10^-7 dilution mixed with host E. coli in soft agar gives 62 plaques. Find the titer (PFU/mL).",
   [S("Volume plated (mL)?", 0.1),
    S("Dilution factor of the plated tube (as a number, e.g. 1e-7)?", 1e-7),
    S("Amount of original lysate plated (mL) = volume × dilution?", 1e-8),
    S("Titer = plaques / amount of original lysate (PFU/mL)?", 6.2e9)],
   "6.2 × 10^9 PFU/mL",
   "Tính như CFU: PFU/mL = số plaque / (thể tích × độ pha loãng) = 62 / (0,1 × 10⁻⁷) = 62 / 10⁻⁸ = 6,2 × 10⁹.")

# ---------------------------------------------------------------- VIR-04
unit("VIR-04", "Viroids, virusoids and prions", "M", 1, 15, SRC + ": slides 35–44",
"""Ở Philippines, hàng chục triệu cây dừa đã chết vì bệnh **cadang-cadang** – tác nhân chỉ là một **sợi RNA vòng trần chưa tới 400 nucleotide**, không có vỏ protein, không mã hóa protein nào. Còn bệnh **bò điên** thì thủ phạm lại là một **protein** không có gene. Đây là những tác nhân gây bệnh \"nhỏ hơn virus\".""",
("What is a viroid?",
 ["A small virus with a DNA genome", "A short piece of naked RNA with no protein coat", "A misfolded protein", "A bacterium without a wall"], 1,
 "Slide 37: viroid = **đoạn RNA trần ngắn (300–400 nt)**, **không có vỏ protein**."),
[
("1. Viroid (slide 37)", """
- **Đoạn RNA trần ngắn**, chỉ **300–400 nucleotide**, **không có vỏ protein**.
- Các nucleotide thường **bắt cặp nội phân tử** → phân tử có **cấu trúc 3D khép kín, gấp nếp** → có lẽ giúp **chống bị enzyme tế bào phân hủy**.
- Được **RNA polymerase của tế bào chủ** sao chép liên tục trong **nhân tế bào hoặc lục lạp**.
- **RNA viroid là một ribozyme** cắt chuỗi RNA dài liên tục (sản phẩm sao chép cuộn lăn) thành các đoạn viroid.
- RNA **không mã hóa protein nào**; có thể gây bệnh bằng **làm im lặng gene (gene silencing)**.
- Chỉ gây bệnh ở **thực vật**.
"""),
("2. Virusoid (slide 37)", """
- **Một số viroid được bao trong vỏ protein** gọi là **virusoids**.
- Virusoid **chỉ gây bệnh khi tế bào đồng thời nhiễm một virus** (virus trợ giúp – helper virus cung cấp vỏ và chức năng đóng gói).
"""),
("3. Bệnh cadang-cadang và phân loại viroid (slide 38–40)", """
- **Cadang-cadang** (Philippines) – bệnh chết dừa: **Họ *Pospiviroidae***, **Chi *Cocadviroid***, **Loài Coconut cadang-cadang viroid**.

| Họ | Chi | Vật chủ |
|---|---|---|
| ***Pospiviroidae*** | *Pospiviroid* | **khoai tây** (potato spindle tuber viroid) |
| | *Hostuviroid* | **hoa bia (hop)** |
| | *Cocadviroid* | **dừa** |
| | *Apscaviroid* | **táo** |
| | *Coleviroid* | **tía tô (Coleus/perilla)** |
| ***Avsunviroidae*** | *Avsunviroid* | **bơ (avocado)** |
| | *Pelamoviroid* | **đào (peach)** |

- Tên viroid dùng hậu tố **-viroid** (chi) và **-viroidae** (họ). [mở rộng: *Pospiviroidae* sao chép trong **nhân**; *Avsunviroidae* sao chép trong **lục lạp** và có ribozyme đầu búa.]
"""),
("4. Prion (slide 41–44)", """
- **Prion là protein** (proteinaceous infectious particle) – **không có nucleic acid**.
- Gây một số **bệnh thoái hóa não** (bệnh não xốp): **bò điên (BSE)**, **Creutzfeldt–Jakob (CJD)** ở người, **scrapie** ở cừu, kuru.
- Lây qua **dụng cụ y tế nhiễm** hoặc **ăn phải mô nhiễm**.
- Tiến triển **rất chậm**, **ủ bệnh ít nhất 10 năm** (theo slide; thực tế dao động rộng).
- **Không bị phá hủy hay bất hoạt ở nhiệt độ nấu ăn thông thường**; kháng cả hấp tiệt trùng tiêu chuẩn (cần 134 °C lâu hơn, NaOH 1 N – liên hệ CTL). [mở rộng]
- Cơ chế (slide 43–44): gene chủ mã hóa protein bình thường **PrPᶜ**; protein **sai cấu dạng PrPˢᶜ** tiếp xúc và **chuyển** PrPᶜ thành PrPˢᶜ → phản ứng dây chuyền → **tích tụ, kết tụ** → chết tế bào thần kinh, não thủng lỗ như bọt biển.

| | Virus | Viroid | Virusoid | Prion |
|---|---|---|---|---|
| Nucleic acid | DNA hoặc RNA | **RNA trần 300–400 nt** | RNA | **không** |
| Vỏ protein | có | **không** | **có** | – (chính là protein) |
| Mã hóa protein | có | **không** | không | – |
| Vật chủ | mọi nhóm | **thực vật** | thực vật (cần virus trợ giúp) | động vật, người |
"""),
],
[
("Bò điên và an toàn thực phẩm", """
Dịch BSE ở Anh (1986–1990s) bắt nguồn từ việc cho bò ăn **bột xương thịt** từ gia súc nhiễm. Người ăn thịt nhiễm → **vCJD**. Từ đó nhiều nước cấm thức ăn chăn nuôi chứa protein động vật nhai lại, loại bỏ mô não tủy khi giết mổ. Dụng cụ phẫu thuật thần kinh cần quy trình khử prion đặc biệt.
"""),
],
[
("Viroids", "Short pieces of **naked RNA, 300–400 nucleotides**, no protein coat; internally paired into a closed folded 3D structure that resists cellular enzymes. Replicated by **host RNA polymerase** in the **nucleus or chloroplasts**; viroid RNA is a **ribozyme** that cuts the continuous RNA; **codes for no proteins**; may cause disease by **gene silencing**.", "RNA trần, không mã hóa protein."),
("Virusoids and viroid taxonomy", "**Virusoids**: viroids enclosed in a protein coat; cause disease **only when the cell is also infected by a virus**. **Cadang-cadang** (coconut): *Pospiviroidae*, *Cocadviroid*. *Pospiviroidae*: Pospiviroid (potato), Hostuviroid (hop), Cocadviroid (coconut), Apscaviroid (apple), Coleviroid (perilla). *Avsunviroidae*: Avsunviroid (avocado), Pelamoviroid (peach).", "Hai họ viroid."),
("Prions", "**Proteins** causing degenerative **brain diseases**; transmitted by **contaminated medical equipment** or **ingestion of infected tissue**; very slow, **incubation ≥ 10 years** (lecture); **not inactivated at normal cooking temperatures**. Misfolded PrP converts normal PrP.", "Protein gây bệnh não."),
],
["Viroids have a protein coat", "Viroids encode proteins", "Prions contain RNA", "Cooking destroys prions"])

q("VIR-04", "recall", 1, "Viroids are:",
  ["short pieces of naked RNA, 300–400 nucleotides, without a protein coat", "DNA viruses with envelopes", "misfolded host proteins", "bacteria without walls"], 0,
  "Slide 37: **RNA trần 300–400 nt, không vỏ protein**.",
  ["", "Sai.", "Prion.", "Mycoplasma."], ["viroid"], "Viroids have a protein coat", src=SRC + " slide 37")
q("VIR-04", "recall", 1, "Virusoids differ from other viroids because they:",
  ["are DNA molecules", "are enclosed in a protein coat and cause disease only when the cell is also infected by a virus", "are proteins", "replicate outside cells"], 1,
  "Slide 37: virusoid **có vỏ protein** và **chỉ gây bệnh khi có virus đồng nhiễm**.",
  ["Sai.", "", "Prion.", "Sai."], ["virusoid"], src=SRC + " slide 37")
q("VIR-04", "concept", 2, "How can viroids cause disease if they do not code for any proteins?",
  ["By producing toxins", "Possibly by gene silencing", "By forming endospores", "By lysing cells with lysozyme"], 1,
  "Slide 37: RNA viroid không mã hóa protein và **có thể gây bệnh bằng gene silencing**.",
  ["Không tạo protein.", "", "Sai.", "Sai."], ["viroid", "gene silencing"], "Viroids encode proteins", src=SRC + " slide 37")
q("VIR-04", "recall", 1, "Viroids and virusoids are replicated by:",
  ["their own RNA polymerase", "host RNA polymerase in the nucleus or chloroplasts", "reverse transcriptase", "ribosomes"], 1,
  "Slide 37: **RNA polymerase của chủ** trong **nhân hoặc lục lạp**.",
  ["Không mã hóa protein.", "", "Retrovirus.", "Sai."], ["viroid"], src=SRC + " slide 37")
q("VIR-04", "recall", 1, "Coconut cadang-cadang viroid belongs to which family and genus?",
  ["Avsunviroidae; Avsunviroid", "Pospiviroidae; Cocadviroid", "Pospiviroidae; Pospiviroid", "Herpesviridae; Simplexvirus"], 1,
  "Slide 38: **Pospiviroidae; Cocadviroid**.",
  ["Bơ.", "", "Khoai tây.", "Virus."], ["cadang-cadang"], src=SRC + " slide 38")
q("VIR-04", "recall", 1, "Which viroid genus infects avocado?",
  ["Pospiviroid", "Apscaviroid", "Avsunviroid", "Coleviroid"], 2,
  "Slide 40: **Avsunviroid** (họ Avsunviroidae) – bơ; Pelamoviroid – đào.",
  ["Khoai tây.", "Táo.", "", "Tía tô."], ["Avsunviroidae"], src=SRC + " slide 40")
q("VIR-04", "not", 2, "Which statement about prions is NOT correct according to the lecture?",
  ["They are proteins", "They cause some degenerative brain diseases", "They are destroyed at normal cooking temperatures", "They can be transmitted through contaminated medical equipment"], 2,
  "Slide 42: prion **không bị phá hủy** ở nhiệt độ nấu thông thường.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["prion"], "Cooking destroys prions", src=SRC + " slide 42")
q("VIR-04", "recall", 1, "According to the lecture, the incubation period of prion diseases is:",
  ["a few hours", "about 2 weeks", "at least 10 years", "exactly 1 year"], 2,
  "Slide 42: tấn công rất chậm, **ủ bệnh ít nhất 10 năm** (theo slide).",
  ["Sai.", "Sai.", "", "Sai."], ["prion"], src=SRC + " slide 42")
q("VIR-04", "concept", 2, "How does the viroid's structure help it survive inside the cell?",
  ["It is coated with lipids", "Internal base pairing gives a closed, folded 3D structure that resists cellular enzymes", "It forms spores", "It hides in the capsid of the host"], 1,
  "Slide 37: **bắt cặp nội phân tử → cấu trúc 3D khép kín gấp nếp** → chống enzyme.",
  ["Sai.", "", "Sai.", "Sai."], ["viroid"], pool="mock")
q("VIR-04", "concept", 2, "In the lecture, the viroid RNA acts as a ribozyme. What does it do?",
  ["It translates proteins", "It cuts the continuous RNA into viroid-length segments", "It makes DNA copies", "It forms the capsid"], 1,
  "Slide 37: ribozyme **cắt RNA liên tục thành các đoạn viroid**.",
  ["Không mã hóa protein.", "", "Sai.", "Không có capsid."], ["ribozyme"], pool="mock")
q("VIR-04", "not", 2, "Which is NOT a characteristic of prions?",
  ["Lack nucleic acid", "Cause degenerative brain disease", "Transmitted by ingestion of infected tissue", "Contain a small RNA genome of 300–400 nucleotides"], 3,
  "RNA 300–400 nt là **viroid**; prion **không có nucleic acid**.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["prion", "viroid"], "Prions contain RNA", pool="mock")
q("VIR-04", "recall", 1, "Pelamoviroid, a genus of Avsunviroidae, infects:",
  ["potatoes", "peaches", "coconuts", "apples"], 1,
  "Slide 40: **Pelamoviroid – đào**.",
  ["Pospiviroid.", "", "Cocadviroid.", "Apscaviroid."], ["Avsunviroidae"], pool="mock")

q("VIR-04", "recall", 1, "According to the lecture, prions are transmitted mainly through:",
  ["insect bites", "contaminated medical equipment or ingestion of infected tissue", "respiratory droplets from coughing", "contaminated drinking water only"], 1,
  "Slide 42: qua **dụng cụ y tế nhiễm** hoặc **ăn phải mô nhiễm**.",
  ["Sai.", "", "Sai.", "Sai."], ["prion"], pool="mock", src=SRC + " slide 42")

v("VIR-04", "viroid", "viroid", "A short naked RNA (300–400 nt) plant pathogen that codes for no protein.", "Cadang-cadang is caused by a viroid.", ["viroids"])
v("VIR-04", "virusoid", "virusoid", "A viroid-like RNA in a protein coat that needs a helper virus.", "Virusoids cause disease only with a virus.", ["virusoids"])
v("VIR-04", "ribozyme", "ribozyme (RNA xúc tác)", "An RNA molecule with catalytic activity.", "Viroid RNA is a ribozyme.")
v("VIR-04", "gene silencing", "làm im lặng gene", "Suppression of gene expression, e.g., via small RNAs.", "Viroids may cause disease by gene silencing.")
v("VIR-04", "cadang-cadang", "bệnh cadang-cadang (dừa)", "Lethal coconut disease caused by a Cocadviroid.", "Cadang-cadang occurs in the Philippines.")
v("VIR-04", "Pospiviroidae", "họ Pospiviroidae", "Viroid family: potato, hop, coconut, apple, perilla genera.", "Cocadviroid belongs to Pospiviroidae.")
v("VIR-04", "Avsunviroidae", "họ Avsunviroidae", "Viroid family: avocado and peach genera.", "Avsunviroid infects avocado.")
v("VIR-04", "prion", "prion", "An infectious protein causing degenerative brain disease.", "Prions resist cooking.", ["prions"])
v("VIR-04", "degenerative brain disease", "bệnh thoái hóa não", "Progressive destruction of brain tissue, e.g., by prions.", "BSE is a degenerative brain disease.", ["BSE", "Creutzfeldt-Jakob disease"])

fc("VIR-04", "number", "Viroid length?", "300–400 nucleotides, naked RNA.")
fc("VIR-04", "fact", "Viroid replication and pathogenesis?", "Host RNA polymerase in nucleus/chloroplast; ribozyme cuts continuous RNA; no proteins coded; gene silencing.")
fc("VIR-04", "fact", "Viroid families and genera?", "Pospiviroidae: Pospiviroid (potato), Hostuviroid (hop), Cocadviroid (coconut), Apscaviroid (apple), Coleviroid (perilla). Avsunviroidae: Avsunviroid (avocado), Pelamoviroid (peach).")
fc("VIR-04", "fact", "Prion facts (lecture)?", "Proteins; degenerative brain diseases; spread by contaminated equipment or ingesting infected tissue; incubation ≥10 years; not inactivated by normal cooking.")
fc("VIR-04", "trap", "Virusoid vs viroid?", "Virusoid has a protein coat and needs co-infection with a virus to cause disease.")
