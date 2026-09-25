from _lib import *

SRC = "1.History of Microbiology.pptx"

# ---------------------------------------------------------------- HIS-01
unit("HIS-01", "The microbial world; Hooke and Leeuwenhoek", "M", 1, 15, SRC + ": slides 2–7, 23–27",
"""Bạn cầm một giọt nước ao dưới kính hiển vi trường học và thấy hàng trăm "con vật" li ti bơi lội. Năm 1673, một người bán vải ở Hà Lan — **Anton van Leeuwenhoek** — cũng thấy đúng cảnh đó bằng một chiếc kính tự mài chỉ có **một thấu kính**. Ông gọi chúng là **animalcules**. Vậy ai là người đầu tiên *đặt tên* cho "tế bào", và ai là người đầu tiên *thấy vi sinh vật sống*?""",
("Who was the first to observe and describe LIVING microorganisms (\"animalcules\")?",
 ["Robert Hooke", "Anton van Leeuwenhoek", "Louis Pasteur", "Robert Koch"], 1,
 "Leeuwenhoek (1673) là người đầu tiên quan sát vi sinh vật **sống**. Hooke (1665) quan sát lát **bần (cork)** – chỉ là thành tế bào chết – và đặt ra từ **cell**."),
[
("1. Vi sinh vật học nghiên cứu gì?", """
**Microbiology** (vi sinh vật học) nghiên cứu các sinh vật quá nhỏ để nhìn rõ bằng mắt thường – **microorganisms / microbes** – cùng hoạt động của chúng. Đây là một *phạm vi nghiên cứu*, không phải một nhánh phân loại duy nhất.

Slide 24 chia thế giới vi sinh vật của môn học thành các nhóm:

| Nhóm | Gồm | Kiểu tế bào |
|---|---|---|
| **Bacteria** (vi khuẩn) | vi khuẩn "thật" | nhân sơ (prokaryote) |
| **Archaea** (vi khuẩn cổ) | nhiều loài sống môi trường khắc nghiệt | nhân sơ |
| **Fungi** (nấm) | **yeasts** (nấm men), **molds** (nấm mốc), macroscopic fungi (nấm lớn) | nhân thực (eukaryote) |
| **Protists** (nguyên sinh vật) | **protozoa**, **algae** (tảo), **oomycetes**, **slime molds** (nấm nhầy) | nhân thực |
| **Viruses** | virus, viroid, prion | **không có cấu tạo tế bào** |

- Vi sinh vật **không chỉ gây bệnh**: phần lớn có lợi – phân giải chất hữu cơ, quay vòng N/C, làm bánh mì, bia, sữa chua, kháng sinh, enzyme…
- Nhỏ ≠ nhân sơ: nấm men nhỏ nhưng là **nhân thực**.
- Virus không phải "vi khuẩn rất nhỏ"; nó không có ribosome, không tự trao đổi chất.
"""),
("2. Robert Hooke (1665) – từ \"cell\" ra đời", """
- Năm **1665**, **Robert Hooke** (Anh) dùng kính hiển vi phức (compound microscope) thô sơ quan sát **lát bần (cork)** và thấy những ô nhỏ, ông gọi là **"cells"**.
- Slide ghi: Hooke phát hiện "đơn vị nhỏ nhất của sự sống" → **mở đường cho học thuyết tế bào (Cell Theory)**.
- Thực ra Hooke chỉ thấy **thành tế bào chết** của mô bần, chưa thấy tế bào sống hay vi sinh vật. Học thuyết tế bào (mọi sinh vật cấu tạo từ tế bào) được hoàn thiện sau này bởi Schleiden, Schwann (1838–1839) và Virchow (1858).
"""),
("3. Anton van Leeuwenhoek (1673–1723) – người đầu tiên thấy vi sinh vật sống", """
- **1673**: Leeuwenhoek (Hà Lan) tự chế khoảng **400 kính hiển vi đơn thấu kính** (phóng đại tới ~300 lần) và quan sát **tế bào sống**.
- Ông mô tả **"animalcules"** (động vật nhỏ li ti) trong nước mưa, phân, cặn răng… và gửi hàng loạt thư cho **Hội Hoàng gia Anh (Royal Society)** trong giai đoạn **1673–1723**.
- Hình vẽ của ông [fig] cho thấy các dạng cầu, que, xoắn – chính là vi khuẩn.

| | Hooke | Leeuwenhoek |
|---|---|---|
| Năm | 1665 | 1673 |
| Nước | Anh | Hà Lan |
| Kính | kính phức thô sơ | kính **một thấu kính** tự mài |
| Thấy gì | ô bần (thành tế bào chết) | **vi sinh vật sống** ("animalcules") |
| Ý nghĩa | đặt tên "cell", mở đầu học thuyết tế bào | khai sinh việc quan sát vi sinh vật |
"""),
("4. Dòng thời gian nhanh (slide 4–7) [fig]", """
Các slide 4–7 là hình dòng thời gian trong giáo trình Tortora. Những mốc hay được hỏi:

| Năm | Sự kiện |
|---|---|
| 1665 | Hooke – "cells" |
| 1673 | Leeuwenhoek – vi sinh vật sống |
| 1668 | Redi – thí nghiệm dòi (chống tự sinh ở sinh vật lớn) |
| 1796 | Jenner – vaccine đầu tiên (đậu mùa) |
| 1835 | Bassi – nấm gây bệnh tằm |
| 1857–1864 | Pasteur – lên men, bác bỏ tự sinh (1861), thanh trùng |
| 1867 | Lister – phẫu thuật vô khuẩn (phenol) |
| 1876 | Koch – *Bacillus anthracis* gây bệnh than → định đề Koch |
| 1880 | Pasteur – vaccine giảm độc lực (tả gà) |
| 1910 | Ehrlich – salvarsan chữa giang mai |
| 1928 | Fleming – penicillin |

Mẹo: **H**ooke → **L**eeuwenhoek → **R**edi → **J**enner → **P**asteur → **K**och → **E**hrlich → **F**leming theo thứ tự thời gian (trừ Redi 1668 chen giữa Hooke và Leeuwenhoek về *ý tưởng*).
"""),
("5. Độ phóng đại và độ phân giải", """
- **Magnification** (độ phóng đại): ảnh to lên bao nhiêu lần.
- **Resolution** (độ phân giải): khả năng phân biệt **hai điểm gần nhau** thành hai điểm riêng. Kính quang học giới hạn ≈ **0,2 μm**.
- Vi khuẩn điển hình dài 1–5 μm → thấy được bằng kính quang học; virus (20–300 nm) cần **kính hiển vi điện tử**.
- Phóng đại mà không tăng độ phân giải thì chỉ được một ảnh "to mà mờ" (empty magnification). [mở rộng]
"""),
],
[
("Thực tế: kính hiển vi trong phòng thí nghiệm của bạn", """
Kính hiển vi quang học trong phòng lab CH3004 dùng vật kính dầu **100×** × thị kính **10×** = **1000×** để xem vi khuẩn nhuộm Gram. Dầu soi (immersion oil) giúp tăng độ phân giải vì giảm tán xạ ánh sáng. Đây là hậu duệ trực tiếp của kính Hooke, còn kính một thấu kính của Leeuwenhoek là "tổ tiên" của kính lúp.
"""),
("Mở rộng: vi sinh vật quanh ta", """
- Cơ thể người mang số tế bào vi khuẩn **tương đương** số tế bào người (≈ 3,8 × 10¹³) – **microbiome**.
- Khoảng 50 % O₂ trên Trái Đất đến từ vi sinh vật quang hợp ở biển (vi khuẩn lam, tảo silic).
- Ngành công nghệ sinh học (chuyên ngành của bạn) dựa trên vi sinh vật: enzyme, kháng sinh, ethanol, protein đơn bào (SCP) – sẽ học ở tuần 13–15.
"""),
],
[
("Hooke, 1665", "Robert Hooke observed thin slices of **cork** with a crude compound microscope and named the little boxes **\"cells\"**. He saw dead cell walls, not living microbes. His work opened the way to the **cell theory**.", "Hooke đặt tên cell, nhưng chỉ thấy thành tế bào chết."),
("Leeuwenhoek, 1673", "Anton van **Leeuwenhoek** built about **400 single-lens microscopes** and was the **first to observe living microorganisms**, which he called **\"animalcules\"**. He reported them in letters to the Royal Society (1673–1723).", "Leeuwenhoek: người đầu tiên thấy vi sinh vật sống."),
("Groups of microbes", "Microbiology covers **bacteria** and **archaea** (prokaryotes), **fungi** (yeasts, molds), **protists** (protozoa, algae, oomycetes, slime molds) and **viruses** (acellular). Most microbes are harmless or beneficial.", "Virus không có cấu tạo tế bào; nấm và nguyên sinh vật là nhân thực."),
],
["Hooke saw living microbes", "Viruses are tiny bacteria", "Microbes are mostly pathogens", "Magnification equals resolution"])

