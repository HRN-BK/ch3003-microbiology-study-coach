from _lib import *

SY = "7. Yeasts.pptx"
SM = "8. Molds.pptx"

# ---------------------------------------------------------------- FUN-01
unit("FUN-01", "Yeast cell structure (Saccharomyces cerevisiae)", "H", 2, 25, SY + ": slides 1–22",
"""Men bánh mì, men bia, men rượu vang – tất cả là **cùng một loài**: *Saccharomyces cerevisiae*. Dưới kính hiển vi nó chỉ to hơn vi khuẩn khoảng 5–10 lần, nhưng bên trong là cả một "thành phố" với **nhân, ty thể, không bào, lưới nội chất** – nó là **tế bào nhân thực** giống tế bào của bạn hơn là giống vi khuẩn.""",
("Which structure is found in a yeast cell but NOT in a bacterial cell?",
 ["Ribosomes", "Plasma membrane", "A membrane-bound nucleus with 16 chromosomes", "Cell wall"], 2,
 "Nấm men là **nhân thực**: có **nhân có màng** (S. cerevisiae đơn bội có **16 nhiễm sắc thể thẳng**), ty thể, ER, Golgi… Vi khuẩn cũng có ribosome, màng và thành."),
[
("1. Hình thái (slide 3–6)", """
- **Yeasts** (nấm men): nấm **đơn bào**, hình **cầu, bầu dục hoặc elip**, kích thước ~**3–10 μm** (to hơn vi khuẩn nhiều lần). [fig]
- Hai kiểu tiêu biểu:
  - ***Saccharomyces cerevisiae*** – sinh sản **nảy chồi (budding)**.
  - ***Schizosaccharomyces pombe*** – sinh sản **phân đôi (fission)**.
- Là **nhân thực** với đầy đủ bào quan (slide 6: sơ đồ cấu trúc tế bào *S. cerevisiae*).
"""),
("2. Thành tế bào (slide 8)", """
Chủ yếu là **polysaccharide**:
| Thành phần | Cấu tạo | Vai trò/vị trí |
|---|---|---|
| **Glucan** | D-glucose; mạch chính **β-1,3**, nhánh **β-1,6** | khung chịu lực chính (lớp trong) |
| **Mannan** | D-**mannose** (slide ghi nhầm D-glucose); mạch chính **α-1,6**, nhánh **α-1,2 và α-1,3** | lớp ngoài, gắn với protein → **mannoprotein** |
| **Chitin** | **N-acetylglucosamine**, liên kết **β-1,4** | tập trung chủ yếu ở **sẹo chồi (bud scars)** |

Thành phần khác: **mannoproteins, lipids, phosphate vô cơ**.

> So sánh: thành vi khuẩn là **peptidoglycan**; thành nấm là **glucan – mannan – chitin** → penicillin không tác dụng lên nấm.
"""),
("3. Khoang chu chất và màng sinh chất (slide 9–10)", """
**Periplasmic space** (giữa thành và màng) chứa **mannoprotein** và enzyme:
- **Invertase**: sucrose → **glucose + fructose** (nhờ đó men dùng được đường mía, rỉ đường).
- **Phosphatase**: thủy phân hợp chất chứa phosphate → giải phóng **phosphate vô cơ** để hấp thu.

**Plasma membrane**: lớp kép phospholipid + protein → **bán thấm (chọn lọc)**. Màng nấm chứa **sterol – ergosterol** (vi khuẩn thường không có sterol). Ergosterol là đích của thuốc kháng nấm (amphotericin B, azole). [mở rộng]
"""),
("4. Tế bào chất, bộ khung và nhân (slide 11–15)", """
- **Cytosol**: ion, chất hữu cơ phân tử nhỏ và trung bình, và phân tử lớn tan như **enzyme, glycogen**; chứa **ribosome 80S**, hạt lipid, phức hợp protein.
- **Cytoskeleton**: **vi ống (microtubules)** và **vi sợi (microfilaments)** → giữ **hình dạng**, ổn định cấu trúc bên trong, **di chuyển bào quan**, tham gia **phân chia tế bào**.
- **Nucleus**: màng nhân có **lỗ nhân (nuclear pores)**. Bộ gene gồm **16 nhiễm sắc thể thẳng** (DNA + protein) ở tế bào đơn bội (lưỡng bội 2n = 32).
- **DNA ngoài nhiễm sắc thể**: **DNA ty thể** và **plasmid** (plasmid 2-μm).
"""),
("5. Các bào quan (slide 16–22)", """
| Bào quan | Chức năng |
|---|---|
| **Endoplasmic reticulum (ER)** | tổng hợp protein tiết và lipid |
| **Golgi** | sửa đổi, đóng gói, phân phối protein |
| **Vacuole** (không bào) | chứa **enzyme thủy phân protein**; chứa **amino acid, polyphosphate, ion kim loại** → **điều hòa áp suất thẩm thấu** |
| **Peroxisome** | chứa **enzyme oxy hóa** (vd catalase phân hủy H₂O₂) |
| **Mitochondrion** (ty thể) | hô hấp tạo ATP (xem dưới) |

**Ty thể (slide 20–22)**:
- **Màng ngoài**: enzyme **chuyển hóa lipid**.
- **Khoang gian màng**.
- **Màng trong**: **NADH dehydrogenase, succinate dehydrogenase, ATP synthase**, protein vận chuyển.
- **Chất nền (matrix)**: enzyme **oxy hóa acid béo**, **chu trình acid citric (TCA)**; chứa **DNA ty thể** và bộ máy sao chép/phiên mã.
- **Hình dạng, kích thước, số lượng** thay đổi theo **loài, giai đoạn sinh trưởng và điều kiện dinh dưỡng**.
"""),
],
[
("Men trong đời sống Việt Nam", """
- **Bánh mì**: CO₂ do nấm men tạo làm bột nở; ethanol bay hơi khi nướng.
- **Bia, rượu vang, rượu gạo**: bánh men rượu truyền thống chứa **nấm mốc** (*Rhizopus, Mucor, Amylomyces* – đường hóa tinh bột) **và nấm men** (*Saccharomyces* – lên men rượu).
- **Men dinh dưỡng / chiết xuất nấm men**: giàu protein, vitamin nhóm B – liên hệ SCP (APP-02).
"""),
("Nấm men – \"tế bào mẫu\" của sinh học", """
*S. cerevisiae* là sinh vật nhân thực **đầu tiên được giải trình tự toàn bộ genome (1996)**, ~6.000 gene, ~12 Mb. Rất nhiều gene người có gene tương đồng ở nấm men → dùng nghiên cứu ung thư, lão hóa. Nấm men tái tổ hợp sản xuất **vaccine viêm gan B, insulin**.
"""),
],
[
("Yeast morphology", "Yeasts are **unicellular fungi**, oval to spherical, larger than bacteria. *Saccharomyces cerevisiae* reproduces by **budding**; *Schizosaccharomyces pombe* by **fission**. Yeasts are **eukaryotes** with 80S ribosomes and membrane-bound organelles.", "Nấm men: nấm đơn bào, nhân thực."),
("Yeast cell wall", "Mainly polysaccharides: **glucan** (β-1,3 backbone, β-1,6 branches), **mannan** (mannose; α-1,6 backbone, α-1,2/α-1,3 branches; forms mannoproteins), **chitin** (N-acetylglucosamine, β-1,4) mainly in **bud scars**. Also lipids and inorganic phosphate.", "Glucan – mannan – chitin, không peptidoglycan."),
("Periplasm and membrane", "The periplasmic space holds **invertase** (sucrose → glucose + fructose) and **phosphatase**. The plasma membrane is a semipermeable phospholipid bilayer with proteins and **ergosterol**.", "Invertase phân giải sucrose."),
("Nucleus and organelles", "Nucleus with nuclear pores; **16 linear chromosomes** (haploid). Extrachromosomal DNA: **mitochondrial DNA and plasmids**. ER, Golgi, **vacuole** (proteases, amino acids, polyphosphate, metal ions → osmotic regulation), **peroxisome** (oxidizing enzymes), **mitochondria** (TCA cycle, ATP synthase).", "16 NST; không bào điều hòa thẩm thấu."),
],
["Yeast walls contain peptidoglycan", "Chitin is spread evenly in the wall", "Yeast ribosomes are 70S", "Mannan is a glucose polymer"])

q("FUN-01", "recall", 1, "In the Saccharomyces cerevisiae cell wall, chitin is found mainly in:",
  ["the periplasmic space", "bud scars", "the nucleus", "the vacuole"], 1,
  "Slide 8: **chitin** (N-acetylglucosamine, β-1,4) tập trung chủ yếu ở **sẹo chồi (bud scars)**.",
  ["Khoang chu chất chứa invertase, phosphatase.", "", "Sai.", "Sai."], ["chitin", "bud scar"], "Chitin is spread evenly in the wall", src=SY + " slide 8")
q("FUN-01", "recall", 1, "Invertase in the yeast periplasmic space catalyzes:",
  ["glucose → ethanol + CO2", "sucrose → glucose + fructose", "starch → maltose", "lactose → glucose + galactose"], 1,
  "Slide 9: **invertase**: sucrose → **glucose + fructose**.",
  ["Đó là lên men ethanol (nhiều enzyme).", "", "Đó là amylase.", "Đó là β-galactosidase."], ["invertase"], src=SY + " slide 9")
q("FUN-01", "not", 2, "Which is NOT a major component of the Saccharomyces cerevisiae cell wall?",
  ["Glucan", "Mannan", "Chitin", "Peptidoglycan"], 3,
  "**Peptidoglycan** là thành phần thành **vi khuẩn**. Thành nấm men: glucan, mannan, chitin (+ mannoprotein, lipid, phosphate).",
  ["Có.", "Có.", "Có.", ""], ["glucan", "mannan", "peptidoglycan"], "Yeast walls contain peptidoglycan")
q("FUN-01", "recall", 1, "How many linear chromosomes does the haploid nucleus of Saccharomyces cerevisiae contain?",
  ["1 circular chromosome", "16", "23", "46"], 1,
  "Slide 14: bộ gene gồm **16 nhiễm sắc thể thẳng** (đơn bội; lưỡng bội 32).",
  ["Đó là vi khuẩn.", "", "Người đơn bội.", "Người lưỡng bội."], ["chromosome"], src=SY + " slide 14")
q("FUN-01", "concept", 2, "The yeast vacuole helps regulate osmotic pressure because it:",
  ["contains 70S ribosomes", "stores amino acids, polyphosphates and metal ions", "is surrounded by peptidoglycan", "produces ATP"], 1,
  "Slide 18: không bào chứa **amino acid, polyphosphate, ion kim loại** → **điều hòa áp suất thẩm thấu**; còn chứa enzyme thủy phân protein.",
  ["Sai.", "", "Sai.", "ATP do ty thể."], ["vacuole"], src=SY + " slide 18")
q("FUN-01", "recall", 1, "Where are NADH dehydrogenase, succinate dehydrogenase and ATP synthase located in the yeast mitochondrion?",
  ["Outer membrane", "Inner membrane", "Matrix", "Intermembrane space"], 1,
  "Slide 20: **màng trong** chứa NADH dehydrogenase, succinate dehydrogenase, ATP synthase, protein vận chuyển. Màng ngoài: enzyme chuyển hóa lipid; chất nền: TCA, oxy hóa acid béo, mtDNA.",
  ["Enzyme chuyển hóa lipid.", "", "TCA, mtDNA.", "Không phải."], ["mitochondrion"], src=SY + " slide 20")