q("HIS-01", "recall", 1, "In 1665, Robert Hooke used a crude microscope to examine thin slices of cork. What was his main contribution?",
  ["He described living \"animalcules\" in rainwater", "He named the small boxes he saw \"cells\"", "He disproved spontaneous generation", "He proved that microbes cause disease"], 1,
  "Hooke (1665) quan sát lát **bần (cork)** và gọi các ô nhỏ là **cells** → mở đường cho **học thuyết tế bào**. Người mô tả **animalcules** sống là Leeuwenhoek (1673).",
  ["Đây là Leeuwenhoek, không phải Hooke.", "", "Bác bỏ tự sinh là Redi/Spallanzani/Pasteur.", "Liên hệ vi sinh vật – bệnh là Koch (1876)."],
  ["cell theory"], "Hooke saw living microbes", src=SRC + " slide 3")
q("HIS-01", "recall", 1, "Anton van Leeuwenhoek is best known as the first person to:",
  ["observe living microorganisms", "develop a vaccine", "grow bacteria in pure culture", "use phenol in surgery"], 0,
  "Leeuwenhoek dùng kính **một thấu kính** tự chế (khoảng 400 chiếc) và là người **đầu tiên quan sát vi sinh vật sống** (animalcules), báo cáo cho Hội Hoàng gia Anh từ 1673.",
  ["", "Vaccine: Jenner (1796).", "Nuôi cấy thuần: Koch.", "Phenol trong phẫu thuật: Lister (1860s)."], ["animalcules"], src=SRC + " slide 3")
q("HIS-01", "not", 1, "Which of the following is NOT a cellular organism?",
  ["A yeast", "A bacterium", "A virus", "An alga"], 2,
  "**Virus** không có cấu tạo tế bào (không ribosome, không tự trao đổi chất), chỉ nhân lên trong tế bào chủ. Nấm men và tảo là **nhân thực**, vi khuẩn là **nhân sơ** – đều là tế bào.",
  ["Nấm men là tế bào nhân thực.", "Vi khuẩn là tế bào nhân sơ.", "", "Tảo là nguyên sinh vật nhân thực."], ["virus", "eukaryote"], "Viruses are tiny bacteria", src=SRC + " slide 24")
q("HIS-01", "concept", 2, "A student says: \"If I increase magnification enough, I can always see two very close points separately.\" Why is this wrong?",
  ["Magnification makes the image darker", "Separating two close points depends on resolution, which has a physical limit", "Only electron microscopes magnify images", "Resolution depends only on the eyepiece"], 1,
  "Phân biệt hai điểm gần nhau là **độ phân giải (resolution)**, bị giới hạn vật lý (~0,2 μm với kính quang học). Phóng đại thêm mà không tăng độ phân giải chỉ cho ảnh to mà mờ.",
  ["Không phải lý do chính.", "", "Kính quang học cũng phóng đại.", "Độ phân giải phụ thuộc chủ yếu vật kính và bước sóng ánh sáng."], ["resolution"], "Magnification equals resolution")
q("HIS-01", "concept", 1, "Which pair is correctly matched with its cell type?",
  ["Yeast – prokaryote", "Archaea – eukaryote", "Molds – eukaryote", "Bacteria – eukaryote"], 2,
  "Nấm mốc (molds) và nấm men đều là **nấm – nhân thực**. Bacteria và Archaea là **nhân sơ**.",
  ["Nấm men là nhân thực.", "Archaea là nhân sơ.", "", "Vi khuẩn là nhân sơ."], ["prokaryote", "eukaryote"])
q("HIS-01", "recall", 1, "Which group of microbes includes protozoa, algae, oomycetes and slime molds in the course's classification?",
  ["Fungi", "Protists", "Archaea", "Viruses"], 1,
  "Slide 24: **Protists** gồm protozoa, algae (tảo), oomycetes và slime molds (nấm nhầy). Fungi gồm yeasts, molds và nấm lớn.",
  ["Fungi gồm nấm men, nấm mốc, nấm lớn.", "", "Archaea là nhân sơ.", "Virus không có tế bào."], ["protist"], pool="mock", src=SRC + " slide 24")
q("HIS-01", "not", 1, "Which statement about Leeuwenhoek is NOT correct?",
  ["He made single-lens microscopes", "He described \"animalcules\"", "He sent letters to the Royal Society", "He proposed the germ theory of disease"], 3,
  "Thuyết mầm bệnh gắn với **Pasteur và Koch** (thời kỳ vàng). Leeuwenhoek chỉ quan sát và mô tả, không đưa ra thuyết gây bệnh.",
  ["Đúng: kính một thấu kính.", "Đúng: animalcules.", "Đúng: thư gửi Royal Society 1673–1723.", ""], ["germ theory"], pool="mock")
q("HIS-01", "application", 2, "A virus about 100 nm in diameter must be observed. Which instrument is required and why?",
  ["A light microscope, because oil immersion gives 1000× magnification", "An electron microscope, because 100 nm is below the ~0.2 μm resolution limit of light microscopes", "A hand lens, because viruses are large", "A light microscope with a stronger eyepiece"], 1,
  "100 nm = 0,1 μm < giới hạn phân giải ~0,2 μm của kính quang học → cần **kính hiển vi điện tử**. Thêm thị kính mạnh chỉ tăng phóng đại, không tăng độ phân giải.",
  ["1000× không vượt được giới hạn phân giải.", "", "Virus rất nhỏ.", "Thị kính mạnh hơn = phóng đại rỗng."], ["resolution", "virus"], pool="mock")

v("HIS-01", "microorganism", "vi sinh vật", "An organism too small to be seen clearly with the naked eye.", "Bacteria, yeasts and protozoa are microorganisms.", ["microorganisms", "microbe", "microbes"])
v("HIS-01", "animalcules", "\"động vật li ti\" (tên Leeuwenhoek gọi vi sinh vật)", "Leeuwenhoek's word for the living microbes he saw.", "Leeuwenhoek described animalcules in rainwater.", ["animalcule"])
v("HIS-01", "cell theory", "học thuyết tế bào", "All living things are composed of cells, and cells arise from pre-existing cells.", "Hooke's cork observation opened the way to the cell theory.")
v("HIS-01", "prokaryote", "sinh vật nhân sơ", "A cell without a membrane-bound nucleus (bacteria, archaea).", "E. coli is a prokaryote.", ["prokaryotes", "prokaryotic"])
v("HIS-01", "eukaryote", "sinh vật nhân thực", "A cell with a membrane-bound nucleus and organelles.", "Yeasts and molds are eukaryotes.", ["eukaryotes", "eukaryotic"])
v("HIS-01", "resolution", "độ phân giải", "The ability of a lens to distinguish two close points as separate.", "The resolution of a light microscope is about 0.2 μm.", ["resolving power"])
v("HIS-01", "virus", "virus", "An acellular infectious particle that replicates only inside a host cell.", "A virus has no ribosomes.", ["viruses"])

fc("HIS-01", "fact", "Who named \"cells\" and in what year?", "Robert Hooke, 1665 (cork slices).")
fc("HIS-01", "fact", "Who first observed living microorganisms?", "Anton van Leeuwenhoek, 1673 – \"animalcules\" (single-lens microscope).")
fc("HIS-01", "number", "Resolution limit of a light microscope?", "About 0.2 μm (200 nm).")
fc("HIS-01", "trap", "TRUE/FALSE: Hooke saw living bacteria in cork.", "FALSE – he saw empty cell walls of dead cork cells.")

# ---------------------------------------------------------------- HIS-02
unit("HIS-02", "Spontaneous generation versus biogenesis", "H", 2, 20, SRC + ": slides 8–11",
"""Bạn nấu nồi canh, để quên ngoài bếp 2 ngày thì canh đục và bốc mùi. Người thế kỷ 18 giải thích: vi sinh vật **tự sinh ra từ nước canh**. Người khác cãi: chúng **bay từ không khí vào**. Làm sao thiết kế một thí nghiệm mà **vẫn cho không khí vào** nhưng **không cho vi sinh vật vào**?""",
("Pasteur's swan-neck (S-neck) flask stayed clear for a long time even though it was open to the air. Why?",
 ["The broth was sealed so no air entered", "Dust and microbes were trapped in the curved neck", "Boiling destroyed the \"vital force\" in air", "The broth contained an antibiotic"], 1,
 "Cổ cong cho **không khí đi qua** nhưng **giữ bụi mang vi sinh vật** ở chỗ uốn. Không khí vẫn vào mà dịch không đục → không khí không tự sinh ra vi sinh vật."),
[
("1. Hai thuyết đối lập", """
- **Spontaneous generation** (thuyết tự sinh / abiogenesis): sự sống có thể phát sinh từ vật không sống. Ví dụ slide 8: cóc, rắn, chuột sinh ra từ đất ẩm; ruồi từ phân; **dòi từ xác thối**.
- **Biogenesis** (thuyết sinh học / "sinh từ sinh"): tế bào sống chỉ sinh ra từ **tế bào sống có trước**. Khái niệm do **Rudolf Virchow (1858, Đức)** đưa ra (slide 10).
"""),
("2. Redi (1668) – thí nghiệm dòi", """
**Francesco Redi** (Ý) đặt thịt vào:
| Bình | Kết quả |
|---|---|
| Mở | ruồi đậu, **có dòi** |
| Đậy kín | **không dòi** |
| Đậy **gạc** (không khí qua được, ruồi không vào) | **không dòi** trên thịt (trứng ruồi đẻ trên gạc) |

→ Dòi đến từ **trứng ruồi**, không tự sinh. **Nhưng** nhiều nhà khoa học vẫn tin **vi sinh vật** đủ đơn giản để tự sinh từ vật không sống (slide 8).
"""),
("3. Needham (1745) và Spallanzani (1765)", """
- **John Needham** (Anh, 1745): đun nóng **nước dùng gà và ngô**, rót vào bình **đậy nắp**. Nguội một thời gian → dịch **đục** (vi sinh vật mọc). Needham kết luận: vi sinh vật **tự sinh từ nước dùng**.
- **Lazzaro Spallanzani** (Ý, 1765): cho rằng vi sinh vật từ **không khí** đã lọt vào sau khi đun. Ông đun dịch **sau khi hàn kín** bình → **không mọc**.
- Needham phản bác: nhiệt đã **phá hủy "sinh lực" (vital force)** cần cho tự sinh, và việc hàn kín **ngăn không khí** mang sinh lực vào.

→ Tranh cãi chưa kết thúc vì thí nghiệm của Spallanzani **loại cả không khí**.
"""),
("4. Virchow (1858) và Pasteur (1861) – kết thúc tranh luận", """
- **Virchow (1858)**: đề xuất **biogenesis** – tế bào chỉ sinh ra từ tế bào. Tranh luận kéo dài tới 1861.
- **Louis Pasteur (Pháp, 1861)** chứng minh: vi sinh vật **có trong không khí** có thể làm nhiễm dịch đã tiệt trùng; **bản thân không khí không tạo ra vi sinh vật**.
  - Thí nghiệm bình **cổ ngắn** chứa dịch chiết thịt bò: đun sôi → để hở → **nhiễm**.
  - Thí nghiệm bình **cổ dài uốn cong (S-shaped / swan-neck flask)** (Hình 1.3): đun sôi dịch trong bình rồi uốn cổ → không khí vào tự do nhưng **bụi và vi sinh vật bị giữ ở chỗ cong** → dịch **trong suốt nhiều năm**. Nếu **nghiêng bình** cho dịch chạm chỗ cong (hoặc bẻ cổ) → dịch **đục** trong vài ngày.

**Sức mạnh của thiết kế**: bác bỏ luận điểm "thiếu không khí" của Needham, vì không khí vẫn vào.
"""),
("5. Ý nghĩa", """
- Là nền tảng của **kỹ thuật vô trùng (aseptic technique)**: dụng cụ, môi trường phải tiệt trùng và ngăn nhiễm từ không khí, tay, bụi.
- Mở ra **thời kỳ vàng** của vi sinh vật học (1857–1914).
- Giới hạn: Pasteur bác bỏ tự sinh **trong điều kiện ngày nay**; không nói gì về nguồn gốc sự sống đầu tiên trên Trái Đất hàng tỉ năm trước.
"""),
],
[
("Thực tế phòng lab: vì sao bạn phải hơ miệng ống nghiệm?", """
Khi cấy vi sinh, bạn hơ miệng ống qua đèn cồn, mở nắp nghiêng, thao tác gần ngọn lửa – tất cả nhằm **ngăn vi sinh vật trong không khí/bụi rơi vào**, đúng bài học của Pasteur. Nút bông trên bình tam giác cũng hoạt động như "cổ cong": cho khí trao đổi, giữ bụi.
"""),
("Thực tế công nghiệp", """
Nồi lên men công nghiệp dùng **bộ lọc khí vô trùng (0,2 μm)** cho khí sục vào: không khí vào được, vi sinh vật bị giữ lại – "bình cổ cong" hiện đại. Đồ hộp bị phồng là do vi sinh vật **còn sống sót hoặc lọt vào sau** xử lý nhiệt, chứ không phải tự sinh.
"""),
],
[
("Spontaneous generation vs biogenesis", "**Spontaneous generation**: life arises from nonliving matter. **Biogenesis** (Virchow, 1858): living cells arise only from preexisting living cells.", "Tự sinh vs sinh từ sinh."),
("Redi, Needham, Spallanzani", "**Redi (1668)**: gauze-covered meat had no maggots → maggots come from fly eggs. **Needham (1745)**: heated broth in covered flasks became turbid → claimed spontaneous generation. **Spallanzani (1765)**: broth heated after sealing stayed clear; Needham replied that heat destroyed the \"vital force\".", "Needham ủng hộ tự sinh; Spallanzani phản bác."),
("Pasteur, 1861", "**Pasteur** boiled beef broth in **S-shaped (swan-neck) flasks**. Air entered freely but microbes were trapped in the neck, so the broth stayed sterile. Tilting the flask contaminated it. Conclusion: microbes come from the air, **air itself does not generate them**.", "Cổ cong giữ bụi, không khí vẫn vào."),
],
["Pasteur sealed the flask", "Needham supported biogenesis", "Redi settled the question for microbes", "Virchow did the swan-neck experiment"])

q("HIS-02", "recall", 1, "Who introduced the concept of biogenesis in 1858, stating that living cells arise only from preexisting living cells?",
  ["Louis Pasteur", "Rudolf Virchow", "John Needham", "Francesco Redi"], 1,
  "Slide 10: **Rudolf Virchow (1858)** đưa ra khái niệm **biogenesis**. Pasteur (1861) mới là người giải quyết dứt điểm tranh luận bằng thực nghiệm.",
  ["Pasteur chứng minh bằng thực nghiệm năm 1861.", "", "Needham ủng hộ tự sinh.", "Redi làm thí nghiệm dòi 1668."], ["biogenesis"], "Virchow did the swan-neck experiment", src=SRC + " slide 10")