q("FUN-01", "concept", 2, "Which cytoskeletal elements does the lecture describe in yeast, and what is one function?",
  ["Peptidoglycan; shape", "Microtubules and microfilaments; moving organelles and participating in cell division", "Flagella; swimming", "Pili; DNA transfer"], 1,
  "Slide 11: bộ khung gồm **vi ống và vi sợi** → giữ hình dạng, ổn định cấu trúc, **di chuyển bào quan**, tham gia **phân chia**.",
  ["Sai.", "", "Nấm men không có roi.", "Sai."], ["cytoskeleton"])
q("FUN-01", "not", 2, "Which statement about the yeast mitochondrion is NOT correct?",
  ["It contains its own DNA", "The matrix contains enzymes of the citric acid cycle", "Its shape and number are fixed regardless of growth conditions", "The inner membrane contains ATP synthase"], 2,
  "Slide 21: hình dạng, kích thước, số lượng ty thể **thay đổi theo loài, giai đoạn sinh trưởng và điều kiện dinh dưỡng**.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["mitochondrion"], pool="mock")
q("FUN-01", "recall", 1, "Which organelle contains oxidizing enzymes in the yeast cell?",
  ["Golgi body", "Peroxisome", "Vacuole", "Nucleus"], 1,
  "Slide 19: **peroxisome** chứa enzyme oxy hóa.",
  ["Golgi: đóng gói protein.", "", "Không bào: protease, dự trữ.", "Nhân: DNA."], ["peroxisome"], pool="mock")
q("FUN-01", "concept", 2, "Why does penicillin have no effect on yeasts?",
  ["Yeasts have an outer membrane", "Yeast walls are made of glucan, mannan and chitin, not peptidoglycan", "Yeasts have 70S ribosomes", "Yeasts produce invertase"], 1,
  "Penicillin nhắm **transpeptidase của peptidoglycan**; thành nấm men **không có peptidoglycan**.",
  ["Nấm men không có màng ngoài kiểu Gram âm.", "", "Nấm men có 80S.", "Không liên quan."], ["cell wall", "penicillin"], pool="mock")
q("FUN-01", "application", 2, "A yeast strain lacking invertase is grown on a medium whose only sugar is sucrose. What is expected?",
  ["Normal growth, because sucrose diffuses in freely", "Poor or no growth, because sucrose cannot be split into glucose and fructose", "Faster growth", "The strain will form endospores"], 1,
  "Không có **invertase** → không thủy phân được sucrose → thiếu nguồn carbon dùng được → sinh trưởng kém.",
  ["Sucrose cần được thủy phân trước.", "", "Sai.", "Nấm men không tạo nội bào tử."], ["invertase"], pool="mock")

v("FUN-01", "yeast", "nấm men", "A unicellular fungus.", "Saccharomyces cerevisiae is a baker's yeast.", ["yeasts"])
v("FUN-01", "budding", "nảy chồi", "Asexual reproduction by a bud that grows and separates from the mother cell.", "S. cerevisiae reproduces by budding.")
v("FUN-01", "fission", "phân đôi", "Division of one cell into two by a cross wall.", "Schizosaccharomyces pombe divides by fission.")
v("FUN-01", "glucan", "glucan", "A glucose polymer (β-1,3 with β-1,6 branches) forming the main yeast wall.", "Glucan gives the yeast wall strength.")
v("FUN-01", "mannan", "mannan", "A mannose polymer linked to proteins (mannoproteins) in the outer yeast wall.", "Mannan forms mannoproteins.", ["mannoprotein", "mannoproteins"])
v("FUN-01", "chitin", "chitin", "A polymer of N-acetylglucosamine (β-1,4); in yeast mainly in bud scars; main wall component of molds.", "Chitin is concentrated in bud scars.")
v("FUN-01", "bud scar", "sẹo chồi", "A chitin-rich ring left on the mother cell after a bud separates.", "Old cells have many bud scars.", ["bud scars"])
v("FUN-01", "invertase", "invertase", "Enzyme that splits sucrose into glucose and fructose.", "Invertase lies in the periplasmic space.")
v("FUN-01", "ergosterol", "ergosterol", "The main sterol of fungal membranes.", "Antifungal drugs target ergosterol.")
v("FUN-01", "vacuole", "không bào", "Organelle storing enzymes, amino acids, polyphosphate and ions; regulates osmotic pressure.", "The yeast vacuole contains proteases.")
v("FUN-01", "peroxisome", "peroxisome", "Organelle containing oxidizing enzymes.", "Peroxisomes break down hydrogen peroxide.")
v("FUN-01", "mitochondrion", "ty thể", "Organelle of respiration with its own DNA.", "The citric acid cycle occurs in the mitochondrion.", ["mitochondria"])
v("FUN-01", "cytoskeleton", "bộ khung tế bào", "Network of microtubules and microfilaments.", "The cytoskeleton moves organelles.")

fc("FUN-01", "fact", "Three polysaccharides of the yeast wall?", "Glucan (β-1,3/β-1,6), mannan (α-1,6 with α-1,2/α-1,3), chitin (β-1,4, bud scars).")
fc("FUN-01", "fact", "Two periplasmic enzymes of yeast?", "Invertase (sucrose → glucose + fructose) and phosphatase.")
fc("FUN-01", "number", "Chromosome number of haploid S. cerevisiae?", "16 linear chromosomes.")
fc("FUN-01", "fact", "Mitochondrial inner membrane enzymes (lecture)?", "NADH dehydrogenase, succinate dehydrogenase, ATP synthase.")
fc("FUN-01", "trap", "TRUE/FALSE: yeast ribosomes are 70S like bacteria.", "FALSE – cytoplasmic yeast ribosomes are 80S.")

# ---------------------------------------------------------------- FUN-02
unit("FUN-02", "Yeast metabolism and reproduction", "H", 2, 25, SY + ": slides 23–36",
"""Nhà máy bia sục khí cho nấm men lúc đầu để chúng **sinh sôi**, rồi **đậy kín** để chúng **tạo cồn**. Cùng một tế bào, hai "chế độ" khác nhau: có oxy thì **hô hấp** (nhiều ATP, nhiều tế bào), thiếu oxy thì **lên men** (ít ATP, nhiều ethanol). Đó là vì *S. cerevisiae* là sinh vật **kỵ khí tùy nghi**.""",
("Why do brewers first aerate the wort and then keep the fermenter closed?",
 ["Oxygen kills contaminating bacteria", "With oxygen yeast respires and multiplies; without oxygen it ferments sugar to ethanol", "Oxygen is needed to produce ethanol", "Closing the tank raises the temperature"], 1,
 "*S. cerevisiae* là **facultative anaerobe**: có O₂ → hô hấp, sinh khối tăng; thiếu O₂ → lên men tạo **ethanol + CO₂**."),
[
("1. Kiểu trao đổi chất", """
- *S. cerevisiae* là **dị dưỡng hóa năng (chemoheterotroph)** và **kỵ khí tùy nghi (facultative anaerobe)** (slide 23).
- **Hô hấp hiếu khí**: glucose → pyruvate (đường phân) → acetyl-CoA → **chu trình acid citric** trong ty thể → chuỗi truyền electron → nhiều ATP.
- **Lên men ethanol** (khi thiếu O₂ hoặc thừa đường): glucose → 2 pyruvate → 2 acetaldehyde + 2 CO₂ → **2 ethanol**; tái tạo NAD⁺, chỉ **2 ATP/glucose** từ đường phân.
  - Phương trình: **C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂**.
- Ở nồng độ glucose cao, *S. cerevisiae* vẫn lên men ngay cả khi có O₂ (**hiệu ứng Crabtree**). [mở rộng]
"""),
("2. Chu trình acid citric – con số cần nhớ (slide 23)", """
Slide: **mỗi 2 phân tử acetyl-CoA (CH₃-CO-CoA)** đi vào chu trình tạo:
| Sản phẩm | Số lượng |
|---|---|
| CO₂ | **4** |
| NADH | **6** |
| FADH₂ | **2** |
| ATP (GTP) | **2** |

→ Mỗi acetyl-CoA: 2 CO₂, 3 NADH, 1 FADH₂, 1 ATP. (Một glucose tạo 2 acetyl-CoA.)
- Oxy hóa pyruvate → acetyl-CoA là bước **riêng**, tạo thêm 1 NADH + 1 CO₂ mỗi pyruvate – đừng cộng lẫn.
"""),
("3. Sinh sản vô tính – nảy chồi và phân đôi (slide 29–31)", """
- **Nảy chồi (budding)** ở *S. cerevisiae*: một chồi nhỏ nhú ra trên tế bào mẹ → nhân **nguyên phân (mitosis)** → một nhân đi vào chồi → chồi lớn lên → vách ngăn (chitin) tách chồi → để lại **sẹo chồi** trên tế bào mẹ.
- **Cả tế bào đơn bội (n) và lưỡng bội (2n)** đều nảy chồi được (slide 29: *haploid and diploid cells: mitosis (budding)*).
- **Phân đôi (fission)** ở *Schizosaccharomyces pombe*: tế bào dài ra rồi chia đôi bằng vách ngăn, giống vi khuẩn.
- Chồi không tách hẳn, xếp thành chuỗi → **giả sợi (pseudohyphae)** – ví dụ *Candida albicans*. [fig]
"""),
("4. Sinh sản hữu tính – giao phối và bào tử túi (slide 31–36)", """
**Chu trình sống của *S. cerevisiae*** [fig]:
1. Hai tế bào đơn bội khác **kiểu giao phối (mating type)** – **α** và **a** – kết hợp → **hợp tử (zygote) lưỡng bội 2n**.
2. Tế bào lưỡng bội có thể **nảy chồi** nhiều thế hệ (pha lưỡng bội).
3. Khi **thiếu dinh dưỡng** (đói nitơ), tế bào 2n **giảm phân (meiosis)** → **4 bào tử đơn bội (ascospores)** nằm trong **túi (ascus)**.
4. Bào tử nảy mầm → tế bào đơn bội α hoặc a → nảy chồi (pha đơn bội) → lại giao phối.

Công thức rút gọn (slide): **Haploid α + haploid a → zygote → meiosis → haploid spores**.

> Nhớ: **n = 16** (đơn bội) → **2n = 32** (lưỡng bội). Sau giảm phân I nhân đã là **n** (nhiễm sắc thể còn kép) – slide 32 ghi "2n" là nhầm.
"""),
("5. So sánh hai kiểu sinh sản", """
| | Vô tính | Hữu tính |
|---|---|---|
| Cơ chế | **nguyên phân** | **hợp giao + giảm phân** |
| Hình thức | nảy chồi / phân đôi | giao phối α × a → ascus 4 bào tử |
| Bội thể con | giống mẹ (n → n; 2n → 2n) | bào tử **n** |
| Biến dị di truyền | thấp | **cao** (tái tổ hợp) |
| Điều kiện | đủ dinh dưỡng | thường khi **đói** |
"""),
],
[
("Công nghiệp: điều khiển \"chế độ\" nấm men", """
- **Sản xuất men bánh mì (sinh khối)**: nuôi **fed-batch**, cấp đường từ từ và **sục khí mạnh** → tránh hiệu ứng Crabtree, tối đa sinh khối.
- **Sản xuất ethanol/bia**: yếm khí, đường cao → tối đa ethanol (APP-03).
- Nồng độ ethanol thường ức chế nấm men ở ~13–15 % (slide 28 nêu 13 %), chủng chịu cồn tốt có thể cao hơn.
"""),
("Di truyền học nấm men", """
Vì có pha đơn bội ổn định, đột biến lặn ở nấm men **biểu hiện ngay** – tiện cho nghiên cứu gene. Phân tích 4 bào tử trong một túi (**tetrad analysis**) cho phép lập bản đồ gene trực tiếp.
"""),
],
[
("Yeast metabolism", "*S. cerevisiae* is a **facultative anaerobe**. With O₂ it respires (glycolysis → acetyl-CoA → **citric acid cycle** → electron transport). Without O₂ (or with excess sugar) it **ferments**: C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂, net 2 ATP.", "Kỵ khí tùy nghi: hô hấp hoặc lên men."),
("Citric acid cycle numbers", "Every **two acetyl-CoA** entering the cycle produce **4 CO₂, 6 NADH, 2 FADH₂ and 2 ATP**.", "2 acetyl-CoA → 4 CO₂, 6 NADH, 2 FADH₂, 2 ATP."),
("Asexual reproduction", "**Budding** (*S. cerevisiae*): mitosis, bud grows and separates, leaving a **bud scar**; both haploid and diploid cells bud. **Fission** (*S. pombe*). Buds that stay attached form **pseudohyphae**.", "Nảy chồi – nguyên phân."),
("Sexual reproduction", "Haploid **α** + haploid **a** → diploid **zygote**; diploid cells can bud; under starvation they undergo **meiosis** → **4 haploid ascospores** in an **ascus**.", "α + a → 2n → giảm phân → 4 bào tử túi."),
],
["Only haploid cells can bud", "Budding uses meiosis", "Fermentation gives more ATP than respiration", "Ascus contains 8 spores in S. cerevisiae"])

q("FUN-02", "calc", 2, "According to the lecture, how many NADH molecules are produced when TWO acetyl-CoA molecules pass through the citric acid cycle?",
  ["3", "6", "4", "2"], 1,
  "Slide 23: 2 acetyl-CoA → **4 CO₂, 6 NADH, 2 FADH₂, 2 ATP**.",
  ["Đó là cho 1 acetyl-CoA.", "", "Đó là số CO₂.", "Đó là số FADH₂ hoặc ATP."], ["citric acid cycle"], src=SY + " slide 23", steps=["Mỗi acetyl-CoA tạo 3 NADH", "2 × 3 = 6 NADH"])
q("FUN-02", "recall", 1, "Saccharomyces cerevisiae is best described as a:",
  ["obligate aerobe", "obligate anaerobe", "facultative anaerobe", "photoautotroph"], 2,
  "Slide 23: *S. cerevisiae* là **facultative anaerobe** – hô hấp khi có O₂, lên men khi không có.",
  ["Nó sống được không có O₂.", "Nó dùng O₂ khi có.", "", "Nấm là dị dưỡng."], ["facultative anaerobe"], src=SY + " slide 23")
q("FUN-02", "concept", 2, "Which statement about budding in S. cerevisiae is correct?",
  ["Only haploid cells can bud", "Budding involves meiosis", "Both haploid and diploid cells can reproduce by budding through mitosis", "Budding produces four ascospores"], 2,
  "Slide 29: **tế bào đơn bội và lưỡng bội** đều **nảy chồi bằng nguyên phân**.",
  ["Sai.", "Nảy chồi là nguyên phân.", "", "Ascospore là sinh sản hữu tính."], ["budding"], "Only haploid cells can bud", src=SY + " slide 29")
q("FUN-02", "concept", 2, "In the S. cerevisiae life cycle, what is the product of mating between a haploid α cell and a haploid a cell?",
  ["Four ascospores", "A diploid zygote", "A haploid bud", "A pseudohypha"], 1,
  "α + a → **hợp tử lưỡng bội (2n)**. Sau đó (khi đói) mới giảm phân tạo 4 bào tử túi.",
  ["Đó là sau giảm phân.", "", "Sai.", "Sai."], ["mating type", "zygote"])
q("FUN-02", "recall", 1, "A yeast that divides by fission, like bacteria, is:",
  ["Saccharomyces cerevisiae", "Schizosaccharomyces pombe", "Candida albicans", "Cryptococcus neoformans"], 1,
  "***Schizosaccharomyces pombe*** – phân đôi. *S. cerevisiae* – nảy chồi.",
  ["Nảy chồi.", "", "Nảy chồi, tạo giả sợi.", "Nảy chồi."], ["fission"], src=SY + " slide 30")
q("FUN-02", "calc", 2, "In ethanol fermentation, how many moles of ethanol and CO2 are produced from 1 mole of glucose (ideal equation)?",
  ["1 ethanol + 1 CO2", "2 ethanol + 2 CO2", "2 ethanol + 6 CO2", "3 ethanol + 3 CO2"], 1,
  "C₆H₁₂O₆ → **2 C₂H₅OH + 2 CO₂** (cân bằng: 6 C = 2×2 + 2×1).",
  ["Không cân bằng carbon.", "", "6 CO₂ là hô hấp hoàn toàn.", "Không cân bằng."], ["fermentation"], steps=["C bên trái = 6", "2 ethanol (4 C) + 2 CO₂ (2 C) = 6 C"])
q("FUN-02", "concept", 2, "Why does yeast grow (increase in biomass) much more under aerobic conditions than during fermentation?",
  ["Oxygen is a nutrient that becomes cell mass", "Respiration yields much more ATP per glucose than fermentation (2 ATP)", "Fermentation kills the cells", "Ethanol is used as a building block"], 1,
  "Hô hấp tạo **nhiều ATP** hơn nhiều so với **2 ATP** của lên men → nhiều năng lượng cho sinh tổng hợp → sinh khối cao.",
  ["Sai.", "", "Sai.", "Sai."], ["respiration", "fermentation"], "Fermentation gives more ATP than respiration")
q("FUN-02", "not", 2, "Which statement about sexual reproduction of S. cerevisiae is NOT correct?",
  ["It involves haploid cells of mating types a and α", "The diploid undergoes meiosis to form haploid spores", "The spores are enclosed in an ascus", "It is achieved by budding of haploid cells"], 3,
  "Nảy chồi là **vô tính**. Hữu tính = giao phối α × a + giảm phân tạo bào tử túi.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["ascus", "meiosis"], "Budding uses meiosis", pool="mock")
q("FUN-02", "recall", 1, "Meiosis of a diploid S. cerevisiae cell typically produces how many ascospores per ascus?",
  ["2", "4", "8", "16"], 1,
  "Một lần giảm phân → **4 bào tử túi đơn bội** trong một ascus (ở nấm mốc Ascomycota thường là 8 do thêm một lần nguyên phân).",
  ["Sai.", "", "Thường gặp ở nấm mốc túi (Neurospora).", "Sai."], ["ascospore"], "Ascus contains 8 spores in S. cerevisiae", pool="mock")
q("FUN-02", "calc", 2, "Two acetyl-CoA molecules enter the citric acid cycle. How many CO2 molecules are released by the cycle?",
  ["2", "4", "6", "3"], 1,
  "Slide 23: 2 acetyl-CoA → **4 CO₂** (2 mỗi vòng).",
  ["Đó là cho 1 acetyl-CoA.", "", "Nhầm với số NADH.", "Sai."], ["citric acid cycle"], pool="mock", steps=["1 acetyl-CoA → 2 CO₂", "2 × 2 = 4"])
q("FUN-02", "application", 2, "Chains of elongated yeast buds that remain attached look like hyphae. These are called:",
  ["true hyphae", "pseudohyphae", "mycelia", "conidiophores"], 1,
  "Chồi không tách tạo chuỗi = **giả sợi (pseudohyphae)**, ví dụ *Candida albicans*.",
  ["Sợi thật là của nấm mốc.", "", "Hệ sợi nấm mốc.", "Cuống bào tử đính."], ["pseudohyphae"], pool="mock")

v("FUN-02", "facultative anaerobe", "kỵ khí tùy nghi", "An organism that uses O2 when present but can grow without it by fermentation.", "S. cerevisiae is a facultative anaerobe.", ["facultative anaerobes"])
v("FUN-02", "respiration", "hô hấp", "ATP production using an electron transport chain and a final electron acceptor.", "Aerobic respiration uses O2.", ["aerobic respiration"])
v("FUN-02", "citric acid cycle", "chu trình acid citric (Krebs)", "Mitochondrial cycle oxidizing acetyl-CoA to CO2 and producing NADH and FADH2.", "Two acetyl-CoA give 6 NADH in the citric acid cycle.", ["Krebs cycle", "TCA cycle"])
v("FUN-02", "acetyl-CoA", "acetyl-CoA", "A two-carbon acetyl group carried by coenzyme A; fuel of the citric acid cycle.", "Pyruvate is converted to acetyl-CoA.")
v("FUN-02", "mating type", "kiểu giao phối", "Genetically determined compatibility class (a or α) of haploid yeast cells.", "Cells of opposite mating type fuse.", ["mating types"])
v("FUN-02", "zygote", "hợp tử", "Diploid cell formed by fusion of two haploid cells.", "The yeast zygote is diploid.")
v("FUN-02", "meiosis", "giảm phân", "Division that halves the chromosome number, producing haploid cells.", "Meiosis forms four ascospores.")
v("FUN-02", "mitosis", "nguyên phân", "Nuclear division that keeps the chromosome number.", "Budding involves mitosis.")
v("FUN-02", "ascus", "túi bào tử (nang)", "A sac in which ascospores form.", "Each ascus holds four yeast ascospores.", ["asci"])
v("FUN-02", "ascospore", "bào tử túi (bào tử nang)", "A sexual spore formed inside an ascus.", "Ascospores are haploid.", ["ascospores"])
v("FUN-02", "haploid", "đơn bội", "Having one set of chromosomes (n).", "Haploid yeast has 16 chromosomes.", ["diploid"])
v("FUN-02", "pseudohyphae", "giả sợi", "Chains of elongated buds that remain attached.", "Candida albicans forms pseudohyphae.", ["pseudohypha"])

fc("FUN-02", "number", "2 acetyl-CoA through the citric acid cycle give?", "4 CO2, 6 NADH, 2 FADH2, 2 ATP.")
fc("FUN-02", "fact", "Ethanol fermentation equation?", "C6H12O6 → 2 C2H5OH + 2 CO2 (net 2 ATP from glycolysis).")
fc("FUN-02", "fact", "S. cerevisiae life cycle in one line?", "Haploid α + haploid a → diploid zygote (buds) → meiosis → 4 haploid ascospores in an ascus.")
fc("FUN-02", "fact", "Budding vs fission yeasts?", "Saccharomyces cerevisiae buds; Schizosaccharomyces pombe divides by fission.")
fc("FUN-02", "trap", "TRUE/FALSE: only haploid yeast cells can bud.", "FALSE – both haploid and diploid cells bud by mitosis.")

# ---------------------------------------------------------------- FUN-03
unit("FUN-03", "Yeast vs bacteria; yeast classification and counting", "H", 2, 20, SY + ": slides 37–48",
"""Phòng QC nhà máy bia cần biết **mật độ nấm men sống** trước khi cấy vào thùng lên men. Cách nhanh: đếm trên **buồng đếm hồng cầu** trong 10 phút. Cách chắc: **cấy đĩa đếm khuẩn lạc** nhưng chờ 2–3 ngày. Mỗi cách trả lời một câu hỏi khác nhau – và cách thứ nhất có thể **đếm nhầm cả tế bào chết**.""",
("A direct count with a counting chamber gives a higher number than a plate count of the same yeast suspension. The most likely reason is:",
 ["The plate count includes dead cells", "The chamber counts both live and dead cells, while only viable cells form colonies", "Yeasts cannot grow on agar", "The chamber has a smaller volume"], 1,
 "Buồng đếm đếm **mọi tế bào nhìn thấy** (sống + chết); đếm đĩa chỉ đếm tế bào **có khả năng tạo khuẩn lạc** (CFU)."),
[
("1. Nấm men vs vi khuẩn (slide 37)", """
| Đặc điểm | **Nấm men** | **Vi khuẩn (Eubacteria)** |
|---|---|---|
| Kiểu tế bào | **nhân thực**: có nhân, bào quan có màng, bộ khung tế bào; ribosome **80S** | **nhân sơ**: không nhân, không bào quan có màng và bộ khung (theo slide); ribosome **70S** |
| Màng sinh chất | có **sterol** (ergosterol) | **không sterol**, trừ *Mycoplasma* |
| Thành tế bào | **glucan, mannan, chitin** | **peptidoglycan** |
| Bào tử | cấu trúc **sinh sản** vô tính và hữu tính | **nội bào tử** (không để sinh sản) nhưng có thể thành tế bào sinh dưỡng |
| Trao đổi chất | **dị dưỡng**; **kỵ khí tùy nghi** | dị dưỡng **hoặc tự dưỡng**; **hiếu khí, kỵ khí tùy nghi, kỵ khí** |
| Kích thước | ~3–10 μm | ~0,5–5 μm |
| Kháng sinh nhạy | kháng penicillin; nhạy thuốc kháng nấm | nhạy penicillin, streptomycin… |

> Slide nói vi khuẩn "không có cytoskeleton" – đây là khái quát cũ; vi khuẩn có protein tương đồng (FtsZ, MreB) nhưng không có vi ống/vi sợi điển hình.
"""),
("2. Phân loại nấm men (slide 38–40)", """
"Nấm men" là **dạng sinh trưởng đơn bào**, không phải một ngành. Nấm men thuộc nhiều nhóm:
| Nhóm | Bào tử hữu tính | Ví dụ |
|---|---|---|
| **Ascomycetes** (nấm túi) | **ascospore** trong ascus | *Saccharomyces, Schizosaccharomyces, Pichia, Kluyveromyces* |
| **Basidiomycetes** (nấm đảm) | **basidiospore** | *Cryptococcus, Rhodotorula* |
| **Deuteromycetes** (nấm bất toàn – chưa thấy giai đoạn hữu tính) | không biết | *Candida* (nay xếp vào Ascomycota) |

Các tiêu chí phân loại truyền thống: hình thái tế bào, kiểu sinh sản (chồi, phân đôi), bào tử hữu tính, khả năng lên men/đồng hóa các loại đường, sử dụng nitrate…; hiện nay dùng trình tự **ITS, 26S/18S rDNA** (IDT-02).
"""),
("3. Định lượng nấm men – buồng đếm (slide 41–43)", """
**Buồng đếm hồng cầu (hemocytometer / Thoma / Neubauer)**:
- Buồng có lưới ô với **diện tích và chiều sâu biết trước** → biết **thể tích** mẫu trong ô.
- Ví dụ buồng Neubauer: ô lớn trung tâm 1 mm × 1 mm, sâu **0,1 mm** → V = 0,1 mm³ = **10⁻⁴ mL** (chia 25 ô trung bình × 16 ô nhỏ = 400 ô nhỏ).
- **Mật độ (tế bào/mL) = (số tế bào đếm được / thể tích đã đếm, mL) × hệ số pha loãng**.
- Ví dụ: đếm 120 tế bào trong 1 mm² (10⁻⁴ mL), mẫu pha loãng 10 lần → 120 × 10 / 10⁻⁴ = **1,2 × 10⁷ tế bào/mL**.
- Nhuộm **xanh methylene (methylene blue)**: tế bào **chết bắt màu xanh**, tế bào sống khử màu → **không màu** → đếm được tỉ lệ sống.
- Quy tắc: chồi lớn hơn ½ tế bào mẹ đếm là 1 tế bào riêng; đếm tế bào chạm cạnh trên và trái, bỏ cạnh dưới và phải. [mở rộng]
"""),
("4. Định lượng – đếm khuẩn lạc trên đĩa", """
- Pha loãng liên tiếp → cấy trải (spread) hoặc đổ đĩa (pour) → ủ 2–3 ngày (nấm men 28–30 °C) → đếm khuẩn lạc (30–300).
- **CFU/mL = số khuẩn lạc / (thể tích cấy × độ pha loãng)**.
- Chỉ **tế bào sống có khả năng phân chia** mới tạo khuẩn lạc.
"""),
("5. So sánh hai phương pháp (slide 44–48: \"Time & materials\", \"Dead cells\")", """
| Tiêu chí | **Buồng đếm** | **Đếm khuẩn lạc trên đĩa** |
|---|---|---|
| **Thời gian** | **nhanh** (vài phút) | **chậm** (2–3 ngày ủ) |
| **Vật tư** | ít: buồng đếm, kính hiển vi | nhiều: môi trường, đĩa, ống pha loãng, tủ ấm |
| **Tế bào chết** | **đếm cả tế bào chết** (trừ khi nhuộm methylene blue) | **chỉ đếm tế bào sống** |
| Mật độ tối thiểu | cần mẫu đặc (≥ ~10⁶ tế bào/mL) | phát hiện được mật độ thấp |
| Cụm tế bào | đếm được từng tế bào | 1 cụm = 1 CFU → có thể thấp hơn thực tế |
| Nhiễm tạp | khó phân biệt | quan sát được khuẩn lạc lạ |

→ Buồng đếm: **nhanh, rẻ**, nhưng **không phân biệt sống/chết**. Đếm đĩa: **chính xác số tế bào sống**, nhưng **tốn thời gian, vật tư**.
"""),
],
[
("Thực tế: kiểm soát men giống trong nhà máy bia", """
Nhà máy bia thường cấy khoảng **10–20 × 10⁶ tế bào/mL** dịch đường và yêu cầu tỉ lệ sống **> 90 %** (nhuộm methylene blue). Tỉ lệ sống thấp → lên men chậm, bia có mùi lạ. Máy đếm tế bào tự động hiện đại dùng nguyên lý nhuộm huỳnh quang + phân tích ảnh – vẫn là "buồng đếm" nâng cấp.
"""),
("Candida – nấm men gây bệnh", """
*Candida albicans* (thường trú ở miệng, ruột, âm đạo) có thể gây **nấm miệng, nấm âm đạo**, nhiễm trùng máu ở người suy giảm miễn dịch; chuyển từ dạng men sang **giả sợi/sợi** khi xâm lấn mô. *Cryptococcus neoformans* (có vỏ nhầy) gây viêm màng não.
"""),
],
[
("Yeast vs bacteria", "Yeast: eukaryotic, nucleus, organelles, 80S ribosomes; **sterol** in membrane; wall of **glucan, mannan, chitin**; spores are **reproductive**; heterotroph, facultative anaerobe. Bacteria: prokaryotic, 70S; no sterol (except *Mycoplasma*); **peptidoglycan**; **endospores** are not for reproduction; heterotroph or autotroph; aerobic/facultative/anaerobic.", "Bảng so sánh nấm men – vi khuẩn."),
("Counting chamber", "Cells counted in a grid of known area and depth (e.g., 1 mm² × 0.1 mm = 10⁻⁴ mL). Cells/mL = count ÷ volume (mL) × dilution factor. **Methylene blue** stains dead cells blue; live cells stay colorless.", "Buồng đếm: nhanh, đếm cả tế bào chết."),
("Chamber vs plate count", "Chamber: fast, few materials, but counts **dead cells** too and needs dense samples. Plate count: counts only **viable** cells (CFU) and detects low numbers, but needs **2–3 days** and more materials.", "So sánh thời gian, vật tư, tế bào chết."),
],
["Chamber counts only live cells", "Yeast is a phylum", "Endospores reproduce bacteria"])

q("FUN-03", "not", 2, "Which comparison between yeasts and bacteria is NOT correct?",
  ["Yeasts have 80S ribosomes; bacteria have 70S", "Yeast membranes contain sterols; most bacterial membranes do not", "Yeast walls contain peptidoglycan; bacterial walls contain chitin", "Yeast spores are reproductive; bacterial endospores are not"], 2,
  "Ngược lại: thành **nấm men** là glucan–mannan–chitin; thành **vi khuẩn** là **peptidoglycan**.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["peptidoglycan", "chitin"], src=SY + " slide 37")
q("FUN-03", "concept", 2, "What is the main disadvantage of counting yeast cells with a red-blood-cell counting chamber compared with plate counts?",
  ["It takes 2–3 days", "It counts dead cells as well as live cells unless a viability stain is used", "It requires large amounts of media", "It cannot count cells at high density"], 1,
  "Buồng đếm **đếm cả tế bào chết**; muốn phân biệt phải nhuộm **methylene blue**. Nó lại **nhanh** và **ít vật tư**.",
  ["Đó là nhược điểm của đếm đĩa.", "", "Đó là nhược điểm của đếm đĩa.", "Ngược lại, nó cần mật độ cao."], ["counting chamber", "plate count"], "Chamber counts only live cells", src=SY + " slides 44–48")
q("FUN-03", "calc", 2, "A yeast suspension diluted 10-fold is placed in a counting chamber. 150 cells are counted in a volume of 10⁻⁴ mL. What is the cell concentration of the original suspension?",
  ["1.5 × 10⁶ cells/mL", "1.5 × 10⁷ cells/mL", "1.5 × 10⁵ cells/mL", "1.5 × 10⁸ cells/mL"], 1,
  "C = 150 / 10⁻⁴ × 10 = 1,5 × 10⁶ × 10 = **1,5 × 10⁷ tế bào/mL**.",
  ["Quên nhân hệ số pha loãng 10.", "", "Chia thay vì nhân hệ số pha loãng.", "Nhân thừa một bậc 10."], ["counting chamber", "dilution factor"],
  steps=["C = N / V × D", "150 / 10⁻⁴ = 1,5 × 10⁶", "× 10 = 1,5 × 10⁷ tế bào/mL"])
q("FUN-03", "recall", 1, "In a methylene blue viability test of yeast, dead cells appear:",
  ["colorless", "blue", "red", "green"], 1,
  "Tế bào **sống khử** methylene blue → không màu; tế bào **chết** không khử được → **xanh**.",
  ["Đó là tế bào sống.", "", "Sai.", "Sai."], ["methylene blue"])
q("FUN-03", "concept", 2, "\"Yeast\" is best described as:",
  ["a single phylum of fungi", "a unicellular growth form found in several fungal groups (e.g., ascomycetes and basidiomycetes)", "a type of bacterium", "a protist"], 1,
  "Nấm men là **dạng sinh trưởng đơn bào**, có trong nhiều nhóm (Ascomycetes: *Saccharomyces*; Basidiomycetes: *Cryptococcus*).",
  ["Không phải một ngành.", "", "Nấm men là nấm nhân thực.", "Không phải nguyên sinh vật."], ["yeast"], "Yeast is a phylum")
q("FUN-03", "calc", 2, "0.1 mL of a 10⁻⁵ dilution of a yeast culture is spread on a plate and gives 64 colonies. What is the viable count of the original culture?",
  ["6.4 × 10⁶ CFU/mL", "6.4 × 10⁷ CFU/mL", "6.4 × 10⁵ CFU/mL", "6.4 × 10⁸ CFU/mL"], 1,
  "CFU/mL = 64 / (0,1 × 10⁻⁵) = 64 × 10⁶ = **6,4 × 10⁷ CFU/mL**.",
  ["Quên chia cho 0,1 mL.", "", "Sai hai bậc.", "Nhân thừa một bậc."], ["CFU", "plate count"],
  steps=["CFU/mL = số khuẩn lạc / (V × d)", "V × d = 0,1 × 10⁻⁵ = 10⁻⁶", "64 / 10⁻⁶ = 6,4 × 10⁷"])
q("FUN-03", "not", 2, "Which is NOT an advantage of the plate count method over the counting chamber?",
  ["It counts only viable cells", "It can detect low cell numbers", "It gives results within minutes", "Contaminants can be seen as different colonies"], 2,
  "Đếm đĩa cần **2–3 ngày ủ** – đó là **nhược điểm**. Buồng đếm mới cho kết quả trong vài phút.",
  ["Ưu điểm.", "Ưu điểm.", "", "Ưu điểm."], ["plate count"], pool="mock")
q("FUN-03", "recall", 1, "Which metabolic description applies to yeasts according to the yeast–bacteria comparison table?",
  ["Autotrophic and strictly anaerobic", "Heterotrophic and facultatively anaerobic", "Photoautotrophic", "Chemoautotrophic and aerobic"], 1,
  "Bảng slide 37: nấm men **dị dưỡng, kỵ khí tùy nghi**; vi khuẩn đa dạng hơn (tự dưỡng/dị dưỡng; hiếu khí/kỵ khí).",
  ["Sai.", "", "Sai.", "Sai."], ["facultative anaerobe"], pool="mock", src=SY + " slide 37")
q("FUN-03", "application", 3, "A counting chamber gives 2.0 × 10⁸ cells/mL, of which 25% stain blue with methylene blue. What is the estimated concentration of LIVE cells?",
  ["5.0 × 10⁷ cells/mL", "1.5 × 10⁸ cells/mL", "2.0 × 10⁸ cells/mL", "2.5 × 10⁷ cells/mL"], 1,
  "25 % bắt màu xanh = **chết** → sống 75 %: 2,0 × 10⁸ × 0,75 = **1,5 × 10⁸ tế bào/mL**.",
  ["Đó là số tế bào chết.", "", "Đó là tổng số.", "Sai."], ["methylene blue"], pool="mock",
  steps=["Tế bào xanh = chết = 25 %", "Sống = 75 %", "2,0 × 10⁸ × 0,75 = 1,5 × 10⁸"])
q("FUN-03", "recall", 1, "Cryptococcus is an example of a yeast belonging to:",
  ["Ascomycetes", "Basidiomycetes", "Bacteria", "Protists"], 1,
  "*Cryptococcus* là nấm men thuộc **Basidiomycetes**; *Saccharomyces* thuộc Ascomycetes.",
  ["Saccharomyces.", "", "Sai.", "Sai."], ["basidiomycetes"], pool="mock")

v("FUN-03", "counting chamber", "buồng đếm (hồng cầu)", "A slide with a grid of known area and depth for direct cell counts.", "A counting chamber gives results in minutes.", ["hemocytometer", "haemocytometer", "Neubauer chamber"])
v("FUN-03", "plate count", "phương pháp đếm khuẩn lạc trên đĩa", "Counting colonies from diluted samples to estimate viable cells.", "The plate count takes two days.", ["plate counts"])
v("FUN-03", "CFU", "đơn vị hình thành khuẩn lạc", "Colony-forming unit: a cell or clump that forms one colony.", "Results are reported as CFU/mL.", ["colony-forming unit", "colony-forming units"])
v("FUN-03", "methylene blue", "xanh methylene", "A dye reduced (decolorized) by live yeast; dead cells stay blue.", "Dead cells stain with methylene blue.")
v("FUN-03", "viable", "còn sống (có khả năng sinh trưởng)", "Able to grow and reproduce.", "Only viable cells form colonies.", ["viability"])
v("FUN-03", "dilution factor", "hệ số pha loãng", "How many times a sample was diluted (D = 1/d).", "Multiply the count by the dilution factor.", ["dilution"])
v("FUN-03", "basidiomycetes", "nấm đảm", "Fungi producing basidiospores on basidia.", "Cryptococcus is a basidiomycete yeast.", ["Basidiomycota"])
v("FUN-03", "ascomycetes", "nấm túi (nấm nang)", "Fungi producing ascospores in asci.", "Saccharomyces is an ascomycete.", ["Ascomycota"])

fc("FUN-03", "fact", "Chamber vs plate count – 2 slide keywords?", "Time & materials (chamber fast, cheap) and dead cells (chamber counts them; plates count viable only).")
fc("FUN-03", "number", "Volume over 1 mm² of a 0.1 mm deep chamber?", "0.1 mm³ = 10⁻⁴ mL.")
fc("FUN-03", "fact", "Yeast spores vs bacterial endospores?", "Yeast spores: reproductive (sexual/asexual). Endospores: survival only.")
fc("FUN-03", "fact", "Methylene blue result?", "Live cells colorless (reduce the dye); dead cells blue.")

# ---------------------------------------------------------------- FUN-04
unit("FUN-04", "Mold structure: hyphae, septa and mycelium", "H", 1, 20, SM + ": slides 1–14",
"""Ổ bánh mì để lâu nổi một lớp **bông trắng**, vài ngày sau chuyển **đen**. Lớp bông đó là **hệ sợi nấm (mycelium)** – hàng triệu **sợi nấm (hyphae)** đan xen, bò khắp ổ bánh và tiết enzyme tiêu hóa nó từ bên ngoài. Chấm đen là hàng nghìn **túi bào tử** sẵn sàng bay đi. Vì sao cắt bỏ phần mốc chưa chắc đã an toàn?""",
("A piece of bread shows a small moldy spot. Why is cutting it off not always enough?",
 ["Molds are bacteria", "Hyphae grow through the bread beyond the visible colony, and fragments can regrow", "Mold spores cannot survive", "Bread contains antibiotics"], 1,
 "Sợi nấm **lan sâu** vào bánh ngoài phần nhìn thấy; **mỗi đoạn sợi** có thể mọc thành hệ sợi mới."),
[
("1. Nấm mốc là gì?", """
- **Molds** (nấm mốc / nấm sợi): nấm **đa bào**, phát triển thành các **sợi dài (hyphae)**. Là **nhân thực**, dị dưỡng **hấp thụ** (tiết enzyme ra ngoài, hấp thụ chất tan).
- Khuẩn lạc nấm mốc: **xốp, bông, dạng bột**, có màu (xanh, đen, vàng…) do bào tử – khác khuẩn lạc vi khuẩn/nấm men (nhẵn, ướt). Slide 7: khuẩn lạc *Penicillium* nhìn đại thể.
- Slide 3 đặt câu hỏi so sánh nấm mốc – nấm men (hình thái, thành, bào tử, sinh sản, trao đổi chất) – xem bài FUN-06.
"""),
("2. Sợi nấm (hyphae) và vách ngăn (septa)", """
- **Hypha** (số nhiều **hyphae**): **ống tế bào** có **thành chitin** bao quanh màng sinh chất và tế bào chất (slide 10).
- **Septate hyphae** (sợi có vách ngăn): có **septa** (số ít septum) – vách ngang chia sợi thành các **đơn vị giống tế bào**, slide ghi mỗi đơn vị **một nhân (uninucleate)**. Vách có **lỗ** cho tế bào chất và nhân di chuyển. Ví dụ: *Penicillium, Aspergillus*.
- **Coenocytic hyphae** (sợi cộng bào / không vách): **không có vách ngăn**, là một khối tế bào chất **dài liên tục chứa nhiều nhân**. Ví dụ: *Rhizopus, Mucor* (nhóm Zygomycetes).

| | Có vách ngăn (septate) | Cộng bào (coenocytic) |
|---|---|---|
| Vách ngang | có (septa có lỗ) | không |
| Nhân | 1 (hoặc vài) mỗi khoang | nhiều nhân trong ống liên tục |
| Ví dụ | *Aspergillus, Penicillium* | *Rhizopus, Mucor* |
"""),
("3. Hệ sợi (mycelium)", """
- **Mycelium** (số nhiều mycelia): **khối sợi nấm đan xen** nhìn thấy được bằng mắt thường – được tạo thành **từ các hyphae**.
- Slide 10 ghi "Mycelia: formed from the mycelium" – hiểu đúng: hệ sợi (mycelium) **được tạo từ nhiều sợi nấm (hyphae)**.
"""),
("4. Sinh trưởng ở đỉnh và phân mảnh (slide 12–13)", """
- Sợi nấm **dài ra ở đỉnh (tip growth)** và phân nhánh.
- **Mỗi phần của sợi đều có khả năng sinh trưởng**; khi một **đoạn sợi bị đứt ra**, nó có thể **kéo dài thành sợi mới** → sinh sản bằng **phân mảnh (fragmentation)**.
- **Bào tử (spores)** là **cơ quan sinh sản** của nấm sợi (bài FUN-05).
"""),
("5. Sợi dinh dưỡng và sợi khí sinh (slide 14)", """
| | **Vegetative hypha** (sợi dinh dưỡng / sợi cơ chất) | **Aerial hypha** (sợi khí sinh / sợi sinh sản) |
|---|---|---|
| Vị trí | trong/trên bề mặt cơ chất | **vươn lên trên** bề mặt môi trường |
| Chức năng | **hấp thụ chất dinh dưỡng** | thường **mang bào tử sinh sản** |
"""),
],
[
("Nấm mốc có lợi trong thực phẩm Việt Nam", """
- ***Aspergillus oryzae*** (mốc tương, koji): làm **tương, nước tương, miso**, rượu sake – tiết amylase, protease mạnh.
- ***Rhizopus, Mucor*** trong **bánh men rượu**, **tempeh** (Indonesia).
- ***Penicillium roqueforti / camemberti***: phô mai xanh, phô mai trắng.
- ***Monascus purpureus***: gạo men đỏ (tạo màu tự nhiên, giảm cholesterol).
"""),
("Nấm mốc có hại: độc tố nấm (mycotoxin)", """
***Aspergillus flavus*** trên lạc, ngô mốc sinh **aflatoxin B1** – một trong những chất **gây ung thư gan mạnh nhất**, **chịu nhiệt**, không bị phá khi nấu. Vì vậy thực phẩm mốc nên **bỏ cả phần** chứ không chỉ cắt chỗ mốc, đặc biệt với thực phẩm mềm, nhiều nước.
"""),
],
[
("Hyphae", "Molds grow as **hyphae**: tubes with a **chitin** wall around the plasma membrane and cytoplasm. **Septate** hyphae have cross-walls (**septa**) dividing them into cell-like units (uninucleate); **coenocytic** hyphae have no septa and many nuclei in one continuous cytoplasm.", "Sợi có vách vs cộng bào."),
("Mycelium and growth", "A **mycelium** is the visible mass of intertwined hyphae. Hyphae grow by **elongating at the tips**; any fragment can grow into a new hypha (**fragmentation**). **Spores** are the reproductive structures.", "Mọc ở đỉnh; đoạn sợi mọc thành sợi mới."),
("Vegetative vs aerial hyphae", "**Vegetative hyphae** obtain nutrients from the substrate. **Aerial (reproductive) hyphae** project above the medium and often bear reproductive spores.", "Sợi dinh dưỡng hấp thụ; sợi khí sinh mang bào tử."),
],
["Coenocytic hyphae have septa", "Mold walls are peptidoglycan", "Only spores can start a new colony"])

q("FUN-04", "recall", 1, "Hyphae that lack cross-walls and contain many nuclei in a continuous cytoplasm are called:",
  ["septate", "coenocytic", "aerial", "pseudohyphae"], 1,
  "**Coenocytic** = không vách ngăn, nhiều nhân (ví dụ *Rhizopus, Mucor*).",
  ["Có vách ngăn.", "", "Chỉ vị trí/chức năng.", "Chuỗi tế bào nấm men."], ["coenocytic", "septa"], "Coenocytic hyphae have septa")
q("FUN-04", "recall", 1, "The cell wall of mold hyphae is made mainly of:",
  ["peptidoglycan", "chitin", "cellulose only", "lipopolysaccharide"], 1,
  "Slide 10: sợi nấm là ống tế bào có **thành chitin**.",
  ["Thành vi khuẩn.", "", "Thành thực vật/tảo lục/oomycetes.", "Màng ngoài Gram âm."], ["chitin", "hyphae"], "Mold walls are peptidoglycan", src=SM + " slide 10")
q("FUN-04", "concept", 2, "Which hyphae usually bear the reproductive spores of a mold?",
  ["Vegetative hyphae growing in the substrate", "Aerial hyphae projecting above the medium", "Septa", "Rhizoids only"], 1,
  "Slide 14: **aerial (reproductive) hyphae** vươn lên trên bề mặt và **thường mang bào tử**.",
  ["Sợi dinh dưỡng hấp thụ chất dinh dưỡng.", "", "Septa là vách ngăn.", "Không đúng."], ["aerial hypha"], src=SM + " slide 14")
q("FUN-04", "concept", 2, "How do hyphae elongate?",
  ["By binary fission of each cell", "Mainly by growth at the tips", "By budding along the length", "By fusion of spores"], 1,
  "Slide 12: sợi nấm **kéo dài ở đỉnh (tip)** và phân nhánh.",
  ["Không.", "", "Nảy chồi là nấm men.", "Không."], ["hyphae"], src=SM + " slide 12")
q("FUN-04", "application", 2, "A mold colony is broken into small hyphal fragments by vigorous shaking and spread on agar. Many colonies appear. This shows that:",
  ["only spores can reproduce molds", "each hyphal fragment can elongate into a new hypha", "hyphae are killed by shaking", "molds are unicellular"], 1,
  "Slide 12: **mỗi phần sợi đều có khả năng sinh trưởng**; đoạn sợi đứt ra mọc thành sợi mới → **phân mảnh**.",
  ["Mảnh sợi cũng tạo khuẩn lạc.", "", "Sai.", "Sai."], ["fragmentation"], "Only spores can start a new colony")
q("FUN-04", "not", 2, "Which statement about septate hyphae is NOT correct?",
  ["They contain cross-walls called septa", "Septa divide them into cell-like units", "They are the typical hyphae of Rhizopus", "Septa usually have pores"], 2,
  "*Rhizopus* có sợi **cộng bào (coenocytic)**. Sợi có vách ngăn điển hình ở *Aspergillus, Penicillium*.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["septate hyphae"], pool="mock")
q("FUN-04", "recall", 1, "The visible mass of intertwined hyphae of a mold is called:",
  ["a septum", "a mycelium", "a sporangium", "a thallus of lichen"], 1,
  "**Mycelium** = khối sợi nấm đan xen.",
  ["Vách ngăn.", "", "Túi bào tử.", "Tản địa y."], ["mycelium"], pool="mock")
q("FUN-04", "concept", 2, "Vegetative hyphae mainly function to:",
  ["produce sexual spores", "obtain nutrients from the substrate", "photosynthesize", "attach to host cells like fimbriae"], 1,
  "Slide 14: **vegetative hypha** = phần sợi **lấy chất dinh dưỡng**.",
  ["Không phải chính.", "", "Nấm không quang hợp.", "Không."], ["vegetative hypha"], pool="mock")

v("FUN-04", "mold", "nấm mốc (nấm sợi)", "A multicellular fungus growing as hyphae.", "Penicillium is a mold.", ["molds", "mould", "filamentous fungi"])
v("FUN-04", "hyphae", "sợi nấm", "Long tubular filaments of a mold with chitin walls.", "Hyphae grow at their tips.", ["hypha"])
v("FUN-04", "septa", "vách ngăn (sợi nấm)", "Cross-walls in hyphae.", "Aspergillus hyphae have septa.", ["septum", "septate", "septate hyphae"])
v("FUN-04", "coenocytic", "cộng bào (không vách ngăn)", "Hyphae without septa, containing many nuclei.", "Rhizopus has coenocytic hyphae.", ["coenocytic hyphae"])
v("FUN-04", "mycelium", "hệ sợi (khuẩn ty)", "The mass of intertwined hyphae.", "The mycelium spreads through bread.", ["mycelia"])
v("FUN-04", "vegetative hypha", "sợi dinh dưỡng (sợi cơ chất)", "The part of a hypha that obtains nutrients.", "Vegetative hyphae penetrate the substrate.", ["vegetative hyphae"])
v("FUN-04", "aerial hypha", "sợi khí sinh", "A hypha projecting above the medium, often bearing spores.", "Aerial hyphae carry sporangia.", ["aerial hyphae", "reproductive hypha"])

fc("FUN-04", "fact", "Septate vs coenocytic hyphae?", "Septate: cross-walls, cell-like units (Aspergillus, Penicillium). Coenocytic: no septa, multinucleate (Rhizopus, Mucor).")
fc("FUN-04", "fact", "Where do hyphae grow?", "At the tips; any fragment can grow into a new hypha.")
fc("FUN-04", "fact", "Vegetative vs aerial hypha?", "Vegetative: obtains nutrients. Aerial: projects above the medium, bears spores.")
fc("FUN-04", "trap", "TRUE/FALSE: mold hyphae have peptidoglycan walls.", "FALSE – chitin.")

# ---------------------------------------------------------------- FUN-05
unit("FUN-05", "Mold spores, the sexual cycle and fungal phyla", "H", 2, 25, SM + ": slides 15–43",
"""Mốc đen trên bánh mì (*Rhizopus*) mang bào tử trong **túi**; mốc xanh trên cam (*Penicillium*) xếp bào tử thành **chuỗi hở** như chổi quét; còn cây nấm rơm bạn ăn là **quả thể** của một nấm đảm. Chỉ cần nhìn **bào tử nằm ở đâu và sinh ra thế nào**, nhà nấm học xếp được nấm vào đúng ngành.""",
("Molds are classified into phyla mainly according to:",
 ["the color of their colonies", "their type of sexual spores (sexual reproduction)", "their cell wall thickness", "whether they cause disease"], 1,
 "Slide 15: nấm mốc được phân loại theo **cách sinh sản hữu tính** – loại **bào tử hữu tính** đặc trưng cho từng ngành."),
[
("1. Phân loại nấm mốc (slide 15–19)", """
Nấm mốc được xếp vào các **ngành** theo **kiểu sinh sản hữu tính**:
| Ngành | Bào tử hữu tính | Sợi | Ví dụ trong bài |
|---|---|---|---|
| **Zygomycota** (Zygomycetes; nay là Mucoromycota) | **zygospore** | cộng bào | ***Rhizopus stolonifer*** (mốc bánh mì đen), *Mucor indicus*, *Absidia* |
| **Ascomycota** (nấm túi) | **ascospore** trong **ascus** | có vách | ***Neurospora crassa***, *Penicillium, Aspergillus* |
| **Basidiomycota** (nấm đảm) | **basidiospore** trên **basidium** | có vách | ***Itajahya*** (nấm lõ chó), nấm mũ |

Ngoài ra *Allomyces* (Blastocladiomycota) có **bào tử động (zoospore)**. Phân loại hiện đại dựa thêm vào trình tự DNA (cây phân loại 2018 trên slide).
"""),
("2. Bào tử vô tính (slide 20–31)", """
Nấm mốc có thể sinh sản **vô tính, hữu tính hoặc cả hai**. **Bào tử vô tính** do một cá thể tạo ra qua **nguyên phân** và phân chia tế bào:

**a) Sporangiospores (bào tử túi / bào tử kín)**: hình thành **bên trong túi – sporangium**, ở đầu một sợi khí sinh gọi là **sporangiophore** (cuống túi). Ví dụ: *Rhizopus, Mucor, Absidia*.

**b) Conidiospores (conidia – bào tử đính / bào tử trần)**: bào tử đơn bào hoặc đa bào **không nằm trong túi**, sinh ra ở đầu **conidiophore**. Ví dụ: *Penicillium* (chổi), *Aspergillus* (bông hoa cúc). Các kiểu conidia [fig]:
- **Arthroconidia**: sợi đứt thành đoạn (*Coccidioides*).
- **Blastoconidia**: nảy chồi từ tế bào mẹ (*Candida*).
- **Chlamydoconidia**: bào tử **vách dày** hình thành trong đoạn sợi (*Candida albicans*).

**c) Zoospores (bào tử động)**: bào tử **di động bằng roi (flagella)**, bơi trong nước (*Allomyces*, nấm chytrid).
"""),
("3. Sinh sản hữu tính – 3 giai đoạn (slide 32–34)", """
Bào tử hữu tính **đặc trưng cho từng ngành**. Sinh sản hữu tính gồm:
1. **Plasmogamy (chất giao)**: nhân **đơn bội** của tế bào cho (+) **xâm nhập tế bào chất** của tế bào nhận (−).
2. **Karyogamy (nhân giao)**: nhân (+) và (−) **hợp nhất** thành **nhân hợp tử lưỡng bội**.
3. **Meiosis (giảm phân)**: nhân lưỡng bội tạo các **nhân đơn bội** (bào tử hữu tính), một số là **tái tổ hợp di truyền**.

Mẹo: **Chất → Nhân → Giảm** (P-K-M). Giữa plasmogamy và karyogamy có thể là pha **song nhân (n + n, dikaryotic)** kéo dài, đặc biệt ở nấm đảm.
"""),
("4. Ba loại bào tử hữu tính (slide 35–43)", """
**Zygospore (bào tử tiếp hợp)** – Zygomycota:
- Hai sợi của hai kiểu giao phối (+/−) mọc lại gần nhau, đầu sợi phình (gametangia) và **hợp nhất** → **zygospore vách dày, sần** chịu điều kiện bất lợi → nảy mầm, giảm phân, tạo sporangium. Ví dụ *Rhizopus stolonifer, Mucor indicus*.

**Ascospore (bào tử túi)** – Ascomycota:
- Hình thành **bên trong túi – ascus**; thường **8 ascospores** mỗi ascus (4 nhân sau giảm phân + 1 lần nguyên phân). Túi thường nằm trong **quả thể (ascocarp)**. Ví dụ *Neurospora crassa*, *Penicillium*, *Aspergillus*, nấm men *Saccharomyces* (4 bào tử).

**Basidiospore (bào tử đảm)** – Basidiomycota:
- Hình thành **bên ngoài** một cấu trúc hình chùy gọi là **đảm – basidium**, thường **4 bào tử**/đảm.
- Slide 40–41: **quả thể (basidiocarp)** → **phiến nấm (gill)** → **đảm (basidia)** → **bào tử đảm (basidiospore)**.

| | Zygospore | Ascospore | Basidiospore |
|---|---|---|---|
| Vị trí | bào tử vách dày tự do | **trong** ascus | **ngoài** basidium |
| Số lượng | 1 | thường **8**/túi | thường **4**/đảm |
| Ngành | Zygomycota | Ascomycota | Basidiomycota |
"""),
("5. Tổng hợp: nhận diện nhanh", """
- Có **túi chứa bào tử vô tính** + sợi không vách → nghĩ tới **Zygomycota** (*Rhizopus*).
- Bào tử **trần xếp chuỗi** trên cuống + sợi có vách → **Ascomycota** dạng vô tính (*Penicillium, Aspergillus*).
- Có **quả thể dạng nấm mũ, phiến** → **Basidiomycota**.
- **Bào tử có roi** → zoospore (*Allomyces*, chytrid; lưu ý oomycetes cũng có zoospore nhưng là **nguyên sinh vật** – bài PRO-03).
"""),
],
[
("Công nghiệp: bào tử nấm là \"giống\" sản xuất", """
- Sản xuất **acid citric** bằng *Aspergillus niger* và **penicillin** bằng *Penicillium chrysogenum* đều bắt đầu từ **huyền phù bào tử (conidia)** được đếm bằng buồng đếm (~10⁶–10⁷ bào tử/mL) rồi cấy vào nồi lên men (APP-04).
- **Nấm ăn** (nấm rơm *Volvariella*, nấm bào ngư *Pleurotus*, nấm hương *Lentinula*) là **quả thể của nấm đảm** – ngành trồng nấm là nông nghiệp vi sinh lớn ở Việt Nam.
"""),
("Y tế: bào tử và dị ứng", """
Bào tử *Aspergillus* trong không khí có thể gây **bệnh aspergillosis** ở phổi người suy giảm miễn dịch; bào tử mốc trong nhà ẩm là tác nhân dị ứng, hen suyễn phổ biến.
"""),
],
[
("Classification of molds", "Molds are classified into phyla by their **sexual reproduction**: **Zygomycota** (zygospores; *Rhizopus stolonifer*), **Ascomycota** (ascospores in asci; *Neurospora crassa*), **Basidiomycota** (basidiospores on basidia; *Itajahya*, mushrooms).", "Phân ngành theo bào tử hữu tính."),
("Asexual spores", "Formed by mitosis. **Sporangiospores**: inside a **sporangium** at the tip of a **sporangiophore** (*Rhizopus, Absidia*). **Conidiospores (conidia)**: not enclosed in a sac (*Penicillium, Aspergillus*; arthro-, blasto-, chlamydoconidia). **Zoospores**: motile with **flagella**.", "Bào tử kín, bào tử trần, bào tử động."),
("Sexual cycle", "1) **Plasmogamy**: a haploid (+) nucleus enters the cytoplasm of a (−) cell. 2) **Karyogamy**: nuclei fuse → diploid zygote nucleus. 3) **Meiosis**: haploid nuclei, some recombinant.", "Chất giao → nhân giao → giảm phân."),
("Sexual spores", "**Zygospore**: thick-walled spore from fusion of two hyphal tips (Zygomycota). **Ascospore**: inside an **ascus** (often 8). **Basidiospore**: outside a **basidium** (often 4); basidiocarp → gills → basidia → basidiospores.", "Zygo – trong túi – ngoài đảm."),
],
["Conidia are formed in a sporangium", "Basidiospores form inside the basidium", "Karyogamy comes before plasmogamy", "Asexual spores are formed by meiosis"])

q("FUN-05", "recall", 1, "Asexual spores formed inside a sac at the tip of an aerial hypha are called:",
  ["conidiospores", "sporangiospores", "ascospores", "zygospores"], 1,
  "Slide 22: **sporangiospores** hình thành **trong sporangium** ở đầu **sporangiophore**.",
  ["Conidia không nằm trong túi.", "", "Bào tử hữu tính trong ascus.", "Bào tử hữu tính vách dày."], ["sporangiospore", "sporangium"], "Conidia are formed in a sporangium", src=SM + " slide 22")
q("FUN-05", "recall", 1, "A conidiospore (conidium) is best defined as:",
  ["a motile spore with flagella", "a unicellular or multicellular spore NOT enclosed in a sac", "a sexual spore formed inside an ascus", "a thick-walled spore formed after fusion of hyphae"], 1,
  "Slide 24: conidium là bào tử đơn/đa bào **không nằm trong túi**.",
  ["Đó là zoospore.", "", "Đó là ascospore.", "Đó là zygospore."], ["conidiospore"], src=SM + " slide 24")
q("FUN-05", "concept", 2, "Put the three phases of fungal sexual reproduction in the correct order.",
  ["Karyogamy → plasmogamy → meiosis", "Plasmogamy → karyogamy → meiosis", "Meiosis → plasmogamy → karyogamy", "Plasmogamy → meiosis → karyogamy"], 1,
  "Slide 34: **Plasmogamy** (nhân + vào tế bào chất −) → **Karyogamy** (hợp nhân → 2n) → **Meiosis** (→ n).",
  ["Không thể hợp nhân khi nhân chưa vào chung tế bào chất.", "", "Giảm phân cần nhân 2n trước.", "Giảm phân trước hợp nhân là sai."], ["plasmogamy", "karyogamy"], "Karyogamy comes before plasmogamy", src=SM + " slide 34")
q("FUN-05", "concept", 2, "Basidiospores differ from ascospores in that basidiospores are formed:",
  ["inside an ascus", "externally on a club-shaped basidium", "by mitosis", "inside a sporangium"], 1,
  "**Basidiospore** hình thành **bên ngoài** basidium; **ascospore** hình thành **bên trong** ascus.",
  ["Đó là ascospore.", "", "Bào tử hữu tính hình thành sau giảm phân.", "Sporangium chứa bào tử vô tính."], ["basidiospore", "basidium"], "Basidiospores form inside the basidium")
q("FUN-05", "recall", 1, "Rhizopus stolonifer, the black bread mold, belongs to the group that produces:",
  ["ascospores", "basidiospores", "zygospores", "zoospores only"], 2,
  "*Rhizopus stolonifer* thuộc **Zygomycota** – bào tử hữu tính là **zygospore**; bào tử vô tính là **sporangiospore**.",
  ["Ascomycota (Neurospora).", "Basidiomycota.", "", "Sai."], ["zygospore"], src=SM + " slide 17")
q("FUN-05", "not", 2, "Which is NOT an asexual spore of molds?",
  ["Sporangiospore", "Conidiospore", "Zoospore", "Ascospore"], 3,
  "Slide 20–21: bào tử vô tính gồm sporangiospore, conidiospore, zoospore. **Ascospore là bào tử hữu tính**.",
  ["Vô tính.", "Vô tính.", "Vô tính.", ""], ["ascospore"], "Asexual spores are formed by meiosis")
q("FUN-05", "concept", 2, "Asexual spores are produced by:",
  ["meiosis after karyogamy", "mitosis and subsequent cell division of one individual", "fusion of two mating types", "binary fission of bacteria"], 1,
  "Slide 21: bào tử vô tính do **một cá thể** tạo ra qua **nguyên phân** và phân chia tế bào.",
  ["Đó là bào tử hữu tính.", "", "Đó là hữu tính.", "Sai."], ["mitosis"])
q("FUN-05", "application", 2, "Under the microscope, a mold shows septate hyphae and chains of spores borne openly on brush-like conidiophores. It most likely is:",
  ["Rhizopus", "Penicillium", "Mucor", "Allomyces"], 1,
  "Sợi có vách + **conidia trần xếp chuỗi hình chổi** → ***Penicillium***.",
  ["Rhizopus: sợi cộng bào, sporangium.", "", "Mucor: sporangium.", "Allomyces: zoospore."], ["conidiospore"])
q("FUN-05", "recall", 1, "In the mushroom structure, the order from macroscopic to microscopic is:",
  ["basidia → gills → basidiocarp → basidiospores", "basidiocarp → gills → basidia → basidiospores", "gills → basidiospores → basidiocarp → basidia", "ascocarp → asci → ascospores"], 1,
  "Slide 41: **quả thể (basidiocarp) → phiến nấm (gill) → đảm (basidia) → bào tử đảm**.",
  ["Ngược.", "", "Sai.", "Đó là nấm túi."], ["basidiocarp"], pool="mock", src=SM + " slide 41")
q("FUN-05", "concept", 2, "During plasmogamy:",
  ["a haploid nucleus of a donor (+) cell penetrates the cytoplasm of a recipient (−) cell", "two nuclei fuse into a diploid nucleus", "the diploid nucleus undergoes meiosis", "spores are released from a sporangium"], 0,
  "Slide 34: plasmogamy = nhân đơn bội (+) **xâm nhập tế bào chất** (−). Hợp nhân là karyogamy.",
  ["", "Karyogamy.", "Meiosis.", "Không."], ["plasmogamy"], pool="mock")
q("FUN-05", "recall", 1, "Neurospora crassa is shown in the lecture as an example of which group?",
  ["Zygomycota", "Ascomycota", "Basidiomycota", "Oomycota"], 1,
  "Slide 18: *Neurospora crassa* – nấm túi (**Ascomycota**), 8 ascospore trong ascus.",
  ["Rhizopus.", "", "Itajahya.", "Oomycetes là nguyên sinh vật."], ["ascomycetes"], pool="mock", src=SM + " slide 18")
q("FUN-05", "not", 2, "Which statement about zoospores is NOT correct?",
  ["They are motile", "They use flagella for locomotion", "They are asexual spores", "They are formed inside an ascus"], 3,
  "Zoospore là bào tử **vô tính di động bằng roi**; bào tử trong ascus là **ascospore**.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["zoospore"], pool="mock")

v("FUN-05", "spore", "bào tử", "A reproductive cell of fungi (asexual or sexual).", "Molds spread by spores.", ["spores"])
v("FUN-05", "sporangiospore", "bào tử túi (bào tử kín)", "Asexual spore formed inside a sporangium.", "Rhizopus releases sporangiospores.", ["sporangiospores"])
v("FUN-05", "sporangium", "túi bào tử", "A sac at the tip of a sporangiophore containing sporangiospores.", "The black dots on bread are sporangia.", ["sporangia", "sporangiophore"])
v("FUN-05", "conidiospore", "bào tử đính (bào tử trần)", "Asexual spore not enclosed in a sac.", "Penicillium forms chains of conidiospores.", ["conidia", "conidium", "conidiospores", "conidiophore"])
v("FUN-05", "zoospore", "bào tử động", "A motile asexual spore with flagella.", "Allomyces produces zoospores.", ["zoospores"])
v("FUN-05", "plasmogamy", "chất giao (hợp nhất tế bào chất)", "Entry of a haploid donor nucleus into the cytoplasm of a recipient cell.", "Plasmogamy precedes karyogamy.")
v("FUN-05", "karyogamy", "nhân giao (hợp nhân)", "Fusion of two haploid nuclei into a diploid nucleus.", "Karyogamy forms a zygote nucleus.")
v("FUN-05", "zygospore", "bào tử tiếp hợp", "Thick-walled sexual spore formed by fusion of two hyphal tips (Zygomycota).", "Rhizopus forms zygospores.", ["zygospores", "Zygomycota", "zygomycetes"])
v("FUN-05", "basidiospore", "bào tử đảm", "Sexual spore formed externally on a basidium.", "A mushroom gill releases basidiospores.", ["basidiospores"])
v("FUN-05", "basidium", "đảm", "Club-shaped cell bearing basidiospores.", "Each basidium bears four spores.", ["basidia"])
v("FUN-05", "basidiocarp", "quả thể nấm đảm", "The fruiting body (mushroom) of a basidiomycete.", "The basidiocarp has gills.", ["gill", "gills"])

fc("FUN-05", "fact", "Three asexual spores of molds?", "Sporangiospores (in a sporangium), conidiospores (not enclosed), zoospores (flagellated).")
fc("FUN-05", "fact", "Three phases of sexual reproduction?", "Plasmogamy → karyogamy → meiosis.")
fc("FUN-05", "fact", "Sexual spores and phyla?", "Zygospore – Zygomycota (Rhizopus); ascospore – Ascomycota (Neurospora); basidiospore – Basidiomycota (mushrooms, Itajahya).")
fc("FUN-05", "fact", "Mushroom hierarchy?", "Basidiocarp → gills → basidia → basidiospores.")
fc("FUN-05", "trap", "TRUE/FALSE: basidiospores form inside the basidium.", "FALSE – outside; ascospores form inside the ascus.")

# ---------------------------------------------------------------- FUN-06
unit("FUN-06", "Lichens; comparing molds, yeasts and bacteria; mold biomass", "M", 2, 15, SM + ": slides 3, 44–48",
"""Trên thân cây cổ thụ và đá núi có những mảng xanh xám, vàng cam như vảy – đó là **địa y (lichen)**: một "liên minh" giữa **nấm** và **tảo** (hoặc vi khuẩn lam). Địa y chỉ mọc nơi không khí sạch, nên được dùng làm **chỉ thị ô nhiễm không khí**. Còn khi muốn biết một nồi nấm mốc đã mọc bao nhiêu, ta **không đếm tế bào** như nấm men được – vì sao?""",
("Why is counting individual cells not a good way to measure the growth of a mold in liquid culture?",
 ["Molds do not contain cells", "Molds form a continuous branching network of hyphae with no clear individual cells, so biomass (dry weight) is measured instead", "Molds are too small to see", "Mold cells are always dead"], 1,
 "Nấm mốc tạo **mạng sợi liên tục**, không có ranh giới tế bào rõ → đo **sinh khối (khối lượng khô)** hoặc **đếm bào tử**."),
[
("1. Địa y (lichens) – slide 44–46", """
- **Lichen** = sự kết hợp **cộng sinh** giữa **một nấm** (thường là nấm túi) và **một đối tác quang hợp** (**tảo lục** hoặc **vi khuẩn lam**).
  - **Nấm**: tạo cấu trúc, bám giá thể, giữ nước, hấp thụ khoáng.
  - **Tảo/vi khuẩn lam**: **quang hợp**, cung cấp **chất hữu cơ** cho nấm.
- Ba dạng tản (thallus) [fig]:
| Dạng | Mô tả |
|---|---|
| **Crustose** (dạng vỏ) | bám chặt, phẳng như lớp vỏ trên đá/cây |
| **Foliose** (dạng lá) | giống lá, mép nhấc lên |
| **Fruticose** (dạng bụi/cành) | dạng sợi, cành nhánh, treo hoặc đứng |
- Sinh sản sinh dưỡng bằng **soredia** (cụm sợi nấm + tế bào tảo) hoặc phân mảnh.
- Vai trò: **sinh vật tiên phong** phân hủy đá tạo đất; **chỉ thị ô nhiễm SO₂**; thức ăn tuần lộc; thuốc nhuộm (quỳ tím – litmus – chiết từ địa y).
"""),
("2. So sánh nấm mốc – nấm men – vi khuẩn (slide 3)", """
| Đặc điểm | **Nấm mốc** | **Nấm men** | **Vi khuẩn** |
|---|---|---|---|
| Hình thái | **đa bào, dạng sợi** (hyphae, mycelium) | **đơn bào**, cầu/bầu dục | đơn bào nhân sơ |
| Thành tế bào | chủ yếu **chitin** (+ glucan) | glucan, mannan, chitin (sẹo chồi) | peptidoglycan |
| Bào tử | bào tử **vô tính** (sporangio-, conidio-, zoospore) và **hữu tính** (zygo-, asco-, basidiospore) | ascospore/basidiospore; bào tử vô tính ít | nội bào tử (sống sót) |
| Sinh sản | **bào tử**, **phân mảnh sợi** | **nảy chồi**, phân đôi; hữu tính | phân đôi |
| Trao đổi chất | dị dưỡng, phần lớn **hiếu khí** | dị dưỡng, **kỵ khí tùy nghi** | rất đa dạng |
| pH tối ưu | ~5–6 (chịu acid) | ~5–6 | ~6,5–7,5 |
| Khuẩn lạc | xốp, bông, có màu bào tử | nhẵn, ướt, trắng kem | nhẵn/nhầy |
"""),
("3. Định lượng sinh khối nấm mốc (slide 48)", """
**a) Định lượng bào tử (spore quantification)**:
- Rửa bào tử khỏi bề mặt khuẩn lạc bằng nước có chất hoạt động bề mặt (Tween 80) → lọc bỏ sợi → **đếm bào tử bằng buồng đếm** (bào tử/mL) hoặc **cấy đĩa đếm CFU**.

**b) Định lượng sinh khối (biomass quantification)**:
- **Khối lượng khô (dry weight)**: lọc/ly tâm thu sinh khối → rửa → **sấy đến khối lượng không đổi** → cân (g/L).
- Có thể đo **đường kính khuẩn lạc** trên thạch theo thời gian (tốc độ lan).

**So sánh cách định lượng** giữa ba nhóm:
| | Vi khuẩn | Nấm men | Nấm mốc |
|---|---|---|---|
| Đếm trực tiếp | buồng đếm Petroff-Hausser | buồng đếm hồng cầu | chỉ **đếm bào tử** |
| Đếm khuẩn lạc (CFU) | có | có | bào tử/mảnh sợi (CFU **không** tỉ lệ sinh khối) |
| Độ đục (OD) | có | có | **không phù hợp** (sợi kết viên, không đồng nhất) |
| Khối lượng khô | có | có | **phương pháp chính** |
"""),
],
[
("Công nghệ: đo sinh khối trong nồi lên men nấm", """
Trong sản xuất penicillin hay acid citric, sợi nấm có thể mọc dạng **viên (pellet)** hoặc **sợi phân tán** làm dịch rất nhớt. Kỹ sư theo dõi **khối lượng khô tế bào (DCW, g/L)** và **thể tích sinh khối lắng (packed mycelial volume)** thay cho OD. Hình thái viên/sợi ảnh hưởng mạnh đến truyền oxy và năng suất.
"""),
],
[
("Lichens", "A **symbiosis** of a **fungus** and a photosynthetic partner (**green alga** or **cyanobacterium**). Forms: **crustose** (crust), **foliose** (leaflike), **fruticose** (shrubby). The alga makes organic food; the fungus provides structure and water.", "Địa y = nấm + tảo/vi khuẩn lam."),
("Mold vs yeast", "Molds: multicellular **hyphae**, chitin walls, many asexual and sexual spores, reproduce by spores and fragmentation, mostly aerobic. Yeasts: unicellular, glucan–mannan–chitin walls, **budding**/fission, facultative anaerobes.", "Nấm mốc sợi – nấm men đơn bào."),
("Mold quantification", "Molds are measured by **spore quantification** (counting chamber or CFU of spores) and **biomass quantification** (**dry weight** to constant mass). Direct cell counts and turbidity are unsuitable for hyphal networks.", "Nấm mốc: đếm bào tử + khối lượng khô."),
],
["Lichens are a single organism", "Molds are measured by turbidity", "Molds are unicellular"])

q("FUN-06", "recall", 1, "A lichen is a symbiotic association between:",
  ["a fungus and a bacterium that fixes nitrogen only", "a fungus and a green alga or cyanobacterium", "two different yeasts", "a protozoan and an alga"], 1,
  "Địa y = **nấm + tảo lục hoặc vi khuẩn lam** (đối tác quang hợp).",
  ["Không đủ; đối tác phải quang hợp.", "", "Sai.", "Sai."], ["lichen"], "Lichens are a single organism", src=SM + " slides 44–46")
q("FUN-06", "recall", 1, "A leaflike lichen with lobes that lift from the surface is described as:",
  ["crustose", "foliose", "fruticose", "coenocytic"], 1,
  "**Foliose** = dạng lá. Crustose = dạng vỏ bám phẳng; fruticose = dạng bụi/cành.",
  ["Dạng vỏ.", "", "Dạng bụi.", "Thuật ngữ sợi nấm."], ["foliose"])
q("FUN-06", "concept", 2, "Which method is most appropriate for measuring mold growth in a shaken liquid culture?",
  ["Turbidity at 600 nm", "Dry weight of the mycelium", "Direct count of individual cells in a counting chamber", "Counting endospores"], 1,
  "Sợi nấm **kết viên, không đồng nhất** → OD và đếm tế bào không phù hợp → dùng **khối lượng khô**.",
  ["Sợi nấm làm độ đục không phản ánh sinh khối.", "", "Không có tế bào riêng rẽ.", "Nấm không tạo nội bào tử."], ["dry weight", "biomass"], "Molds are measured by turbidity")
q("FUN-06", "not", 2, "Which comparison between molds and yeasts is NOT correct?",
  ["Molds are filamentous; yeasts are unicellular", "Yeasts typically reproduce by budding; molds by spores and fragmentation", "Molds have peptidoglycan walls; yeasts have chitin", "Both are eukaryotic fungi"], 2,
  "Cả hai đều **không có peptidoglycan**; nấm mốc chủ yếu **chitin**.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["chitin"], "Molds are unicellular")
q("FUN-06", "concept", 2, "In a lichen, the main role of the algal or cyanobacterial partner is to:",
  ["absorb minerals from rock", "provide organic compounds by photosynthesis", "form the fruiting body", "produce zoospores"], 1,
  "Đối tác quang hợp cung cấp **chất hữu cơ**; nấm tạo cấu trúc, giữ nước, hấp thụ khoáng.",
  ["Vai trò của nấm.", "", "Của nấm.", "Không."], ["lichen"])
q("FUN-06", "application", 2, "A student needs the number of Aspergillus spores per mL to inoculate a fermenter quickly. The best method is:",
  ["dry weight of the colony", "counting the spore suspension in a counting chamber", "measuring colony diameter", "Gram staining"], 1,
  "Cần **số bào tử/mL nhanh** → **đếm bào tử bằng buồng đếm**.",
  ["Cho sinh khối, không phải số bào tử.", "", "Cho tốc độ lan.", "Không định lượng."], ["spore", "counting chamber"], pool="mock")
q("FUN-06", "recall", 1, "Which lichen form is shrubby or branched?",
  ["Crustose", "Foliose", "Fruticose", "Septate"], 2,
  "**Fruticose** = dạng bụi/cành.",
  ["Dạng vỏ.", "Dạng lá.", "", "Không phải dạng địa y."], ["fruticose"], pool="mock")
q("FUN-06", "concept", 2, "Why do colony counts (CFU) of a mold not reflect its biomass well?",
  ["Molds cannot form colonies", "A clump of spores may give one CFU while fragmented mycelium can give many CFU", "CFU counts only dead cells", "Molds grow only in liquid"], 1,
  "CFU phụ thuộc số **đơn vị** (bào tử/mảnh sợi) chứ không phụ thuộc **khối lượng** sợi.",
  ["Sai.", "", "Sai.", "Sai."], ["CFU", "biomass"], pool="mock")

v("FUN-06", "lichen", "địa y", "A symbiosis of a fungus with a green alga or cyanobacterium.", "Lichens indicate clean air.", ["lichens"])
v("FUN-06", "crustose", "địa y dạng vỏ", "A flat, crustlike lichen tightly attached to the surface.", "Crustose lichens grow on rocks.", ["foliose", "fruticose"])
v("FUN-06", "symbiosis", "cộng sinh", "A close relationship between two different organisms.", "A lichen is a symbiosis.")
v("FUN-06", "biomass", "sinh khối", "The mass of living cells.", "Mold biomass is measured as dry weight.")
v("FUN-06", "dry weight", "khối lượng khô", "Mass of cells after drying to constant weight.", "Dry weight is used for molds.", ["dry cell weight"])

fc("FUN-06", "fact", "Lichen partners?", "A fungus + a green alga or cyanobacterium.")
fc("FUN-06", "fact", "Three lichen forms?", "Crustose (crust), foliose (leaflike), fruticose (shrubby).")
fc("FUN-06", "fact", "Two ways to quantify molds?", "Spore quantification (chamber/CFU) and biomass quantification (dry weight).")