q("HIS-02", "concept", 2, "Needham heated broth, poured it into covered flasks and saw it become turbid. Spallanzani repeated the work by heating broth AFTER sealing the flask, and it stayed clear. How did Needham respond?",
  ["He accepted biogenesis", "He argued that heat destroyed a \"vital force\" and sealing kept it out", "He argued the broth contained spores", "He argued that Spallanzani used the wrong broth"], 1,
  "Needham cho rằng nhiệt **phá hủy \"sinh lực\" (vital force)** và việc hàn kín **ngăn không khí** mang sinh lực → nên không tự sinh được. Vì vậy cần một thí nghiệm **vẫn cho không khí vào** – chính là bình cổ cong của Pasteur.",
  ["Needham không chấp nhận.", "", "Khái niệm nội bào tử chưa được biết lúc đó.", "Không phải lập luận của Needham."], ["spontaneous generation"], src=SRC + " slide 9")
q("HIS-02", "concept", 2, "What was the key advantage of Pasteur's S-shaped flask over Spallanzani's sealed flask?",
  ["It allowed air in while trapping dust and microbes", "It reached a higher temperature", "It kept the broth free of oxygen", "It contained a disinfectant in the neck"], 0,
  "Cổ cong **cho không khí vào** nhưng **giữ bụi mang vi sinh vật**. Như vậy lập luận \"thiếu không khí/sinh lực\" bị loại bỏ.",
  ["", "Nhiệt độ không phải điểm khác biệt quyết định.", "Không khí (có O₂) vẫn vào.", "Không có hóa chất sát khuẩn."], ["swan-neck flask"], "Pasteur sealed the flask", src=SRC + " slides 10–11")
q("HIS-02", "application", 2, "A swan-neck flask of sterile broth has stayed clear for a year. The flask is tilted so the broth touches the curved neck and is set upright again. What happens and why?",
  ["It stays clear because air cannot carry microbes", "It becomes turbid because microbes trapped in the neck enter the broth", "It stays clear because the broth was boiled", "It becomes turbid because the broth generates life spontaneously"], 1,
  "Vi sinh vật bám ở đoạn cổ cong được dịch cuốn vào → dịch **đục** sau vài ngày. Điều này chứng minh nguồn vi sinh vật là **bụi/không khí**, không phải tự sinh.",
  ["Không khí mang bụi có vi sinh vật.", "", "Đun sôi không ngăn tái nhiễm.", "Đây là cách giải thích của thuyết tự sinh – bị bác bỏ."], ["swan-neck flask"], src=SRC + " slide 11")
q("HIS-02", "recall", 1, "Redi's maggot experiment (1668) showed that:",
  ["microorganisms arise from broth", "maggots come from fly eggs, not from rotting meat", "air contains a vital force", "heat kills all microbes"], 1,
  "Thịt đậy gạc (ruồi không chạm) không có dòi → **dòi từ trứng ruồi**. Tuy nhiên nhiều người vẫn tin **vi sinh vật** có thể tự sinh.",
  ["Không liên quan Redi.", "", "Đây là lập luận của Needham.", "Không phải kết luận của Redi."], ["spontaneous generation"], "Redi settled the question for microbes", src=SRC + " slide 8")
q("HIS-02", "not", 2, "Which statement about the spontaneous generation debate is NOT correct?",
  ["Redi's work did not convince everyone that microbes could not arise spontaneously", "Needham supported spontaneous generation", "Pasteur's flasks were hermetically sealed so no air could enter", "The debate was resolved by Pasteur in 1861"], 2,
  "Bình Pasteur **không bị hàn kín** – cổ bình để hở, uốn cong. Đây chính là điểm khác Spallanzani.",
  ["Đúng: vẫn nhiều người tin vi sinh vật tự sinh.", "Đúng.", "", "Đúng theo slide 10."], ["swan-neck flask"], "Pasteur sealed the flask")
q("HIS-02", "concept", 2, "Which idea was Pasteur's experiment designed to rule out that Spallanzani's experiment could NOT rule out?",
  ["That microbes come from the broth itself because air is required", "That heat kills microbes", "That fly eggs produce maggots", "That microbes cause disease"], 0,
  "Spallanzani hàn kín nên người ủng hộ tự sinh bảo \"thiếu không khí\". Pasteur để **không khí vào tự do** mà dịch vẫn vô trùng → loại bỏ luận điểm đó.",
  ["", "Không phải điểm tranh cãi.", "Thí nghiệm của Redi.", "Thuyết mầm bệnh là chủ đề khác."], ["spontaneous generation"], pool="mock")
q("HIS-02", "recall", 1, "Which scientist argued that microorganisms from the air entered Needham's broth after heating?",
  ["Virchow", "Spallanzani", "Hooke", "Koch"], 1,
  "**Spallanzani (1765)** cho rằng vi sinh vật từ không khí lọt vào dịch của Needham sau khi đun; ông đun sau khi hàn kín và không thấy mọc.",
  ["Virchow đưa khái niệm biogenesis.", "", "Hooke: cork cells.", "Koch: định đề gây bệnh."], [], pool="mock", src=SRC + " slide 9")
q("HIS-02", "application", 2, "Industrial fermenters receive air through sterile 0.2 μm filters. Which historical experiment used the same principle?",
  ["Redi's gauze-covered jar", "Pasteur's swan-neck flask", "Koch's anthrax experiment", "Jenner's vaccination"], 1,
  "Bộ lọc khí vô trùng cho **khí đi qua nhưng giữ vi sinh vật** – giống cổ cong của Pasteur. (Gạc của Redi giữ ruồi, không giữ vi sinh vật.)",
  ["Gạc chỉ ngăn ruồi, kích thước lỗ quá lớn cho vi sinh vật.", "", "Không liên quan.", "Không liên quan."], ["aseptic technique"], pool="mock")

v("HIS-02", "spontaneous generation", "thuyết tự sinh", "The idea that life can arise from nonliving matter.", "Needham believed microbes arose by spontaneous generation.", ["abiogenesis"])
v("HIS-02", "biogenesis", "thuyết sinh học (sự sống sinh từ sự sống)", "Living cells arise only from preexisting living cells (Virchow, 1858).", "Pasteur's flasks supported biogenesis.")
v("HIS-02", "swan-neck flask", "bình cổ cong (cổ thiên nga)", "Pasteur's S-shaped flask that lets air in but traps dust and microbes.", "The broth in the swan-neck flask stayed sterile.", ["S-shaped flask", "S-neck flask"])
v("HIS-02", "vital force", "sinh lực", "A hypothetical force in air that supporters of spontaneous generation believed was needed for life to arise.", "Needham said heat destroyed the vital force.")
v("HIS-02", "aseptic technique", "kỹ thuật vô trùng", "Procedures that prevent contamination of sterile materials and cultures.", "Flaming the tube mouth is part of aseptic technique.", ["aseptic"])
v("HIS-02", "turbid", "đục (do vi sinh vật mọc)", "Cloudy; in broth it usually indicates microbial growth.", "The broth became turbid after two days.", ["turbidity"])

fc("HIS-02", "fact", "Needham (1745) vs Spallanzani (1765): who supported spontaneous generation?", "Needham. Spallanzani heated broth after sealing and saw no growth.")
fc("HIS-02", "fact", "Who proposed biogenesis and when?", "Rudolf Virchow, 1858.")
fc("HIS-02", "fact", "What did Pasteur's S-neck flask prove (1861)?", "Microbes in air contaminate broth; air itself does not produce microbes.")
fc("HIS-02", "trap", "TRUE/FALSE: Pasteur's flasks were sealed.", "FALSE – open to air; the curved neck trapped dust.")
fc("HIS-02", "fact", "Why did Redi's result not end the debate?", "Many believed microorganisms were simple enough to arise from nonliving matter.")

# ---------------------------------------------------------------- HIS-03
unit("HIS-03", "The Golden Age: fermentation, pasteurization, germ theory and Koch's postulates", "H", 2, 25, SRC + ": slides 12–20",
"""Thế kỷ 19, rượu vang và bia Pháp thường bị **chua** khi vận chuyển xa, gây thiệt hại lớn. Người ta mời **Pasteur** giải quyết. Ông phát hiện: nấm men làm ra rượu, còn **vi khuẩn** làm rượu chua. Giải pháp đơn giản đến bất ngờ: **đun nóng nhẹ** – ngày nay gọi là **pasteurization** (thanh trùng) và vẫn dùng cho sữa bạn uống mỗi sáng.""",
("Pasteurization of beer and wine was designed to:",
 ["make the drink completely sterile", "kill the microbes that cause spoilage without ruining the taste", "add yeast to speed up fermentation", "remove alcohol from the drink"], 1,
 "Thanh trùng là **đun nóng nhẹ**, đủ diệt vi sinh vật gây hỏng mà không làm hỏng hương vị. Nó **không** làm sản phẩm vô trùng hoàn toàn."),
[
("1. Thời kỳ vàng (1857–1914)", """
Sau thí nghiệm của Pasteur, vi sinh vật học **bùng nổ**. Giai đoạn **1857–1914** được gọi là **Golden Age of Microbiology**. Pasteur và **Robert Koch** được xem là người đặt nền móng. Trong giai đoạn này:
- phát hiện **tác nhân gây bệnh (pathogens)** của nhiều bệnh;
- phát hiện vai trò của **miễn dịch** trong phòng và kiểm soát bệnh;
- nghiên cứu **hoạt động hóa học** của vi sinh vật, cải tiến **kính hiển vi** và **kỹ thuật nuôi cấy**, phát triển **vaccine** và **kỹ thuật phẫu thuật**.
"""),
("2. Lên men và thanh trùng (slide 16)", """
- Câu hỏi thực tế: **vì sao rượu vang và bia bị chua?** → cần cách bảo quản đồ uống lên men để vận chuyển xa.
- Trước đó, nhiều nhà khoa học cho rằng không khí biến đường thành rượu (quá trình hóa học thuần túy). Pasteur chứng minh:
  - **Nấm men (yeasts)** biến đường thành **rượu** khi **không có không khí** → **fermentation** (lên men) là quá trình **sinh học**.
  - Bia/rượu **chua và hỏng** là do **các vi khuẩn khác** (ví dụ vi khuẩn tạo **acid acetic** – giấm).
- **Pasteurization**: **đun nóng** đồ uống tới nhiệt độ **đủ diệt vi sinh vật gây hỏng**, nhưng không quá cao để giữ hương vị.
- Ngày nay dùng cho sữa: truyền thống **63 °C/30 phút**, **HTST 72 °C/15 giây**, **UHT 140 °C/<1 giây** (chi tiết ở bài CTL-02).
"""),
("3. Thuyết mầm bệnh (Germ Theory of Disease) – slide 17–18", """
- Trước Pasteur: **không biết tác nhân gây bệnh**, chữa bệnh bằng **thử và sai (trial and error)**.
- Ý tưởng then chốt: nếu **nấm men ↔ lên men**, thì có thể **vi sinh vật ↔ bệnh**.
- Khó được chấp nhận vì người ta tin bệnh do "khí độc" (**miasma**) từ cống rãnh, đầm lầy; khó tin vi sinh vật di chuyển từ nơi khác vào cây/động vật để gây bệnh.
- **1835 – Agostino Bassi**: chứng minh **một loại nấm** gây bệnh trên **tằm (silkworm)**.
- **1865 – Pasteur** được mời chống **bệnh tằm**: ông tìm thấy một tác nhân khác là **động vật nguyên sinh (protozoan)** → xây dựng phương pháp phát hiện tằm bệnh.
"""),
("4. Lister và Koch (slide 19)", """
- **Joseph Lister (Anh, 1860s)**: áp dụng thuyết mầm bệnh vào y khoa – xử lý vết mổ bằng **dung dịch phenol (carbolic acid)** → giảm nhiễm trùng vết mổ; khai sinh **phẫu thuật sát khuẩn (antiseptic surgery)**.
- **Robert Koch (Đức, 1876)**: bằng chứng **đầu tiên** rằng **vi khuẩn gây bệnh**: ***Bacillus anthracis*** gây **bệnh than (anthrax)** giết gia súc ở châu Âu.
  - Koch lấy máu con bệnh, **nuôi** vi khuẩn, **tiêm** vào con khỏe → con khỏe bị bệnh → **phân lập lại** vi khuẩn và **so sánh** với vi khuẩn ban đầu → giống nhau.
  - Từ đó hình thành **Koch's postulates** – chuỗi bước thực nghiệm để liên hệ **một vi sinh vật cụ thể** với **một bệnh cụ thể**.
"""),
("5. Bốn định đề Koch (slide 20, Hình 14.3)", """
1. **Cùng một tác nhân** phải có mặt ở **mọi trường hợp bệnh**.
2. Tác nhân phải được **phân lập** từ vật chủ bệnh và nuôi thành **nuôi cấy thuần (pure culture)**.
3. Tác nhân từ nuôi cấy thuần phải **gây ra cùng bệnh** khi tiêm vào **vật chủ khỏe, cảm thụ**.
4. Tác nhân phải được **phân lập lại** từ vật chủ bị gây bệnh thực nghiệm và **giống** tác nhân ban đầu.

Mẹo nhớ: **Thấy – Tách – Tái hiện – Tìm lại**.

**Ngoại lệ** (hay hỏi): virus, *Treponema pallidum* (giang mai), *Mycobacterium leprae* (phong) **không nuôi cấy được trên môi trường nhân tạo**; một bệnh có thể do nhiều tác nhân (viêm phổi); một tác nhân gây nhiều bệnh (*Streptococcus pyogenes*); người mang mầm bệnh không triệu chứng. [mở rộng]
"""),
],
[
("Thực tế: sữa tươi thanh trùng vs tiệt trùng", """
Hộp sữa **"thanh trùng"** (pasteurized) phải bảo quản lạnh 4 °C và dùng trong ~7–10 ngày; hộp **"tiệt trùng UHT"** để nhiệt độ phòng hàng tháng. Lý do: thanh trùng chỉ diệt tác nhân gây bệnh và phần lớn vi sinh vật gây hỏng, **không diệt nội bào tử**; UHT + đóng gói vô trùng gần như vô trùng thương mại.
"""),
("Mở rộng: định đề Koch phân tử", """
Ngày nay, người ta dùng **định đề Koch phân tử** (Falkow, 1988): gen độc lực phải có ở chủng gây bệnh, bất hoạt gen → mất độc lực, phục hồi gen → phục hồi độc lực. Nhờ đó xác định được tác nhân chưa nuôi cấy được, ví dụ *Helicobacter pylori* gây loét dạ dày (Marshall tự uống vi khuẩn năm 1984 – Nobel 2005).
"""),
("Liên hệ ngành: lên men là nền tảng công nghệ sinh học", """
Phát hiện "nấm men làm ra rượu" của Pasteur là khởi đầu của **công nghiệp lên men**: bia, rượu, bánh mì, và sau này là ethanol nhiên liệu (bài APP-03). Chữ "fermentation" trong công nghiệp được dùng rộng cho mọi quá trình nuôi vi sinh vật quy mô lớn.
"""),
],
[
("Golden Age 1857–1914", "Pasteur and **Robert Koch** founded microbiology. Achievements: discovery of **pathogens**, the role of **immunity**, study of microbial chemistry, better microscopy and **culture techniques**, **vaccines** and surgical techniques.", "Thời kỳ vàng 1857–1914."),
("Fermentation and pasteurization", "Pasteur showed that **yeasts** convert sugar to alcohol without air (**fermentation**) and that **bacteria** cause wine and beer to sour. **Pasteurization** = mild heating that kills spoilage microbes without damaging taste.", "Nấm men → rượu; vi khuẩn → chua; thanh trùng = đun nhẹ."),
("Germ theory milestones", "**Bassi (1835)**: a fungus causes silkworm disease. **Pasteur (1865)**: a protozoan also causes silkworm disease. **Lister (1860s)**: phenol on surgical wounds. **Koch (1876)**: *Bacillus anthracis* causes **anthrax**.", "Bassi nấm; Pasteur protozoa; Lister phenol; Koch bệnh than."),
("Koch's postulates", "1) same pathogen in every case; 2) isolated in **pure culture**; 3) the culture causes the same disease in a healthy susceptible host; 4) the pathogen is **re-isolated** and matches the original.", "Thấy – Tách – Tái hiện – Tìm lại."),
],
["Pasteurization sterilizes", "Koch's postulates apply to every disease", "Lister used alcohol", "Bassi found a protozoan in silkworms"])

q("HIS-03", "recall", 1, "The period from 1857 to 1914 is known as the:",
  ["Age of Discovery", "Golden Age of Microbiology", "Antibiotic Era", "Molecular Age"], 1,
  "Slide 15: **1857–1914 = Golden Age of Microbiology**, do Pasteur và Koch đặt nền móng.",
  ["Không đúng thuật ngữ.", "", "Kỷ nguyên kháng sinh bắt đầu từ 1940s.", "Không đúng."], ["Golden Age of Microbiology"], src=SRC + " slide 15")
q("HIS-03", "concept", 2, "Pasteur discovered that wine and beer became sour because of:",
  ["yeasts growing in the presence of air", "different bacteria that spoil the drinks", "chemical oxidation by air alone", "toxins from the barrels"], 1,
  "Nấm men tạo rượu; **các vi khuẩn khác** làm bia/rượu chua và hỏng (slide 16). Vì vậy giải pháp là đun nhẹ để diệt chúng (**pasteurization**).",
  ["Nấm men tạo rượu, không phải nguyên nhân chính làm chua.", "", "Pasteur chứng minh quá trình là sinh học.", "Không phải kết luận của Pasteur."], ["fermentation", "pasteurization"], src=SRC + " slide 16")
q("HIS-03", "recall", 1, "In 1835, before Pasteur's work on silkworms, Agostino Bassi showed that silkworm disease was caused by:",
  ["a protozoan", "a fungus", "a virus", "a bacterium"], 1,
  "**Bassi (1835)**: một loại **nấm** gây bệnh tằm. Năm 1865 Pasteur tìm ra một tác nhân **khác** là **protozoan**.",
  ["Protozoan là phát hiện của Pasteur.", "", "Virus chưa được biết.", "Không đúng."], ["germ theory"], "Bassi found a protozoan in silkworms", src=SRC + " slide 18")
q("HIS-03", "recall", 1, "Joseph Lister applied the germ theory to medicine by:",
  ["treating surgical wounds with phenol", "vaccinating patients against smallpox", "discovering penicillin", "isolating Bacillus anthracis"], 0,
  "**Lister (1860s)** xử lý vết mổ bằng **phenol (carbolic acid)** → khởi đầu phẫu thuật sát khuẩn.",
  ["", "Jenner.", "Fleming.", "Koch."], ["antisepsis"], "Lister used alcohol", src=SRC + " slide 19")
q("HIS-03", "concept", 2, "In Koch's postulates, why must the pathogen be isolated in PURE culture before being injected into a healthy animal?",
  ["To increase its virulence", "So that the disease produced can be attributed to one specific microbe", "Because mixed cultures cannot grow", "To make a vaccine"], 1,
  "Nuôi cấy **thuần** đảm bảo chỉ có **một loại** vi sinh vật → nếu con vật khỏe bị bệnh thì quy được cho **đúng tác nhân đó**.",
  ["Mục đích không phải tăng độc lực.", "", "Nuôi cấy hỗn hợp vẫn mọc được.", "Không phải mục đích của định đề."], ["pure culture", "Koch's postulates"])
q("HIS-03", "not", 2, "Which is NOT one of Koch's postulates?",
  ["The same pathogen must be present in every case of the disease", "The pathogen must be isolated and grown in pure culture", "The pathogen must be killed by heat before injection", "The pathogen must be re-isolated from the experimentally infected host"], 2,
  "Không có bước \"giết bằng nhiệt\". Tác nhân **sống** từ nuôi cấy thuần được tiêm vào vật chủ khỏe để tái hiện bệnh.",
  ["Định đề 1.", "Định đề 2.", "", "Định đề 4."], ["Koch's postulates"])
q("HIS-03", "application", 3, "A new disease is caused by an agent that cannot be grown on any artificial medium. Which of Koch's postulates cannot be satisfied in the classic way?",
  ["Finding the agent in every case", "Growing the agent in pure culture", "Observing symptoms in the patient", "Comparing symptoms between patients"], 1,
  "Không nuôi cấy trên môi trường nhân tạo → **không lập được nuôi cấy thuần** (định đề 2, kéo theo 3–4). Ví dụ: virus, *Treponema pallidum*, *M. leprae*.",
  ["Vẫn có thể thấy tác nhân.", "", "Không phải định đề.", "Không phải định đề."], ["Koch's postulates", "pure culture"], "Koch's postulates apply to every disease")
q("HIS-03", "recall", 1, "Robert Koch's first proof that a bacterium causes a specific disease (1876) involved:",
  ["Mycobacterium tuberculosis and tuberculosis", "Bacillus anthracis and anthrax", "Vibrio cholerae and cholera", "Treponema pallidum and syphilis"], 1,
  "Slide 19: năm **1876**, Koch chứng minh ***Bacillus anthracis*** gây **bệnh than (anthrax)** ở gia súc.",
  ["Lao là năm 1882.", "", "Tả là năm 1883.", "Giang mai – Ehrlich chữa bằng salvarsan."], ["anthrax"], pool="mock", src=SRC + " slide 19")
q("HIS-03", "not", 2, "Which statement about pasteurization is NOT correct?",
  ["It uses heat", "It was first developed to prevent spoilage of wine and beer", "It kills all microorganisms including endospores", "It aims to preserve the taste of the product"], 2,
  "Thanh trùng **không** tiêu diệt mọi vi sinh vật, đặc biệt **không diệt nội bào tử** – đó là mục tiêu của tiệt trùng (sterilization).",
  ["Đúng.", "Đúng.", "", "Đúng."], ["pasteurization", "sterilization"], "Pasteurization sterilizes", pool="mock")
q("HIS-03", "concept", 2, "Why was the germ theory difficult to accept in the 19th century?",
  ["Microscopes had not been invented", "People believed diseases came from bad air or vapors, and it was hard to believe microbes moved into hosts", "Vaccines had already cured all diseases", "Koch's postulates were rejected by Pasteur"], 1,
  "Slide 18: người ta tin bệnh do **khí độc từ cống, đầm lầy (miasma)** và khó tin vi sinh vật từ nơi khác di chuyển vào cây/động vật gây bệnh.",
  ["Kính hiển vi đã có từ thế kỷ 17.", "", "Sai.", "Sai."], ["germ theory"], pool="mock", src=SRC + " slide 18")
q("HIS-03", "concept", 2, "Pasteur showed that fermentation is:",
  ["a purely chemical reaction caused by air", "a biological process carried out by yeasts in the absence of air", "a process that requires bacteria to produce alcohol", "the same as putrefaction"], 1,
  "Pasteur: **nấm men** chuyển đường thành rượu **khi không có không khí** → lên men là quá trình **sinh học**.",
  ["Quan niệm cũ bị Pasteur bác bỏ.", "", "Vi khuẩn làm chua, nấm men tạo rượu.", "Thối rữa là quá trình khác."], ["fermentation"], pool="mock")

v("HIS-03", "fermentation", "lên men", "Conversion of sugar to products such as alcohol by microbes, originally without air.", "Yeast fermentation produces ethanol and CO2.")
v("HIS-03", "pasteurization", "thanh trùng (pasteur hóa)", "Mild heating that kills spoilage organisms and pathogens without damaging product quality.", "Milk pasteurization uses 72 °C for 15 s.", ["pasteurize", "pasteurized"])
v("HIS-03", "germ theory", "thuyết mầm bệnh", "The theory that microorganisms cause many diseases.", "Koch's work supported the germ theory.", ["germ theory of disease"])
v("HIS-03", "pathogen", "tác nhân gây bệnh", "A microorganism that causes disease.", "Bacillus anthracis is a pathogen.", ["pathogens", "pathogenic"])
v("HIS-03", "Koch's postulates", "các định đề Koch", "Experimental steps that relate a specific microbe to a specific disease.", "Koch's postulates require a pure culture.")
v("HIS-03", "pure culture", "nuôi cấy thuần", "A culture containing only one kind of microorganism.", "A single colony gives a pure culture.")
v("HIS-03", "anthrax", "bệnh than", "Disease caused by Bacillus anthracis.", "Koch linked anthrax to Bacillus anthracis in 1876.")
v("HIS-03", "Golden Age of Microbiology", "thời kỳ vàng của vi sinh vật học", "The period 1857–1914 of rapid discoveries in microbiology.", "Koch's postulates date from the Golden Age of Microbiology.", ["Golden Age"])

fc("HIS-03", "number", "Years of the Golden Age of Microbiology?", "1857–1914.")
fc("HIS-03", "fact", "What did Lister use on surgical wounds?", "Phenol (carbolic acid) solution – 1860s.")
fc("HIS-03", "fact", "Bassi (1835) vs Pasteur (1865): agents of silkworm disease?", "Bassi: a fungus. Pasteur: a protozoan.")
fc("HIS-03", "fact", "Koch's postulates in 4 words?", "Find in every case – isolate (pure culture) – reproduce disease – re-isolate.")
fc("HIS-03", "trap", "TRUE/FALSE: pasteurization kills endospores.", "FALSE – it only kills spoilage organisms and pathogens; it does not sterilize.")

# ---------------------------------------------------------------- HIS-04
unit("HIS-04", "Vaccines and chemotherapy: Jenner, Pasteur, Ehrlich, Fleming", "M", 1, 15, SRC + ": slides 21–22",
"""Năm 1928, **Alexander Fleming** đi nghỉ về và thấy một đĩa nuôi *Staphylococcus* bị **nhiễm mốc xanh**. Xung quanh khuẩn lạc mốc là một **vòng trong** – vi khuẩn không mọc được. Thay vì vứt đi, ông tự hỏi: *mốc này tiết ra chất gì?* Chất đó là **penicillin** – mở ra kỷ nguyên kháng sinh cứu hàng trăm triệu người.""",
("What did Fleming's contaminated plate show?",
 ["The mold killed the bacteria by eating them", "A substance diffusing from the Penicillium mold inhibited bacterial growth", "The bacteria killed the mold", "Heat from the incubator killed the bacteria"], 1,
 "Mốc ***Penicillium*** tiết **penicillin** khuếch tán vào thạch, **ức chế vi khuẩn** tạo vùng trong quanh khuẩn lạc mốc."),
[
("1. Jenner và vaccine (1796)", """
- **Edward Jenner (Anh, 1796)** nhận thấy người vắt sữa bò từng mắc **đậu bò (cowpox)** không mắc **đậu mùa (smallpox)**. Ông lấy dịch từ mụn **đậu bò** cấy cho một cậu bé; sau đó cậu bé **không mắc đậu mùa**.
- Quá trình này gọi là **vaccination** (từ *vacca* = bò). Khả năng cơ thể được bảo vệ khỏi bệnh gọi là **immunity** (miễn dịch).

> ⚠ Slide 21 ghi "dịch từ mụn **đậu mùa**". Theo lịch sử chuẩn, Jenner dùng **đậu bò**; dùng dịch đậu mùa là **variolation** – một thực hành cũ, nguy hiểm hơn. Khi thi, câu hỏi thường hỏi *Jenner → vaccination → immunity*; hãy nhớ bản chất đó.
"""),
("2. Pasteur và cơ chế vaccine (1880)", """
- **Pasteur (1880)** phát hiện: vi khuẩn **tả gà (chicken cholera)** nuôi **lâu ngày trong phòng thí nghiệm** mất khả năng gây bệnh (**giảm độc lực – attenuation**) nhưng **vẫn tạo được miễn dịch**.
- Pasteur gọi các chế phẩm này là **vaccines** để vinh danh Jenner.
- Về sau: vaccine bệnh than (1881), dại (1885).
"""),
("3. Hóa trị liệu – Ehrlich và \"viên đạn thần kỳ\"", """
- **Chemotherapy**: điều trị bệnh bằng hóa chất.
- **Paul Ehrlich (Đức, 1910)**: tìm ra **salvarsan** – một dẫn xuất **arsenic** có tác dụng chống ***Treponema pallidum***, vi khuẩn gây **giang mai (syphilis)**. Ý tưởng **"magic bullet"**: chất diệt mầm bệnh mà không hại vật chủ → **độc tính chọn lọc (selective toxicity)**.
- **Sau 1930**: nhiều hợp chất ức chế vi sinh vật gây bệnh được tìm thấy, **phần lớn là dẫn xuất của thuốc nhuộm**; **sulfonamides** (sulfa drugs) được tổng hợp trong giai đoạn này.

Phân biệt: **synthetic drugs** (tổng hợp hóa học: salvarsan, sulfonamide) vs **antibiotics** (chất do vi sinh vật tạo ra: penicillin).
"""),
("4. Fleming và penicillin (1928)", """
- **Alexander Fleming (Scotland, 1928)** phát hiện nấm ***Penicillium notatum*** (nay gọi ***P. chrysogenum***) **ức chế sự phát triển của vi khuẩn**. Hợp chất được gọi là **penicillin**.
- Penicillin được **sản xuất công nghiệp sau 1940** (Florey và Chain tinh chế; sản xuất bằng lên men chìm – bài APP-04).
- Nhờ phát hiện này, **hàng nghìn kháng sinh khác** được tìm thấy.
- **Mặt trái**: nhiều kháng sinh **độc với người và động vật**; xuất hiện **vi sinh vật kháng kháng sinh (antibiotic-resistant microorganisms)**.
"""),
("5. Bảng tổng hợp slide 21–22", """
| Người | Năm | Đóng góp | Từ khóa |
|---|---|---|---|
| Jenner | 1796 | vaccine đậu mùa | vaccination, immunity |
| Pasteur | 1880 | vi khuẩn tả gà giảm độc lực vẫn tạo miễn dịch | attenuated vaccine |
| Ehrlich | 1910 | salvarsan (arsenic) chữa giang mai | chemotherapy, magic bullet |
| (sau 1930) | 1930s | dẫn xuất thuốc nhuộm, sulfonamides | synthetic drugs |
| Fleming | 1928 | penicillin từ *Penicillium notatum/chrysogenum* | antibiotic |
"""),
],
[
("Thực tế: kháng kháng sinh (AMR)", """
WHO xếp **kháng kháng sinh** là một trong 10 mối đe dọa sức khỏe toàn cầu. Dùng kháng sinh khi bị cảm cúm (do virus) không có tác dụng mà còn **chọn lọc** vi khuẩn kháng thuốc. Vi khuẩn kháng penicillin thường tiết **β-lactamase** cắt vòng β-lactam – liên hệ bài BAC-03 (penicillin ức chế transpeptidase).
"""),
("Liên hệ bài học sau", """
- Penicillin tác động vào **peptidoglycan** → vì sao Gram dương nhạy hơn Gram âm (BAC-03, BAC-04).
- Sản xuất penicillin công nghiệp là **chất chuyển hóa bậc 2** bằng lên men fed-batch (APP-04).
- Vaccine hiện đại: bất hoạt, giảm độc lực, tiểu đơn vị, mRNA (vaccine COVID-19) – cùng nguyên lý **tạo trí nhớ miễn dịch** mà Jenner khởi đầu.
"""),
],
[
("Jenner 1796", "Edward **Jenner** protected people against **smallpox** with material from cowpox lesions. The process is **vaccination**; the protection is **immunity**. (The slide says smallpox blisters; historically it was cowpox.)", "Jenner → vaccination → immunity."),
("Pasteur 1880", "Chicken cholera bacteria kept in the lab for a long time lost their ability to cause disease (**attenuated**) but still induced immunity. Pasteur called them **vaccines**.", "Vi khuẩn giảm độc lực vẫn tạo miễn dịch."),
("Ehrlich and Fleming", "**Ehrlich (1910)**: **salvarsan**, an arsenic derivative active against the syphilis bacterium. After 1930: dye derivatives and **sulfonamides**. **Fleming (1928)**: *Penicillium notatum (chrysogenum)* inhibits bacteria → **penicillin**, industrial after 1940. Problems: toxicity and **antibiotic resistance**.", "Salvarsan – giang mai; penicillin – Fleming 1928."),
],
["Vaccines are antibiotics", "Salvarsan is an antibiotic from a mold", "Antibiotics treat viral infections", "Fleming industrialized penicillin in 1928"])

q("HIS-04", "recall", 1, "Paul Ehrlich's salvarsan (1910), an arsenic derivative, was used to treat:",
  ["tuberculosis", "syphilis", "smallpox", "anthrax"], 1,
  "Slide 22: **salvarsan** (dẫn xuất arsenic) chống vi khuẩn gây **giang mai (syphilis)** – *Treponema pallidum*.",
  ["Không đúng.", "", "Đậu mùa là bệnh virus – Jenner.", "Bệnh than – Koch."], ["chemotherapy"], src=SRC + " slide 22")
q("HIS-04", "recall", 1, "Which organism did Fleming observe inhibiting bacterial growth in 1928?",
  ["Saccharomyces cerevisiae", "Penicillium notatum (P. chrysogenum)", "Aspergillus niger", "Streptomyces griseus"], 1,
  "Fleming (Scotland, 1928) phát hiện nấm ***Penicillium notatum*** (***P. chrysogenum***) ức chế vi khuẩn → **penicillin**.",
  ["Nấm men làm bánh mì/rượu.", "", "Dùng sản xuất acid citric.", "Nguồn streptomycin (Waksman)."], ["penicillin"], src=SRC + " slide 22")
q("HIS-04", "concept", 2, "Pasteur found that chicken cholera bacteria cultured in the lab for a long time:",
  ["became more virulent", "lost their ability to cause disease but could still induce immunity", "turned into viruses", "produced penicillin"], 1,
  "Slide 21 (1880): vi khuẩn **mất khả năng gây bệnh** (giảm độc lực – attenuation) nhưng **vẫn gây miễn dịch** → Pasteur gọi là **vaccines**.",
  ["Ngược lại.", "", "Sai.", "Không liên quan."], ["attenuated", "vaccine"], src=SRC + " slide 21")
q("HIS-04", "concept", 2, "What is the main difference between a vaccine and an antibiotic?",
  ["A vaccine kills bacteria directly; an antibiotic stimulates immunity", "A vaccine induces immunity before infection; an antibiotic acts on the microbe to treat infection", "Both are made only from molds", "There is no difference"], 1,
  "Vaccine **huấn luyện hệ miễn dịch** (phòng bệnh); kháng sinh **tác động lên vi khuẩn** (điều trị). Hai cơ chế khác nhau.",
  ["Đảo ngược.", "", "Sai.", "Sai."], ["vaccine", "antibiotic"], "Vaccines are antibiotics")
q("HIS-04", "not", 2, "Which statement about antibiotics after Fleming's discovery is NOT correct?",
  ["Penicillin was produced on an industrial scale after 1940", "Thousands of other antibiotics were discovered", "All antibiotics are harmless to humans and animals", "Antibiotic-resistant microorganisms appeared"], 2,
  "Slide 22: nhiều kháng sinh **độc với người và động vật**, và vi sinh vật **kháng kháng sinh** đã xuất hiện.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["antibiotic resistance"])
q("HIS-04", "recall", 1, "Jenner's work in 1796 is regarded as the origin of:",
  ["pasteurization", "vaccination", "chemotherapy", "aseptic surgery"], 1,
  "**Jenner (1796)** → **vaccination**; sự bảo vệ cơ thể nhờ vaccine gọi là **immunity**.",
  ["Pasteur.", "", "Ehrlich.", "Lister."], ["vaccination", "immunity"], pool="mock", src=SRC + " slide 21")
q("HIS-04", "concept", 2, "Salvarsan and sulfonamides differ from penicillin because they are:",
  ["produced by bacteria", "synthetic chemicals rather than substances produced by microorganisms", "vaccines", "effective only against viruses"], 1,
  "Salvarsan (arsenic) và sulfonamide là **thuốc tổng hợp hóa học**. Penicillin là **kháng sinh** – chất do vi sinh vật (nấm *Penicillium*) tạo ra.",
  ["Sai.", "", "Sai.", "Sai."], ["antibiotic", "chemotherapy"], "Salvarsan is an antibiotic from a mold", pool="mock")
q("HIS-04", "application", 2, "A patient with influenza (a viral infection) asks for penicillin. Based on how penicillin works, what is the best response?",
  ["Penicillin will cure influenza quickly", "Penicillin targets bacterial cell walls, which viruses do not have, so it will not treat influenza", "Penicillin works only if injected", "Penicillin is a vaccine against influenza"], 1,
  "Penicillin ức chế tổng hợp **peptidoglycan** của vi khuẩn; virus **không có thành tế bào** → vô tác dụng, lại còn chọn lọc vi khuẩn kháng thuốc.",
  ["Sai.", "", "Đường dùng không phải vấn đề.", "Penicillin không phải vaccine."], ["penicillin", "virus"], "Antibiotics treat viral infections", pool="mock")

v("HIS-04", "vaccination", "chủng ngừa, tiêm vaccine", "Inducing immunity by exposing the body to a harmless form of a pathogen.", "Jenner's vaccination protected against smallpox.", ["vaccinate"])
v("HIS-04", "vaccine", "vaccine", "A preparation that induces immunity to a disease.", "Pasteur's attenuated cultures were vaccines.", ["vaccines"])
v("HIS-04", "immunity", "miễn dịch", "The body's ability to resist a specific disease.", "Vaccination produces immunity.")
v("HIS-04", "attenuated", "giảm độc lực", "Weakened so it no longer causes disease but still induces immunity.", "Old cholera cultures became attenuated.", ["attenuation"])
v("HIS-04", "chemotherapy", "hóa trị liệu", "Treatment of disease with chemical substances.", "Salvarsan was an early chemotherapy agent.")
v("HIS-04", "antibiotic", "kháng sinh", "A substance produced by a microorganism that inhibits other microorganisms.", "Penicillin is an antibiotic.", ["antibiotics"])
v("HIS-04", "penicillin", "penicillin", "A β-lactam antibiotic from Penicillium that blocks peptidoglycan cross-linking.", "Penicillin was industrialized after 1940.")
v("HIS-04", "antibiotic resistance", "kháng kháng sinh", "The ability of microbes to survive an antibiotic.", "Overuse of drugs selects for antibiotic resistance.", ["antibiotic-resistant"])
v("HIS-04", "selective toxicity", "độc tính chọn lọc", "Harming the microbe without harming the host.", "Ehrlich's magic bullet relied on selective toxicity.", ["magic bullet"])

fc("HIS-04", "fact", "Ehrlich 1910: drug and disease?", "Salvarsan (arsenic derivative) against syphilis.")
fc("HIS-04", "fact", "Fleming 1928: organism and product?", "Penicillium notatum (P. chrysogenum) → penicillin; industrial after 1940.")
fc("HIS-04", "fact", "Pasteur 1880 vaccine principle?", "Chicken cholera bacteria cultured long in the lab lost virulence but still gave immunity.")
fc("HIS-04", "fact", "Two drug groups found after 1930?", "Dye derivatives and sulfonamides (synthetic).")
fc("HIS-04", "trap", "TRUE/FALSE: antibiotics can cure the flu.", "FALSE – influenza is viral; antibiotics act on bacterial targets.")
