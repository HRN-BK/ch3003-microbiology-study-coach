from _lib import *

SRC = "2-3.Bacteria.pptx"

# ---------------------------------------------------------------- BAC-01
unit("BAC-01", "Size, shape and arrangement of bacteria", "H", 1, 20, SRC + ": slides 1–11",
"""Nhìn tiêu bản nhuộm Gram mủ viêm họng, bác sĩ thấy **cầu khuẩn xếp thành chuỗi** như chuỗi hạt; tiêu bản mụn nhọt lại thấy **cầu khuẩn xếp thành chùm** như chùm nho. Chỉ từ **cách sắp xếp** đã gợi ý hai chi khác nhau: *Streptococcus* và *Staphylococcus*. Cách sắp xếp đến từ đâu?""",
("Why do streptococci form chains while staphylococci form grape-like clusters?",
 ["They have different cell wall colors", "Cells divide in one plane and stay attached (chains) versus divide in multiple random planes (clusters)", "Streptococci are rods", "Staphylococci have flagella"], 1,
 "Cách sắp xếp phụ thuộc **mặt phẳng phân chia** và việc tế bào con **còn dính nhau**: một mặt phẳng → chuỗi (strepto-); nhiều mặt phẳng ngẫu nhiên → chùm (staphylo-)."),
[
("1. Kích thước", """
- Phần lớn vi khuẩn: đường kính **0,2–2,0 μm**, dài **2–8 μm** [fig]. Nhỏ hơn nhiều so với tế bào nhân thực (10–100 μm).
- Slide 3: thang kích thước từ virus (nm) → vi khuẩn (μm) → tế bào nhân thực.
- Tỉ lệ **diện tích bề mặt/thể tích** lớn giúp vi khuẩn trao đổi chất nhanh → sinh trưởng nhanh. [mở rộng]
"""),
("2. Ba hình dạng cơ bản", """
| Hình dạng | Tên | Ví dụ |
|---|---|---|
| Hình cầu | **coccus** (số nhiều cocci) – cầu khuẩn | *Staphylococcus, Streptococcus* |
| Hình que | **bacillus** (bacilli) – trực khuẩn | *E. coli, Bacillus* |
| Xoắn | **spiral** – xoắn khuẩn | *Vibrio, Spirillum, Treponema* |

Ba dạng xoắn (slide 1 ghi chú "Spirillum & spirochete: xoắn khuẩn"):
- **Vibrio**: que **cong** như dấu phẩy (*Vibrio cholerae*).
- **Spirillum**: xoắn **cứng**, di chuyển bằng **roi ngoài** giống cánh quạt.
- **Spirochete**: xoắn **mềm dẻo**, di chuyển bằng **sợi trục (axial filament)** nằm dưới vỏ ngoài (*Treponema pallidum, Borrelia*).

Hình dạng khác: **hình sao** (*Stella*), **hình vuông/phẳng** (*Haloarcula* – một archaea). Phần lớn vi khuẩn **đơn hình (monomorphic)**; một số **đa hình (pleomorphic)** như *Rhizobium, Corynebacterium*.

> Chú ý chính tả: **bacillus** (viết thường) = hình que; ***Bacillus*** (viết hoa, in nghiêng) = **tên một chi**.
"""),
("3. Cách sắp xếp của cầu khuẩn", """
| Kiểu | Cách phân chia | Hình ảnh |
|---|---|---|
| **Diplococci** | 1 mặt phẳng, dính 2 tế bào | đôi (*Neisseria*) |
| **Streptococci** | 1 mặt phẳng, dính thành chuỗi | chuỗi hạt |
| **Tetrad** | 2 mặt phẳng vuông góc | nhóm 4 |
| **Sarcinae** | 3 mặt phẳng vuông góc | khối lập phương 8 tế bào |
| **Staphylococci** | nhiều mặt phẳng ngẫu nhiên | chùm nho |
"""),
("4. Cách sắp xếp của trực khuẩn", """
- Trực khuẩn chỉ phân chia theo **mặt phẳng ngang** (vuông góc trục dài) → ít kiểu sắp xếp hơn.
- **Single bacillus** (đơn), **diplobacilli** (đôi), **streptobacilli** (chuỗi), **coccobacillus** (que rất ngắn, gần giống cầu).
- Hình dạng + sắp xếp là **đặc điểm kiểu hình**, dùng hỗ trợ định danh (bài IDT-01), nhưng **không đủ** để xác định loài.
"""),
],
[
("Thực tế lâm sàng", """
- Nhuộm Gram mủ thấy **Gram dương, cầu khuẩn chùm** → nghĩ tới *Staphylococcus aureus*; **song cầu Gram âm hình hạt cà phê** trong tế bào bạch cầu → nghĩ tới *Neisseria gonorrhoeae*.
- Đây là bước định danh sơ bộ nhanh nhất (vài phút), trước khi có kết quả nuôi cấy (1–2 ngày).
"""),
("Công nghệ thực phẩm", """
*Streptococcus thermophilus* (cầu khuẩn chuỗi) và *Lactobacillus bulgaricus* (trực khuẩn) cùng lên men sữa chua. Nhìn tiêu bản sữa chua dưới kính, bạn thấy **cả chuỗi cầu và que** – kiểm tra tỷ lệ hai loài là một chỉ tiêu chất lượng.
"""),
],
[
("Basic shapes", "**Coccus** (spherical), **bacillus** (rod), **spiral**. Spirals: **vibrio** (curved rod), **spirillum** (rigid helix, external flagella), **spirochete** (flexible helix, **axial filaments**). Most bacteria are **monomorphic**; some are **pleomorphic**.", "Cầu, que, xoắn; xoắn khuẩn có vibrio, spirillum, spirochete."),
("Arrangements of cocci", "Division in one plane → **diplococci** or **streptococci** (chains). Two planes → **tetrads**. Three planes → **sarcinae** (cubes of 8). Random planes → **staphylococci** (clusters).", "Mặt phẳng phân chia quyết định cách sắp xếp."),
("Arrangements of bacilli", "Bacilli divide only across the short axis: single, **diplobacilli**, **streptobacilli**, **coccobacilli**. Note: *Bacillus* (genus) ≠ bacillus (shape).", "Trực khuẩn: đơn, đôi, chuỗi, cầu trực."),
],
["bacillus shape = Bacillus genus", "Spirilla move with axial filaments", "Arrangement identifies species"])

q("BAC-01", "recall", 1, "Cocci that divide in three perpendicular planes and remain attached form:",
  ["tetrads", "sarcinae", "staphylococci", "streptococci"], 1,
  "Ba mặt phẳng vuông góc → khối lập phương 8 tế bào = **sarcinae**. Hai mặt phẳng → tetrad; ngẫu nhiên → staphylococci; một mặt phẳng → chuỗi.",
  ["Tetrad: 2 mặt phẳng.", "", "Staphylococci: mặt phẳng ngẫu nhiên.", "Streptococci: 1 mặt phẳng, chuỗi."], ["sarcinae", "tetrad"], src=SRC + " slides 6–8")
q("BAC-01", "concept", 2, "Which feature distinguishes a spirillum from a spirochete?",
  ["Spirilla are curved rods; spirochetes are cocci", "Spirilla are rigid helices moved by external flagella; spirochetes are flexible helices moved by axial filaments", "Spirilla are Gram-positive; spirochetes lack a cell wall", "There is no difference"], 1,
  "**Spirillum**: xoắn cứng, **roi ngoài**. **Spirochete**: xoắn mềm, **sợi trục (axial filament)** dưới vỏ ngoài.",
  ["Que cong là vibrio.", "", "Không phải tiêu chí phân biệt.", "Có khác biệt rõ."], ["spirillum", "spirochete", "axial filament"], "Spirilla move with axial filaments", src=SRC + " slides 9–10")
q("BAC-01", "recall", 1, "A comma-shaped (curved rod) bacterium such as the cholera agent is called a:",
  ["vibrio", "spirillum", "coccobacillus", "sarcina"], 0,
  "Que cong như dấu phẩy = **vibrio** (*Vibrio cholerae*).",
  ["", "Spirillum xoắn nhiều vòng, cứng.", "Coccobacillus là que rất ngắn.", "Sarcina là khối cầu khuẩn."], ["vibrio"])
q("BAC-01", "not", 1, "Which of the following is NOT a typical arrangement of bacilli?",
  ["Diplobacilli", "Streptobacilli", "Sarcinae", "Single bacillus"], 2,
  "**Sarcinae** là cách sắp xếp của **cầu khuẩn** (3 mặt phẳng). Trực khuẩn chỉ chia theo mặt phẳng ngang → đơn, đôi, chuỗi.",
  ["Đúng là của trực khuẩn.", "Đúng là của trực khuẩn.", "", "Đúng là của trực khuẩn."], ["sarcinae"])
q("BAC-01", "concept", 2, "A lab report says \"Gram-positive bacilli, genus Bacillus\". A student writes \"all rod-shaped bacteria belong to Bacillus\". What is the error?",
  ["Rods are always Gram-negative", "\"bacillus\" describes a shape, while Bacillus is one genus; many genera are rod-shaped", "Bacillus is a coccus", "Genus names are never capitalized"], 1,
  "**bacillus** (thường) = hình que; ***Bacillus*** (hoa, nghiêng) = một chi. *E. coli, Clostridium, Lactobacillus* đều hình que nhưng không thuộc chi *Bacillus*.",
  ["Sai: có que Gram dương.", "", "Sai.", "Tên chi luôn viết hoa."], ["bacillus"], "bacillus shape = Bacillus genus")
q("BAC-01", "application", 2, "A Gram stain of pus shows spherical cells in irregular grape-like clusters. Which arrangement term and likely genus fit best?",
  ["Streptococci – Streptococcus", "Staphylococci – Staphylococcus", "Diplococci – Neisseria", "Sarcinae – Sarcina"], 1,
  "Chùm nho = phân chia theo **nhiều mặt phẳng ngẫu nhiên** = **staphylococci**, gợi ý chi *Staphylococcus*. Tuy vậy cần thêm xét nghiệm để xác định loài.",
  ["Streptococci tạo chuỗi.", "", "Diplococci là đôi.", "Sarcinae là khối 8."], ["staphylococci"], "Arrangement identifies species", pool="mock")
q("BAC-01", "recall", 1, "Bacteria that can take several shapes (e.g., Rhizobium, Corynebacterium) are described as:",
  ["monomorphic", "pleomorphic", "coccobacilli", "filamentous"], 1,
  "**Pleomorphic** = đa hình. Phần lớn vi khuẩn là **monomorphic** (một hình dạng).",
  ["Ngược nghĩa.", "", "Là một hình dạng cụ thể.", "Không đúng."], ["pleomorphic"], pool="mock")
q("BAC-01", "concept", 2, "Cocci dividing in two perpendicular planes that remain attached form:",
  ["diplococci", "tetrads", "sarcinae", "streptococci"], 1,
  "Hai mặt phẳng vuông góc → nhóm **4 tế bào (tetrad)**.",
  ["Diplococci: 1 mặt phẳng, 2 tế bào.", "", "Sarcinae: 3 mặt phẳng.", "Streptococci: 1 mặt phẳng, chuỗi."], ["tetrad"], pool="mock")

v("BAC-01", "coccus", "cầu khuẩn", "A spherical bacterium.", "Staphylococcus is a coccus.", ["cocci"])
v("BAC-01", "bacillus", "trực khuẩn (hình que)", "A rod-shaped bacterium (shape term, lowercase).", "E. coli is a bacillus but not in the genus Bacillus.", ["bacilli"])
v("BAC-01", "vibrio", "phẩy khuẩn", "A curved, comma-shaped rod.", "Vibrio cholerae is a vibrio.")
v("BAC-01", "spirillum", "xoắn khuẩn cứng", "A rigid helical bacterium that moves with external flagella.", "A spirillum has a corkscrew shape.", ["spirilla"])
v("BAC-01", "spirochete", "xoắn khuẩn mềm (xoắn thể)", "A flexible helical bacterium that moves with axial filaments.", "Treponema pallidum is a spirochete.", ["spirochetes"])
v("BAC-01", "staphylococci", "tụ cầu (cầu khuẩn chùm)", "Cocci arranged in grape-like clusters.", "Staphylococci divide in random planes.", ["staphylococcus"])
v("BAC-01", "streptococci", "liên cầu (cầu khuẩn chuỗi)", "Cocci arranged in chains.", "Streptococci divide in one plane.", ["streptococcus"])
v("BAC-01", "tetrad", "tứ cầu", "Four cocci formed by division in two planes.", "Micrococcus may form tetrads.", ["tetrads"])
v("BAC-01", "sarcinae", "bát cầu (khối 8)", "Cube-like packets of eight cocci formed by division in three planes.", "Sarcinae look like cubes.", ["sarcina"])
v("BAC-01", "pleomorphic", "đa hình", "Able to take many shapes.", "Corynebacterium is pleomorphic.", ["monomorphic"])

fc("BAC-01", "number", "Typical size of a bacterium?", "0.2–2.0 μm in diameter, 2–8 μm long.")
fc("BAC-01", "fact", "Division planes → arrangement of cocci?", "1 plane: diplo/strepto; 2 planes: tetrad; 3 planes: sarcinae; random: staphylo.")
fc("BAC-01", "fact", "Vibrio vs spirillum vs spirochete?", "Curved rod / rigid helix with external flagella / flexible helix with axial filaments.")
fc("BAC-01", "trap", "TRUE/FALSE: every rod-shaped bacterium is in the genus Bacillus.", "FALSE – bacillus is a shape; Bacillus is one genus.")

# ---------------------------------------------------------------- BAC-02
unit("BAC-02", "Glycocalyx, flagella and archaella, axial filaments, fimbriae and pili", "H", 2, 25, SRC + ": slides 13–22",
"""Mảng bám trên răng (**dental plaque**) thật ra là một **biofilm**: hàng tỉ vi khuẩn *Streptococcus mutans* dính vào men răng nhờ một lớp **đường nhầy** do chính chúng tiết ra. Súc miệng thôi không đủ, phải **chải** (tác động cơ học). Lớp nhầy đó là gì và vì sao nó giúp vi khuẩn gây bệnh?""",
("Encapsulated Streptococcus pneumoniae causes pneumonia, while mutant strains without capsules are easily destroyed. What does the capsule mainly do?",
 ["Makes the cell move faster", "Protects the bacterium from phagocytosis by host cells", "Carries out photosynthesis", "Transfers DNA to other cells"], 1,
 "Vỏ nhầy (**capsule**) giúp vi khuẩn **tránh bị thực bào** → tăng **độc lực (virulence)**. Chủng mất capsule bị bạch cầu tiêu diệt dễ dàng."),
[
("1. Glycocalyx: capsule và slime layer (slide 15)", """
**Glycocalyx** là lớp polymer **nhớt, dạng gel** nằm **bên ngoài thành tế bào**, gồm **polysaccharide, polypeptide hoặc cả hai**.
- **Capsule** (vỏ nhầy): tổ chức chặt, bám chắc vào thành.
- **Slime layer** (lớp nhầy): lỏng lẻo, không tổ chức.

**Vai trò:**
- **Độc lực (virulence)** – mức độ gây bệnh: capsule giúp tránh **thực bào (phagocytosis)**. Ví dụ slide: ***Streptococcus pneumoniae, Bacillus anthracis, Streptococcus mutans, Klebsiella pneumoniae***.
- Thành phần quan trọng của **biofilm**. Glycocalyx giúp tế bào bám vào bề mặt và vào nhau gọi là **EPS (extracellular polymeric substance)**. EPS **bảo vệ** tế bào bên trong, **giúp chúng giao tiếp** và **sống sót** nhờ bám vào nhiều bề mặt.
- Giữ nước, chống khô; dự trữ dinh dưỡng. [fig]
"""),
("2. Roi (flagella) – cấu tạo và vận động", """
**Flagella** (số ít flagellum): phần phụ dài, mảnh giúp vi khuẩn **di chuyển**. Ba phần [fig]:
| Phần | Mô tả |
|---|---|
| **Filament** (sợi) | dài nhất, làm từ protein **flagellin** |
| **Hook** (móc) | nối sợi với thân |
| **Basal body** (thể gốc) | neo roi vào thành và màng bằng các **vòng (rings)**; là "động cơ" quay |

**Kiểu phân bố roi** [fig]:
- **Monotrichous**: 1 roi ở một cực (polar).
- **Amphitrichous**: roi ở **hai đầu**.
- **Lophotrichous**: **chùm** roi ở một đầu.
- **Peritrichous**: roi **khắp bề mặt** (*E. coli, Salmonella*).
- **Atrichous**: không roi.

**Cơ chế:** roi **quay** như chân vịt (xoay ngược chiều kim đồng hồ → **run** bơi thẳng; xoay cùng chiều → **tumble** lộn vòng đổi hướng). Di chuyển hướng tới/xa kích thích gọi là **taxis**: **chemotaxis** (hóa chất), **phototaxis** (ánh sáng).

Protein roi là **kháng nguyên H** – dùng phân biệt chủng, ví dụ ***E. coli* O157:H7**. [mở rộng]
"""),
("3. Archaella (slide 16–18)", """
**Archaella** (số ít archaellum) là cấu trúc vận động của **Archaea**: cũng quay như roi nhưng **khác cấu trúc và nguồn gốc**:
| | Flagellum (Bacteria) | Archaellum (Archaea) |
|---|---|---|
| Protein | flagellin | archaellin (glycoprotein) |
| Năng lượng quay | lực proton (proton motive force) | **ATP** |
| Kênh rỗng giữa sợi | có | **không** |
"""),
("4. Sợi trục – axial filaments (slide 19)", """
- Còn gọi **endoflagella**: bó sợi **nằm dưới vỏ ngoài (outer sheath)**, bám ở hai đầu tế bào, quấn quanh tế bào của **xoắn thể (spirochetes)**.
- Có **cấu trúc giống roi**; sự **quay của sợi** làm vỏ ngoài chuyển động → tế bào di chuyển kiểu **xoắn ốc** (như cái mở nút chai).
- Ví dụ: ***Treponema pallidum*** – **giang mai (syphilis)**; ***Borrelia burgdorferi*** – **bệnh Lyme**.
"""),
("5. Fimbriae và pili (slide 20–22)", """
| | **Fimbriae** (tiêm mao / lông bám) | **Pili** (lông giới tính) |
|---|---|---|
| Hình dạng | ngắn, thẳng, mảnh hơn roi | thường **dài hơn** fimbriae |
| Số lượng | nhiều (vài đến vài trăm) | chỉ **1 hoặc 2** mỗi tế bào |
| Protein | **pilin** | pilin |
| Chức năng | **bám dính (attachment)** vào bề mặt, tế bào chủ | **nối hai tế bào** chuẩn bị **chuyển DNA** (tiếp hợp – conjugation); còn giúp vận động giật (twitching), trượt (gliding) |
| Ví dụ | *E. coli*, *Neisseria gonorrhoeae* (lậu) | pilus giới tính F ở *E. coli* |

- Slide 20: nếu **đột biến mất fimbriae**, vi khuẩn **không gây bệnh được** (vì không bám được vào mô chủ) → fimbriae là **yếu tố độc lực**.
- Fimbriae/pili **không dùng để bơi** như roi.
"""),
],
[
("Biofilm trong đời sống", """
- Biofilm có mặt ở: mảng bám răng, ống thông tiểu, van tim nhân tạo, kính áp tròng, đường ống nước, màng lọc công nghiệp.
- Vi khuẩn trong biofilm **chịu kháng sinh và chất khử trùng gấp 10–1000 lần** tế bào trôi nổi → khó điều trị nhiễm trùng thiết bị y tế.
- Trong công nghệ môi trường, biofilm lại **có lợi**: bể lọc sinh học, đĩa quay sinh học xử lý nước thải.
"""),
("Kháng nguyên O và H", """
Chủng *E. coli* **O157:H7** gây tiêu chảy ra máu: **O157** là kháng nguyên từ chuỗi đường O của LPS (bài BAC-04), **H7** là kháng nguyên roi. Cách gọi tên này dùng trong kiểm nghiệm an toàn thực phẩm.
"""),
],
[
("Glycocalyx", "A viscous, gelatinous polymer **outside the cell wall**, made of polysaccharide, polypeptide or both. **Capsule** = organized and firmly attached; **slime layer** = loose. Capsules protect pathogens from **phagocytosis** (virulence): *S. pneumoniae, B. anthracis, S. mutans, K. pneumoniae*. In biofilms it is called **EPS**.", "Capsule → tránh thực bào; EPS → biofilm."),
("Flagella", "Filament (**flagellin**) + hook + basal body. Arrangements: **monotrichous, amphitrichous, lophotrichous, peritrichous**. Flagella rotate (run and tumble) and allow **taxis**. Archaea have **archaella** (ATP-driven, different structure).", "Roi quay; 4 kiểu phân bố."),
("Axial filaments", "Bundles of **endoflagella** under an outer sheath of **spirochetes** (*Treponema pallidum*: syphilis; *Borrelia burgdorferi*: Lyme disease). Rotation moves the sheath and produces a corkscrew motion.", "Sợi trục của xoắn thể."),
("Fimbriae vs pili", "**Fimbriae**: many, short, thin, made of **pilin**, used for **attachment**; mutants without fimbriae cannot cause disease. **Pili**: longer, only **1–2 per cell**, join two cells for **DNA transfer** (conjugation).", "Fimbriae bám; pili chuyển DNA."),
],
["Fimbriae are for swimming", "Pili are numerous", "Capsule is inside the cell wall", "Archaella are bacterial flagella"])

q("BAC-02", "recall", 1, "The glycocalyx of bacteria is located:",
  ["inside the plasma membrane", "external to the cell wall", "between the two membranes of Gram-negative cells", "inside the nucleoid"], 1,
  "Slide 15: glycocalyx là polymer nhớt **bên ngoài thành tế bào**.",
  ["Đó là tế bào chất.", "", "Đó là vùng chu chất.", "Sai."], ["glycocalyx"], "Capsule is inside the cell wall", src=SRC + " slide 15")
q("BAC-02", "concept", 2, "How does a capsule increase the virulence of Streptococcus pneumoniae?",
  ["It produces toxins", "It protects the bacterium from phagocytosis by host cells", "It allows the cell to swim toward nutrients", "It transfers resistance genes"], 1,
  "Capsule che bề mặt vi khuẩn khiến bạch cầu **khó thực bào** → vi khuẩn sống sót và gây bệnh.",
  ["Capsule không phải độc tố.", "", "Đó là roi.", "Đó là pili/plasmid."], ["capsule", "virulence", "phagocytosis"], src=SRC + " slide 15")
q("BAC-02", "recall", 1, "A bacterium with a tuft of flagella at one end is described as:",
  ["monotrichous", "amphitrichous", "lophotrichous", "peritrichous"], 2,
  "**Lophotrichous** = chùm roi ở một đầu. Mono = 1 roi; amphi = hai đầu; peri = khắp bề mặt.",
  ["1 roi.", "Roi ở hai đầu.", "", "Roi khắp bề mặt."], ["flagella"])
q("BAC-02", "concept", 2, "Which statement correctly contrasts fimbriae and pili?",
  ["Fimbriae are used for swimming; pili for attachment", "Fimbriae are numerous and used for attachment; pili are few (1–2) and join cells for DNA transfer", "Both are made of flagellin", "Pili are shorter than fimbriae"], 1,
  "Slide 20–21: **fimbriae** nhiều, ngắn, dùng **bám**; **pili** 1–2/tế bào, dài hơn, nối tế bào để **chuyển DNA**.",
  ["Không cái nào dùng để bơi như roi.", "", "Chúng làm từ pilin.", "Ngược lại."], ["fimbriae", "pili", "conjugation"], "Fimbriae are for swimming")
q("BAC-02", "application", 2, "A mutant of Neisseria gonorrhoeae cannot produce fimbriae. What is the most likely consequence?",
  ["It cannot swim", "It cannot attach to host mucous membranes and fails to cause disease", "It loses its outer membrane", "It becomes Gram-positive"], 1,
  "Slide 20: fimbriae giúp **bám**; mất fimbriae → **không gây bệnh**.",
  ["Fimbriae không phải cơ quan bơi.", "", "Không liên quan.", "Không liên quan."], ["fimbriae"], src=SRC + " slide 20")
q("BAC-02", "recall", 1, "Treponema pallidum, the cause of syphilis, moves by means of:",
  ["peritrichous flagella", "axial filaments", "fimbriae", "a capsule"], 1,
  "Xoắn thể (spirochetes) như *T. pallidum* và *Borrelia burgdorferi* di chuyển bằng **sợi trục (axial filaments)** dưới vỏ ngoài.",
  ["Không phải.", "", "Fimbriae để bám.", "Capsule không dùng để di chuyển."], ["axial filament", "spirochete"], src=SRC + " slide 19")
q("BAC-02", "concept", 2, "In a biofilm, the glycocalyx that helps cells attach to surfaces and to each other is called EPS. Which is NOT a function of EPS stated in the lecture?",
  ["Protects cells within it", "Facilitates communication among cells", "Carries out protein synthesis", "Helps cells survive by attaching to surfaces"], 2,
  "EPS bảo vệ, giúp giao tiếp và giúp bám sống sót. **Tổng hợp protein** là việc của **ribosome**, không phải EPS.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["EPS", "biofilm"], src=SRC + " slide 15")
q("BAC-02", "not", 2, "Which statement about archaella is NOT correct?",
  ["They are motility structures of archaea", "They rotate like flagella", "They are identical in structure to bacterial flagella", "They are powered by ATP"], 2,
  "Archaella **khác** roi vi khuẩn về protein, nguồn năng lượng (ATP) và cấu trúc (không có kênh rỗng).",
  ["Đúng.", "Đúng.", "", "Đúng."], ["archaella"], "Archaella are bacterial flagella", pool="mock")
q("BAC-02", "recall", 1, "The protein that makes up the filament of a bacterial flagellum is:",
  ["pilin", "flagellin", "tubulin", "actin"], 1,
  "Sợi roi làm từ **flagellin**. **Pilin** tạo fimbriae/pili; tubulin là roi nhân thực.",
  ["Pilin là của fimbriae/pili.", "", "Tubulin: vi ống nhân thực.", "Actin: vi sợi nhân thực."], ["flagella"], pool="mock")
q("BAC-02", "application", 2, "A bacterium swims straight for a while, then tumbles and changes direction; runs become longer when it moves toward glucose. This behavior is:",
  ["phototaxis", "chemotaxis", "conjugation", "phagocytosis"], 1,
  "Di chuyển theo gradient **hóa chất** = **chemotaxis**, thực hiện nhờ luân phiên **run–tumble** của roi.",
  ["Phototaxis: theo ánh sáng.", "", "Tiếp hợp: chuyển DNA.", "Thực bào: tế bào chủ nuốt vi khuẩn."], ["taxis"], pool="mock")
q("BAC-02", "not", 2, "Which bacterium is NOT listed in the lecture as using a capsule to avoid phagocytosis?",
  ["Streptococcus pneumoniae", "Klebsiella pneumoniae", "Bacillus anthracis", "Treponema pallidum"], 3,
  "Slide 15 liệt kê *S. pneumoniae, B. anthracis, S. mutans, K. pneumoniae*. ***T. pallidum*** được nêu với **sợi trục**.",
  ["Có trong danh sách.", "Có trong danh sách.", "Có trong danh sách.", ""], ["capsule"], pool="mock")

v("BAC-02", "glycocalyx", "lớp glycocalyx (lớp vỏ đường ngoài)", "A sticky polysaccharide/polypeptide layer outside the cell wall.", "The glycocalyx helps bacteria stick to teeth.")
v("BAC-02", "capsule", "vỏ nhầy (bao)", "An organized glycocalyx firmly attached to the cell wall.", "The capsule protects S. pneumoniae from phagocytosis.", ["capsules"])
v("BAC-02", "slime layer", "lớp nhầy", "An unorganized, loosely attached glycocalyx.", "A slime layer is easily washed off.")
v("BAC-02", "biofilm", "màng sinh học", "A community of microbes attached to a surface within an extracellular matrix.", "Dental plaque is a biofilm.", ["biofilms"])
v("BAC-02", "EPS", "chất polymer ngoại bào", "Extracellular polymeric substance; the glycocalyx of a biofilm.", "EPS protects cells within a biofilm.", ["extracellular polymeric substance"])
v("BAC-02", "virulence", "độc lực", "The degree to which a pathogen causes disease.", "Capsules increase virulence.")
v("BAC-02", "phagocytosis", "thực bào", "Engulfment of particles or microbes by a cell such as a white blood cell.", "Capsules resist phagocytosis.")
v("BAC-02", "flagella", "roi (tiên mao)", "Long rotating appendages that propel bacteria.", "Peritrichous flagella cover E. coli.", ["flagellum", "peritrichous", "monotrichous", "lophotrichous", "amphitrichous"])
v("BAC-02", "archaella", "roi của vi khuẩn cổ", "ATP-driven rotating motility structures of archaea.", "Archaella differ from bacterial flagella.", ["archaellum"])
v("BAC-02", "axial filament", "sợi trục", "Endoflagella under the outer sheath of spirochetes.", "Axial filaments give spirochetes a corkscrew motion.", ["axial filaments", "endoflagella"])
v("BAC-02", "fimbriae", "tiêm mao (lông bám)", "Short, numerous, hairlike appendages used for attachment.", "Fimbriae help N. gonorrhoeae attach.", ["fimbria"])
v("BAC-02", "pili", "lông giới tính (pilus)", "Longer appendages (1–2 per cell) that join cells for DNA transfer.", "A pilus connects two cells before conjugation.", ["pilus", "sex pilus"])
v("BAC-02", "taxis", "tính hướng (hóa hướng động…)", "Movement toward or away from a stimulus.", "Chemotaxis is a type of taxis.", ["chemotaxis", "phototaxis"])

fc("BAC-02", "fact", "Capsule vs slime layer?", "Capsule: organized, firmly attached. Slime layer: unorganized, loose.")
fc("BAC-02", "fact", "Four bacteria given as capsule examples?", "Streptococcus pneumoniae, Bacillus anthracis, Streptococcus mutans, Klebsiella pneumoniae.")
fc("BAC-02", "fact", "Three parts of a flagellum?", "Filament (flagellin), hook, basal body.")
fc("BAC-02", "number", "How many pili per cell (lecture)?", "Only 1 or 2.")
fc("BAC-02", "trap", "TRUE/FALSE: fimbriae are used for swimming.", "FALSE – attachment. Flagella swim; axial filaments give corkscrew motion.")

# ---------------------------------------------------------------- BAC-03
unit("BAC-03", "Peptidoglycan and the Gram-positive cell wall", "H", 2, 25, SRC + ": slides 23–37",
"""Nước mắt của bạn chứa **lysozyme**, còn thuốc **penicillin** thì do nấm tạo ra. Cả hai đều giết vi khuẩn nhưng **không làm hại tế bào người**. Bí mật: cả hai tấn công cùng một mục tiêu mà tế bào người **không có** – mạng lưới **peptidoglycan** của thành tế bào vi khuẩn.""",
("Why does penicillin harm bacteria but not human cells?",
 ["Human cells have thicker cell walls", "It targets peptidoglycan synthesis, and human cells have no peptidoglycan", "It targets 80S ribosomes", "It dissolves all lipid membranes"], 1,
 "Penicillin ức chế enzyme tạo liên kết chéo **peptidoglycan**; tế bào người **không có thành peptidoglycan** → **độc tính chọn lọc**."),
[
("1. Chức năng của thành tế bào", """
- Giữ **hình dạng** tế bào.
- Chống **vỡ do áp suất thẩm thấu**: nồng độ chất tan trong tế bào cao hơn môi trường → nước đi vào → thành chống lại áp lực.
- Điểm neo cho roi.
- Là **đích tác động** của kháng sinh (penicillin) và lysozyme; thành phần thành giúp phân biệt **Gram dương / Gram âm**.
"""),
("2. Cấu trúc peptidoglycan (murein) – slide 28", """
**Peptidoglycan** là mạng lưới gồm:
- **Khung đường (glycan backbone)**: xen kẽ **NAG** (N-acetylglucosamine) và **NAM** (N-acetylmuramic acid), nối bằng liên kết **β-1,4**. Mỗi chuỗi dài **10–65 đơn vị** (slide ghi "10–65 monomers"), các chuỗi xếp **song song**.
- **Chuỗi bên tetrapeptide (side chain)**: 4 amino acid gắn vào **NAM**. Ghi chú slide 3: gồm **L-alanine, D-glutamate, diaminopimelic acid (DAP), D-alanine** – có **D-amino acid** (hiếm gặp ở protein thường).
- **Cầu nối chéo peptide (cross-bridge)**: chuỗi amino acid ngắn nối các tetrapeptide của hai chuỗi kề nhau (ví dụ cầu pentaglycine ở *Staphylococcus aureus*).

Hình dung: khung đường = các sợi dây song song; tetrapeptide + cầu nối = các "nút buộc" tạo lưới.
"""),
("3. Penicillin và lysozyme – hai cách phá thành", """
| | **Penicillin** | **Lysozyme** |
|---|---|---|
| Nguồn | nấm *Penicillium* | nước mắt, nước bọt, lòng trắng trứng |
| Đích | enzyme **transpeptidase** tạo **cầu nối chéo** | **liên kết β-1,4** giữa NAM và NAG |
| Tác động | ngăn **tổng hợp** thành mới → tế bào **đang sinh trưởng** bị vỡ | **cắt** khung đường của thành có sẵn |

- Slide 28: *penicillin inactivates transpeptidase (responsible for cross-bridge synthesis) → breaks down the peptidoglycan layer.*
- Mất thành trong môi trường đẳng trương: Gram dương → **protoplast**; Gram âm (còn màng ngoài) → **spheroplast**. Trong môi trường nhược trương, chúng **vỡ (osmotic lysis)**. [fig]
"""),
("4. Thành tế bào Gram dương (slide 34–37)", """
- **Nhiều lớp peptidoglycan** → thành **dày và chắc**; **nhạy với penicillin** (peptidoglycan lộ ra ngoài, không có màng ngoài che chắn).
- Chứa **teichoic acid** (gồm **rượu – glycerol hoặc ribitol – và phosphate**):
  - **Lipoteichoic acid**: xuyên qua lớp peptidoglycan và **gắn vào màng sinh chất**.
  - **Wall teichoic acid**: gắn vào **lớp peptidoglycan**.
- Teichoic acid **tích điện âm** → có thể **liên kết và điều hòa sự di chuyển của cation** (ion dương) ra vào tế bào; cũng là kháng nguyên giúp định danh. [fig]
- Thành *Streptococcus* chứa **nhiều loại polysaccharide** khác nhau (dùng phân nhóm Lancefield). [mở rộng]
"""),
("5. Mycobacterium – thành giàu acid mycolic", """
- Slide 37: thành ***Mycobacterium*** chứa **60 % mycolic acid** (lipid sáp), phần còn lại là peptidoglycan.
- Lớp sáp khiến thuốc nhuộm Gram khó thấm → dùng **nhuộm kháng acid (acid-fast stain)**: vi khuẩn giữ màu đỏ carbolfuchsin sau khi tẩy bằng cồn-acid.
- Vi khuẩn lao (*M. tuberculosis*) và phong (*M. leprae*); *Nocardia* cũng kháng acid.
- Lớp sáp giúp chống khô, chống nhiều chất sát khuẩn và kháng sinh, sinh trưởng rất chậm.
"""),
],
[
("Thực tế: vì sao β-lactam là \"con cưng\" của ngành dược", """
Penicillin, ampicillin, amoxicillin, cephalosporin đều có **vòng β-lactam** và đều ức chế transpeptidase (còn gọi **penicillin-binding proteins – PBP**). Chúng chiếm hơn 60 % lượng kháng sinh dùng trên thế giới vì độc tính chọn lọc cao. Vi khuẩn kháng lại bằng **β-lactamase** (cắt vòng β-lactam) hoặc thay đổi PBP (tụ cầu vàng kháng methicillin **MRSA**).
"""),
("Công nghệ thực phẩm: lysozyme bảo quản", """
Lysozyme từ lòng trắng trứng được dùng làm chất bảo quản trong **phô mai** (ngăn *Clostridium tyrobutyricum* gây phồng phô mai) và rượu vang – một ứng dụng trực tiếp của kiến thức cấu trúc peptidoglycan.
"""),
],
[
("Peptidoglycan structure", "Backbone of alternating **NAG** and **NAM** linked by **β-1,4** bonds (10–65 units per chain, chains in parallel). A **tetrapeptide side chain** (L-Ala, D-Glu, DAP, D-Ala) is attached to NAM; short **peptide cross-bridges** link side chains.", "NAG–NAM + tetrapeptide + cầu nối."),
("Penicillin vs lysozyme", "**Penicillin** inactivates **transpeptidase**, the enzyme that makes cross-bridges, so new wall cannot be built. **Lysozyme** hydrolyzes the **β-1,4 bond** between NAM and NAG. Without a wall: protoplast (Gram+) or spheroplast (Gram−); in hypotonic media → lysis.", "Penicillin chặn nối chéo; lysozyme cắt khung đường."),
("Gram-positive wall", "**Many layers** of peptidoglycan → thick, strong, **sensitive to penicillin**. **Teichoic acids** (glycerol or ribitol + phosphate): **lipoteichoic acid** spans the wall and links to the plasma membrane; **wall teichoic acid** links to peptidoglycan. Negatively charged → bind and regulate cations.", "Gram dương: dày, có teichoic acid."),
("Mycobacterium", "Wall contains about **60 % mycolic acid** (waxy lipid) and the rest peptidoglycan → **acid-fast**, resistant to drying and many chemicals.", "60 % acid mycolic → kháng acid."),
],
["Lysozyme and penicillin act the same way", "Teichoic acid is in Gram-negative walls", "Human cells have peptidoglycan"])

q("BAC-03", "recall", 1, "The glycan backbone of peptidoglycan consists of alternating:",
  ["glucose and galactose", "NAG and NAM", "NAG and NAT", "glycerol and phosphate"], 1,
  "Khung peptidoglycan: **NAG** (N-acetylglucosamine) và **NAM** (N-acetylmuramic acid) nối β-1,4. **NAT** thay NAM trong pseudomurein của Archaea.",
  ["Sai.", "", "Đây là pseudomurein (Archaea).", "Đây là teichoic acid."], ["peptidoglycan"], src=SRC + " slide 28")
q("BAC-03", "concept", 2, "Penicillin kills growing bacteria because it:",
  ["hydrolyzes the bond between NAM and NAG", "inactivates transpeptidase, preventing formation of peptide cross-bridges", "dissolves the outer membrane", "inhibits 70S ribosomes"], 1,
  "Slide 28: penicillin **bất hoạt transpeptidase** (enzyme tạo cầu nối chéo) → không xây được thành mới → tế bào đang sinh trưởng vỡ.",
  ["Đó là lysozyme.", "", "Không phải cơ chế penicillin.", "Đó là streptomycin/erythromycin."], ["penicillin", "transpeptidase"], "Lysozyme and penicillin act the same way", src=SRC + " slide 28")
q("BAC-03", "concept", 2, "Where is the tetrapeptide side chain attached in peptidoglycan?",
  ["To NAG", "To NAM", "To teichoic acid", "To lipid A"], 1,
  "Tetrapeptide gắn vào **NAM**.",
  ["Sai.", "", "Sai.", "Lipid A thuộc LPS Gram âm."], ["peptidoglycan"])
q("BAC-03", "recall", 1, "Which molecule spans the peptidoglycan layer and is linked to the plasma membrane in Gram-positive bacteria?",
  ["Wall teichoic acid", "Lipoteichoic acid", "Lipopolysaccharide", "Porin"], 1,
  "Slide 34: **lipoteichoic acid** xuyên lớp peptidoglycan và **gắn vào màng sinh chất**; wall teichoic acid gắn vào peptidoglycan.",
  ["Gắn với peptidoglycan, không phải màng.", "", "LPS là của Gram âm.", "Porin là của Gram âm."], ["teichoic acid"], "Teichoic acid is in Gram-negative walls", src=SRC + " slide 34")
q("BAC-03", "concept", 2, "Teichoic acids are negatively charged. According to the lecture, this allows them to:",
  ["bind and regulate the movement of cations into and out of the cell", "block penicillin", "act as endotoxins", "form porins"], 0,
  "Slide 37: tích điện âm → **gắn và điều hòa cation** ra vào tế bào.",
  ["", "Không.", "Nội độc tố là lipid A.", "Không."], ["teichoic acid"], src=SRC + " slide 37")
q("BAC-03", "application", 3, "Gram-positive cells are treated with lysozyme in an isotonic sucrose solution. They become spherical but do not burst. Then they are moved to distilled water. What happens?",
  ["Nothing, because the membrane is intact", "They form protoplasts that now lyse due to osmotic water uptake", "They regrow the wall immediately", "They become Gram-negative"], 1,
  "Lysozyme loại thành → **protoplast** (sống được trong môi trường đẳng trương). Chuyển sang nước cất (nhược trương) → nước vào → **vỡ (osmotic lysis)** vì không còn thành chống áp lực.",
  ["Màng không đủ chống áp suất thẩm thấu.", "", "Không tái tạo tức thì.", "Không."], ["protoplast", "lysozyme"])
q("BAC-03", "recall", 1, "The cell wall of Mycobacterium contains about 60% of:",
  ["teichoic acid", "mycolic acid", "lipopolysaccharide", "chitin"], 1,
  "Slide 37: thành *Mycobacterium* gồm **60 % mycolic acid**, còn lại peptidoglycan → kháng acid.",
  ["Sai.", "", "Sai.", "Chitin ở thành nấm."], ["mycolic acid", "acid-fast"], src=SRC + " slide 37")
q("BAC-03", "not", 2, "Which is NOT a feature of the Gram-positive cell wall?",
  ["Multiple layers of peptidoglycan", "Teichoic acids", "An outer membrane containing LPS", "Sensitivity to penicillin"], 2,
  "Màng ngoài chứa **LPS** là đặc trưng của **Gram âm**.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["lipopolysaccharide"], pool="mock")
q("BAC-03", "concept", 2, "Which amino acid in the peptidoglycan side chain is unusual because it is a D-isomer?",
  ["L-alanine", "D-glutamate", "Glycine", "L-lysine only"], 1,
  "Chuỗi bên: L-Ala, **D-Glu**, DAP, **D-Ala** – có **D-amino acid**, khác protein thông thường. (Pseudomurein của Archaea **không** có D-amino acid.)",
  ["L-Ala là dạng L thông thường.", "", "Glycine không có đồng phân quang học.", "Sai."], ["peptidoglycan"], pool="mock")
q("BAC-03", "application", 2, "Lysozyme in tears protects the eye mainly against which bacteria?",
  ["Gram-positive bacteria, whose peptidoglycan is exposed", "Gram-negative bacteria, whose peptidoglycan is covered by an outer membrane", "Mycoplasma, which lacks a wall", "Viruses"], 0,
  "Lysozyme cắt peptidoglycan; ở **Gram dương** lớp này **lộ ra ngoài** nên dễ bị tấn công. Gram âm có màng ngoài che chắn; Mycoplasma không có thành.",
  ["", "Màng ngoài cản lysozyme.", "Không có đích tác động.", "Virus không có peptidoglycan."], ["lysozyme"], pool="mock")
q("BAC-03", "not", 2, "Which statement about penicillin is NOT correct?",
  ["It targets transpeptidase", "It is most effective against actively growing cells", "It is toxic to human cells because they contain peptidoglycan", "Gram-positive bacteria are generally more sensitive to it"], 2,
  "Tế bào người **không có peptidoglycan** → penicillin có **độc tính chọn lọc**.",
  ["Đúng.", "Đúng.", "", "Đúng (thành dày lộ ra)."], ["penicillin", "selective toxicity"], "Human cells have peptidoglycan", pool="mock")

v("BAC-03", "cell wall", "thành tế bào", "A rigid layer outside the plasma membrane that gives shape and prevents osmotic lysis.", "The bacterial cell wall contains peptidoglycan.")
v("BAC-03", "peptidoglycan", "peptidoglycan (murein)", "A mesh of NAG–NAM chains cross-linked by peptides.", "Gram-positive walls have many layers of peptidoglycan.", ["murein"])
v("BAC-03", "NAG", "N-acetylglucosamine", "One of the two sugars of the peptidoglycan backbone.", "NAG alternates with NAM.", ["N-acetylglucosamine"])
v("BAC-03", "NAM", "N-acetylmuramic acid", "The peptidoglycan sugar that carries the tetrapeptide.", "The tetrapeptide is attached to NAM.", ["N-acetylmuramic acid"])
v("BAC-03", "transpeptidase", "enzyme transpeptidase", "The enzyme that forms peptide cross-bridges; target of penicillin.", "Penicillin inactivates transpeptidase.")
v("BAC-03", "lysozyme", "lysozyme", "An enzyme that hydrolyzes the β-1,4 bond between NAM and NAG.", "Lysozyme in tears attacks peptidoglycan.")
v("BAC-03", "teichoic acid", "acid teichoic", "Polymers of glycerol or ribitol and phosphate in Gram-positive walls.", "Teichoic acids bind cations.", ["teichoic acids", "lipoteichoic acid", "wall teichoic acid"])
v("BAC-03", "mycolic acid", "acid mycolic", "A waxy lipid forming about 60% of the Mycobacterium wall.", "Mycolic acid makes Mycobacterium acid-fast.")
v("BAC-03", "acid-fast", "kháng acid", "Retaining carbolfuchsin after acid-alcohol decolorization.", "Mycobacterium tuberculosis is acid-fast.")
v("BAC-03", "protoplast", "thể nguyên sinh (protoplast)", "A wall-less Gram-positive cell.", "Lysozyme converts Gram-positive cells into protoplasts.", ["spheroplast"])

fc("BAC-03", "fact", "Peptidoglycan backbone and bond?", "Alternating NAG and NAM, β-1,4 glycosidic bonds; 10–65 units per chain.")
fc("BAC-03", "fact", "Four amino acids of the side chain (lecture notes)?", "L-alanine, D-glutamate, diaminopimelic acid (DAP), D-alanine.")
fc("BAC-03", "fact", "Penicillin target?", "Transpeptidase – the enzyme that makes peptide cross-bridges.")
fc("BAC-03", "number", "Mycolic acid content of the Mycobacterium wall?", "About 60%.")
fc("BAC-03", "trap", "TRUE/FALSE: lipoteichoic acid links to peptidoglycan only.", "FALSE – lipoteichoic acid links to the plasma membrane; wall teichoic acid links to peptidoglycan.")

# ---------------------------------------------------------------- BAC-04
unit("BAC-04", "Gram-negative wall, LPS, the Gram stain and atypical walls", "H", 2, 25, SRC + ": slides 26–27, 38–41",
"""Một bệnh nhân nhiễm trùng máu do *E. coli* được tiêm kháng sinh, vi khuẩn chết hàng loạt – nhưng bệnh nhân lại **sốt cao hơn, tụt huyết áp**. Lý do: khi vi khuẩn **Gram âm** chết và vỡ, chúng giải phóng **lipid A** từ màng ngoài – một **nội độc tố (endotoxin)**. Màng ngoài này còn giải thích vì sao Gram âm **khó trị** hơn.""",
("Which part of the Gram-negative outer membrane is the endotoxin?",
 ["Porin", "O polysaccharide", "Lipid A", "Teichoic acid"], 2,
 "**Lipid A** của LPS là **nội độc tố** → sốt, giãn mạch, sốc, đông máu. Được giải phóng khi vi khuẩn Gram âm chết/vỡ."),
[
("1. Cấu tạo thành Gram âm (slide 38–39)", """
Từ trong ra ngoài:
1. **Màng sinh chất** (plasma membrane).
2. **Periplasmic space (vùng chu chất)** – khoảng giữa màng sinh chất và màng ngoài; chứa **nồng độ cao enzyme phân giải và protein vận chuyển**.
3. **Peptidoglycan**: chỉ **một hoặc rất ít lớp**, **mỏng** → dễ tổn thương cơ học; nằm trong vùng chu chất và **liên kết với lipoprotein** (lipid gắn cộng hóa trị với protein) của màng ngoài.
4. **Outer membrane (màng ngoài)**: lipoprotein, **lipopolysaccharide (LPS)**, phospholipid và **porin**.

- **Không có teichoic acid**.
"""),
("2. Màng ngoài – chức năng (slide 40–41)", """
- **Điện tích âm mạnh** → giúp **tránh thực bào** và tránh tác động của **bổ thể (complement)** (hệ protein làm tan tế bào và thúc đẩy thực bào).
- **Hàng rào** ngăn: chất tẩy rửa, **kim loại nặng, muối mật**, một số thuốc nhuộm, **kháng sinh (như penicillin)** và enzyme tiêu hóa như **lysozyme**.
- **Porin**: protein tạo **kênh** cho các phân tử nhỏ đi qua – nucleotide, disaccharide, peptide, amino acid, vitamin B12, sắt…

> Slide 40 ghi porin còn cho "virus và hợp chất nguy hiểm" đi qua. Hiểu đúng: porin cho **các chất tan nhỏ, ưa nước** đi qua (kể cả chất có hại); virus nguyên vẹn thì **quá lớn**, chúng dùng porin như **thụ thể bám** chứ không chui qua.
"""),
("3. LPS – lipopolysaccharide", """
LPS gồm 3 phần [fig]:
| Phần | Vai trò |
|---|---|
| **Lipid A** | neo LPS vào màng ngoài; là **nội độc tố (endotoxin)** → **sốt, giãn mạch máu, sốc, đông máu** ở vật chủ (slide 41) |
| **Core polysaccharide** | lõi đường nối lipid A với chuỗi O |
| **O polysaccharide** | chuỗi đường hướng ra ngoài; là **kháng nguyên O** (ví dụ *E. coli* **O157**) |

Nội độc tố được giải phóng khi vi khuẩn **chết và vỡ** → dùng kháng sinh diệt khuẩn ồ ạt có thể làm triệu chứng nặng lên tạm thời.
"""),
("4. Nhuộm Gram – cơ chế (slide 26–27)", """
| Bước | Hóa chất | Gram dương | Gram âm |
|---|---|---|---|
| 1. Nhuộm chính | **Crystal violet** | tím | tím |
| 2. Cẩn màu | **Iodine** (mordant) → phức CV-I | tím | tím |
| 3. Tẩy màu | **Alcohol / acetone** | **tím** (giữ màu) | **không màu** |
| 4. Nhuộm phụ | **Safranin** (counterstain) | tím | **hồng/đỏ** |

**Vì sao?**
- Gram dương: cồn làm **lớp peptidoglycan dày mất nước, co lại** → phức CV-I **bị giữ lại**.
- Gram âm: cồn **hòa tan màng ngoài (lipid)**, lớp peptidoglycan **mỏng** không giữ được phức CV-I → phức bị rửa trôi → bắt màu safranin.
- **Tế bào già** Gram dương có thể bắt màu như Gram âm (thành bị tổn thương) → nên nhuộm vi khuẩn **non (18–24 h)**. [mở rộng]
"""),
("5. So sánh Gram dương – Gram âm", """
| Đặc điểm | Gram dương | Gram âm |
|---|---|---|
| Peptidoglycan | **dày, nhiều lớp** | **mỏng, 1–vài lớp** |
| Teichoic acid | **có** | **không** |
| Màng ngoài | không | **có** (LPS, porin, lipoprotein) |
| Vùng chu chất | hẹp/không rõ | **có**, nhiều enzyme |
| Nội độc tố (lipid A) | không | **có** |
| Nhạy penicillin, lysozyme | **cao** | **thấp** (màng ngoài cản) |
| Chịu tác động cơ học | tốt | kém |
| Màu Gram | **tím** | **hồng/đỏ** |
"""),
("6. Thành tế bào không điển hình", """
- ***Mycoplasma***: **không có thành tế bào**; màng chứa **sterol** (giúp chống vỡ); rất nhỏ; kháng penicillin tự nhiên.
- **Kháng acid** (*Mycobacterium, Nocardia*): acid mycolic (BAC-03).
- **Archaea**: không có peptidoglycan; có **pseudomurein** hoặc lớp S (BAC-08).
"""),
],
[
("Thực tế: nội độc tố trong dược phẩm", """
Nước tiêm, dịch truyền, vaccine phải kiểm tra **endotoxin** (phép thử **LAL – Limulus Amebocyte Lysate** từ máu cua móng ngựa). Vì lipid A **chịu nhiệt**, hấp tiệt trùng (autoclave) diệt vi khuẩn nhưng **không phá nội độc tố** → phải loại bỏ bằng nhiệt khô 250 °C (depyrogenation) hoặc lọc.
"""),
("Liên hệ: vì sao Gram âm khó trị", """
Màng ngoài + bơm đẩy thuốc (efflux pump) + β-lactamase trong vùng chu chất làm vi khuẩn Gram âm như *Pseudomonas aeruginosa, Klebsiella, Acinetobacter* đứng đầu danh sách vi khuẩn kháng thuốc ưu tiên của WHO. *P. aeruginosa* còn kháng triclosan (bài CTL-04).
"""),
],
[
("Gram-negative wall", "Plasma membrane → **periplasmic space** (degrading enzymes, transport proteins) → **thin peptidoglycan** (one or a few layers, linked to lipoproteins) → **outer membrane** (lipoproteins, **LPS**, phospholipids, **porins**). No teichoic acid.", "Gram âm: peptidoglycan mỏng + màng ngoài."),
("Outer membrane functions", "Strong negative charge helps **evade phagocytosis and complement**. Barrier to detergents, heavy metals, bile salts, some dyes, **antibiotics (penicillin)** and **lysozyme**. **Porins** let small molecules pass (nucleotides, disaccharides, peptides, amino acids, vitamin B12, iron).", "Màng ngoài: hàng rào + porin."),
("LPS", "**Lipid A** (endotoxin → fever, vasodilation, shock, blood clotting), **core polysaccharide**, **O polysaccharide** (O antigen, e.g., O157).", "Lipid A = nội độc tố."),
("Gram stain", "Crystal violet → iodine (mordant) → **alcohol decolorizes** → safranin. Gram+: thick peptidoglycan dehydrates and traps CV-I → **purple**. Gram−: alcohol dissolves the outer membrane; thin wall loses CV-I → **pink/red**.", "Tím = Gram dương; hồng = Gram âm."),
],
["Gram-negative has thicker peptidoglycan", "Porins transport whole viruses", "Endotoxin is released from living cells only", "Safranin stains only Gram-negatives"])

q("BAC-04", "recall", 1, "Lipid A of Gram-negative bacteria is important medically because it:",
  ["is a capsule that prevents phagocytosis", "is an endotoxin causing fever, vasodilation, shock and blood clotting", "is the target of penicillin", "forms porins"], 1,
  "Slide 41: **lipid A là nội độc tố** → sốt, giãn mạch, sốc, đông máu.",
  ["Capsule là glycocalyx.", "", "Đích của penicillin là transpeptidase.", "Porin là protein."], ["lipid A", "endotoxin"], src=SRC + " slide 41")
q("BAC-04", "concept", 2, "During the Gram stain, what makes Gram-negative cells lose the crystal violet–iodine complex?",
  ["Iodine cannot enter Gram-negative cells", "Alcohol dissolves the outer membrane and the thin peptidoglycan cannot retain the complex", "Safranin displaces crystal violet", "Gram-negative cells have no plasma membrane"], 1,
  "Cồn **hòa tan lipid màng ngoài**, lớp peptidoglycan **mỏng** không giữ phức CV-I → mất màu → bắt safranin (hồng).",
  ["Iodine vào được cả hai.", "", "Safranin nhuộm cả hai, nhưng tím đậm che màu ở Gram dương.", "Sai."], ["Gram stain"], "Safranin stains only Gram-negatives")
q("BAC-04", "recall", 1, "The periplasmic space of Gram-negative bacteria contains high concentrations of:",
  ["teichoic acids", "degrading enzymes and transport proteins", "ribosomes", "mycolic acid"], 1,
  "Slide 38: vùng chu chất chứa **nhiều enzyme phân giải và protein vận chuyển**.",
  ["Teichoic acid ở Gram dương.", "", "Ribosome ở tế bào chất.", "Acid mycolic ở Mycobacterium."], ["periplasmic space"], src=SRC + " slide 38")
q("BAC-04", "not", 2, "Which substance is NOT listed as being blocked by the Gram-negative outer membrane?",
  ["Bile salts", "Lysozyme", "Penicillin", "Small nutrients passing through porins"], 3,
  "Chất dinh dưỡng nhỏ **đi qua porin** (nucleotide, amino acid, vitamin B12, sắt…). Muối mật, lysozyme, penicillin, chất tẩy, kim loại nặng bị cản.",
  ["Bị cản.", "Bị cản.", "Bị cản.", ""], ["outer membrane", "porin"], src=SRC + " slides 40–41")
q("BAC-04", "concept", 2, "Why are Gram-negative bacteria generally more sensitive to mechanical breakage than Gram-positive bacteria?",
  ["They lack a plasma membrane", "Their peptidoglycan layer is thin", "They have teichoic acid", "They have no LPS"], 1,
  "Slide 39: peptidoglycan **mỏng** → **nhạy tác động cơ học**.",
  ["Có màng sinh chất.", "", "Gram âm không có teichoic acid.", "Có LPS."], ["peptidoglycan"], "Gram-negative has thicker peptidoglycan", src=SRC + " slide 39")
q("BAC-04", "application", 2, "A student Gram-stains a 5-day-old culture of a Gram-positive Bacillus and sees many pink cells. The most likely explanation is:",
  ["The organism changed to Gram-negative", "Old cells have damaged walls that no longer retain crystal violet", "Safranin was omitted", "Iodine was added twice"], 1,
  "Tế bào **già** có thành tổn thương → không giữ phức CV-I → bắt màu hồng giả. Nên nhuộm tế bào non 18–24 h.",
  ["Phản ứng Gram gắn với cấu trúc thành, không \"đổi loài\".", "", "Nếu bỏ safranin, tế bào mất màu sẽ không màu, không hồng.", "Không gây mất màu."], ["Gram stain"])
q("BAC-04", "concept", 2, "The O polysaccharide of LPS is useful in the laboratory because it:",
  ["acts as an antigen that distinguishes strains (e.g., E. coli O157)", "anchors LPS in the membrane", "is the endotoxin", "forms the peptide cross-bridge"], 0,
  "Chuỗi **O** là **kháng nguyên O** dùng phân biệt serotype, ví dụ *E. coli* **O157**:H7.",
  ["", "Đó là lipid A.", "Đó là lipid A.", "Sai."], ["lipopolysaccharide"], pool="mock")
q("BAC-04", "not", 2, "Which is NOT a component of the Gram-negative outer membrane?",
  ["Lipopolysaccharide", "Porins", "Lipoproteins", "Teichoic acid"], 3,
  "**Teichoic acid** chỉ có ở **Gram dương**.",
  ["Có.", "Có.", "Có.", ""], ["teichoic acid", "outer membrane"], pool="mock")
q("BAC-04", "concept", 2, "The strong negative charge of the Gram-negative outer membrane is an important factor in:",
  ["evading phagocytosis and the actions of complement", "retaining crystal violet", "making the cell acid-fast", "forming endospores"], 0,
  "Slide 40: điện tích âm mạnh giúp **tránh thực bào và bổ thể**.",
  ["", "Gram âm không giữ CV.", "Kháng acid là acid mycolic.", "Không liên quan."], ["outer membrane", "complement"], pool="mock")
q("BAC-04", "application", 3, "A drug solution is autoclaved and is sterile, yet patients develop fever after injection. The contaminating bacteria were Gram-negative. The most likely cause is:",
  ["surviving endospores", "heat-stable lipid A (endotoxin) from dead cells", "teichoic acid", "live bacteria growing in the vial"], 1,
  "Autoclave diệt vi khuẩn nhưng **lipid A chịu nhiệt**, vẫn gây sốt → phải kiểm tra endotoxin (LAL).",
  ["Gram âm thường không tạo nội bào tử; dung dịch đã vô trùng.", "", "Teichoic acid ở Gram dương.", "Dung dịch đã vô trùng."], ["endotoxin"], "Endotoxin is released from living cells only", pool="mock")
q("BAC-04", "recall", 1, "In the Gram stain, the mordant that forms a complex with crystal violet is:",
  ["safranin", "iodine", "alcohol", "methylene blue"], 1,
  "**Iodine** là chất cẩn màu (mordant), tạo phức CV-I.",
  ["Safranin là màu phụ.", "", "Cồn là chất tẩy.", "Không dùng trong nhuộm Gram."], ["Gram stain"], pool="mock")

v("BAC-04", "outer membrane", "màng ngoài", "The lipid bilayer outside the thin peptidoglycan of Gram-negative bacteria.", "The outer membrane blocks lysozyme.")
v("BAC-04", "lipopolysaccharide", "lipopolysaccharide (LPS)", "Molecule of lipid A, core polysaccharide and O polysaccharide in the outer membrane.", "LPS gives the outer membrane a negative charge.", ["LPS"])
v("BAC-04", "lipid A", "lipid A", "The lipid portion of LPS; an endotoxin.", "Lipid A causes fever.")
v("BAC-04", "endotoxin", "nội độc tố", "Lipid A released from Gram-negative cells; causes fever and shock.", "Endotoxin is heat-stable.", ["endotoxins"])
v("BAC-04", "porin", "porin (kênh màng ngoài)", "A protein channel in the outer membrane for small molecules.", "Amino acids pass through porins.", ["porins"])
v("BAC-04", "periplasmic space", "khoang chu chất", "The space between the plasma membrane and the outer membrane.", "The periplasmic space contains degrading enzymes.", ["periplasm"])
v("BAC-04", "Gram stain", "nhuộm Gram", "Differential stain: crystal violet, iodine, alcohol, safranin.", "Gram-positive cells stay purple after the Gram stain.", ["Gram-positive", "Gram-negative"])
v("BAC-04", "counterstain", "thuốc nhuộm phụ", "The second dye (safranin) that colors decolorized cells.", "Safranin is the counterstain.")
v("BAC-04", "mordant", "chất cẩn màu", "A substance (iodine) that intensifies or fixes a stain.", "Iodine is the mordant in the Gram stain.")
v("BAC-04", "complement", "bổ thể", "Host proteins that lyse cells and promote phagocytosis.", "The outer membrane helps evade complement.")

fc("BAC-04", "fact", "Four steps of the Gram stain?", "Crystal violet → iodine → alcohol/acetone → safranin.")
fc("BAC-04", "fact", "Three parts of LPS?", "Lipid A (endotoxin), core polysaccharide, O polysaccharide (O antigen).")
fc("BAC-04", "fact", "Effects of lipid A in the host?", "Fever, dilation of blood vessels, shock, blood clotting.")
fc("BAC-04", "fact", "Name 5 things the outer membrane blocks.", "Detergents, heavy metals, bile salts, certain dyes, antibiotics (penicillin), lysozyme.")
fc("BAC-04", "trap", "TRUE/FALSE: Mycoplasma is Gram-negative because it has a thin wall.", "FALSE – Mycoplasma has no cell wall; its membrane contains sterols.")

# ---------------------------------------------------------------- BAC-05
unit("BAC-05", "The plasma membrane and transport across it", "H", 2, 25, SRC + ": slides 42–50",
"""Muối dưa, ướp cá, làm mứt đường – ông bà ta đã dùng **áp suất thẩm thấu** để bảo quản thực phẩm hàng nghìn năm. Trong môi trường **ưu trương**, nước bị rút khỏi tế bào vi khuẩn qua **màng sinh chất**, tế bào co lại và ngừng phát triển. Màng sinh chất quyết định chất gì vào, chất gì ra.""",
("A bacterium is placed in 20% salt solution (hypertonic). What happens?",
 ["Water enters and the cell bursts", "Water leaves the cell and the cytoplasm shrinks (plasmolysis)", "Nothing, because the cell wall blocks water", "Salt is actively pumped out and the cell grows faster"], 1,
 "Môi trường **ưu trương** → nước đi **ra** → **co nguyên sinh (plasmolysis)** → ức chế sinh trưởng. Đó là nguyên lý muối, ướp đường."),
[
("1. Cấu trúc màng sinh chất (slide 42–44)", """
- **Lớp kép phospholipid (bilayer)**: hai hàng phospholipid song song.
  - **Đầu phân cực (polar head)**: nhóm phosphate + glycerol → **ưa nước**, hướng ra ngoài.
  - **Đuôi không phân cực (non-polar tails)**: acid béo → **kỵ nước**, hướng vào trong.
- Bao bọc **tế bào chất (cytosol)**; gồm **phospholipid và protein**.
- **Không chứa sterol** như tế bào nhân thực, **ngoại trừ *Mycoplasma***.
- **Mô hình khảm lỏng (fluid mosaic)**: phospholipid và protein **không đứng yên** mà di chuyển khá tự do trên mặt màng.
- **Protein màng**:
  - **Peripheral proteins** (ngoại vi, ở bề mặt): **xúc tác phản ứng**, **nâng đỡ**.
  - **Integral proteins** (xuyên màng): **kênh vận chuyển**.
  - Nhiều protein mang đường (glycoprotein) giúp nhận diện, truyền tín hiệu. [fig]
"""),
("2. Chức năng (slide 45–47)", """
- **Tính thấm chọn lọc (selective permeability = semipermeability)**: cho một số chất qua, chặn chất khác. Phân tử nhỏ, không phân cực (O₂, CO₂) qua dễ; ion, phân tử lớn cần protein.
- **Phân giải chất hữu cơ tạo năng lượng**: vi khuẩn **không có ty thể** → chuỗi truyền electron và ATP synthase nằm **trên màng sinh chất**.
- **Chromatophores**: ở một số vi khuẩn quang hợp, sắc tố và enzyme quang hợp nằm trong các **nếp gấp của màng** lõm vào tế bào chất.
  - **Vi khuẩn lưu huỳnh màu tía (purple sulfur bacteria)** **không dùng nước** làm chất khử → **không tạo O₂**. Chúng dùng **sulfide (H₂S), thiosulfate** (một số dùng H₂, Fe²⁺, NO₂⁻) làm chất cho electron; S bị oxy hóa thành **hạt lưu huỳnh**, có thể tiếp tục thành **acid sulfuric**.
- **Bị phá hủy bởi**: chất khử trùng **cồn và hợp chất amoni bậc bốn (quats)**, kháng sinh **polymyxin** (tương tác với phospholipid).
"""),
("3. Vận chuyển thụ động (slide 48)", """
Không tốn năng lượng, đi **theo gradient** (cao → thấp):
- **Simple diffusion (khuếch tán đơn giản)**: chất đi thẳng qua lớp lipid – **O₂, CO₂**.
- **Facilitated diffusion (khuếch tán được hỗ trợ)**: nhờ **protein màng – permease** (kênh hoặc chất mang) – **glucose, amino acid**…
"""),
("4. Thẩm thấu (slide 49)", """
**Osmosis**: sự di chuyển **của nước** qua màng bán thấm, từ nơi **nồng độ chất tan thấp** (nhiều nước) sang nơi **nồng độ chất tan cao**.

| Môi trường | So với trong tế bào | Nước | Kết quả |
|---|---|---|---|
| **Isotonic** (đẳng trương) | bằng | cân bằng, không có dòng ròng | bình thường |
| **Hypotonic** (nhược trương) | thấp hơn (vd nước cất) | **đi vào** | tế bào trương; thành chống vỡ; mất thành → **vỡ (lysis)** |
| **Hypertonic** (ưu trương) | cao hơn (vd muối, đường đặc) | **đi ra** | **co nguyên sinh (plasmolysis)** |

Nước còn đi nhanh qua kênh **aquaporin**. [mở rộng]
"""),
("5. Vận chuyển chủ động (slide 50)", """
- **Cần năng lượng** (ATP hoặc gradient ion); đi **ngược gradient** → tích lũy chất trong tế bào.
- **Phụ thuộc protein mang (carrier) trên màng**.
- **Group translocation (chuyển vị nhóm)**: **gắn nhóm chức vào chất trong lúc vận chuyển** – ví dụ **glucose được phosphoryl hóa** thành glucose-6-phosphate (hệ phosphotransferase). Glucose-6-P không đi ngược ra được → giữ trong tế bào.

| Cơ chế | Chiều gradient | Protein? | Năng lượng? |
|---|---|---|---|
| Khuếch tán đơn giản | thuận | không | không |
| Khuếch tán hỗ trợ | thuận | **có** (permease) | không |
| Thẩm thấu (nước) | thuận thế nước | không/aquaporin | không |
| Vận chuyển chủ động | **ngược** | **có** | **có** |
| Chuyển vị nhóm | – (chất bị biến đổi) | **có** | **có** (PEP) |
"""),
],
[
("Thực tế: bảo quản bằng muối và đường", """
- Nồng độ muối 10–15 % (cá khô, mắm), đường 50–65 % (mứt, sữa đặc) tạo môi trường ưu trương. Tuy nhiên **nấm mốc và nấm men chịu áp suất thẩm thấu tốt hơn vi khuẩn** → mứt để lâu vẫn có thể mốc.
- Vi khuẩn **ưa mặn (halophiles)** như *Staphylococcus aureus* (chịu tới 15 % muối) vẫn có thể phát triển trong thịt muối. (Bài GRO-01.)
"""),
("Liên hệ: polymyxin và chất khử trùng", """
Polymyxin B / colistin gắn phospholipid và LPS, phá màng – là kháng sinh \"cứu cánh cuối cùng\" cho Gram âm đa kháng. Cồn 70 % và quats (benzalkonium chloride trong nước rửa tay) cũng đánh vào màng (bài CTL-04, CTL-05).
"""),
],
[
("Plasma membrane structure", "A **phospholipid bilayer** (polar phosphate–glycerol heads, nonpolar fatty-acid tails) with **peripheral proteins** (catalysis, support) and **integral proteins** (transport channels). **Fluid mosaic**: molecules move freely. **No sterols**, except in *Mycoplasma*.", "Lớp kép phospholipid; không sterol trừ Mycoplasma."),
("Membrane functions", "**Selective permeability**; breakdown of nutrients and **energy (ATP) production**; **chromatophores** (photosynthetic infoldings). Purple sulfur bacteria use H₂S/thiosulfate, not water, so they **do not produce O₂** and deposit sulfur granules. Damaged by **alcohols, quats, polymyxin**.", "Màng = nơi tạo năng lượng ở vi khuẩn."),
("Transport", "**Passive**: simple diffusion (O₂, CO₂); facilitated diffusion with **permeases** (glucose, amino acids). **Osmosis**: water moves toward higher solute; isotonic / hypotonic (water in) / hypertonic (water out → **plasmolysis**). **Active transport**: needs energy and carriers; **group translocation** phosphorylates glucose during transport.", "Thụ động – thẩm thấu – chủ động – chuyển vị nhóm."),
],
["Bacterial membranes contain sterols", "Facilitated diffusion needs ATP", "Hypotonic makes cells shrink", "Purple sulfur bacteria release O2"])

q("BAC-05", "recall", 1, "Unlike eukaryotic membranes, bacterial plasma membranes generally lack sterols. Which bacterium is the exception?",
  ["Escherichia coli", "Mycoplasma", "Bacillus subtilis", "Mycobacterium"], 1,
  "Slide 43: màng vi khuẩn **không có sterol**, **ngoại trừ *Mycoplasma*** (không có thành, sterol giúp màng bền hơn).",
  ["Không có sterol.", "", "Không có sterol.", "Không có sterol; có acid mycolic ở thành."], ["sterol", "Mycoplasma"], "Bacterial membranes contain sterols", src=SRC + " slide 43")
q("BAC-05", "concept", 2, "Glucose enters a bacterial cell down its concentration gradient with the help of a permease and without energy input. This is:",
  ["simple diffusion", "facilitated diffusion", "active transport", "group translocation"], 1,
  "Có protein (**permease**) + thuận gradient + không tốn năng lượng = **khuếch tán được hỗ trợ**.",
  ["Không cần protein.", "", "Cần năng lượng, ngược gradient.", "Glucose bị phosphoryl hóa, tốn năng lượng."], ["facilitated diffusion", "permease"], "Facilitated diffusion needs ATP", src=SRC + " slide 48")
q("BAC-05", "concept", 2, "In group translocation, glucose is:",
  ["pumped out of the cell", "phosphorylated as it is transported, trapping it inside the cell", "converted to CO2 in the membrane", "moved by simple diffusion"], 1,
  "Slide 50: gắn nhóm chức trong khi vận chuyển – **glucose bị phosphoryl hóa** → glucose-6-P không đi ra được.",
  ["Ngược chiều.", "", "Không.", "Không."], ["group translocation"], src=SRC + " slide 50")
q("BAC-05", "application", 2, "Bacteria are suspended in distilled water after their cell walls have been removed by lysozyme. What happens?",
  ["Plasmolysis", "Water enters and the cells lyse", "No net water movement", "Cells form endospores"], 1,
  "Nước cất là môi trường **nhược trương** → nước vào; không có thành chống áp lực → **vỡ**.",
  ["Co nguyên sinh xảy ra ở ưu trương.", "", "Chỉ ở đẳng trương.", "Không liên quan."], ["osmosis", "hypotonic"], "Hypotonic makes cells shrink")
q("BAC-05", "recall", 1, "Which molecules cross the bacterial plasma membrane by simple diffusion according to the lecture?",
  ["Glucose and amino acids", "Oxygen and carbon dioxide", "Proteins", "Na+ and K+ ions"], 1,
  "Slide 48: **O₂, CO₂** – phân tử nhỏ, không phân cực – khuếch tán đơn giản. Glucose và amino acid cần permease.",
  ["Cần permease.", "", "Quá lớn.", "Ion cần kênh/protein."], ["simple diffusion"], src=SRC + " slide 48")
q("BAC-05", "concept", 2, "Purple sulfur bacteria carry out photosynthesis but do not produce oxygen because:",
  ["they lack chlorophyll", "they use sulfide or thiosulfate instead of water as the electron donor", "they are anaerobic and destroy oxygen", "they have no chromatophores"], 1,
  "Slide 47: chúng **không dùng nước** làm chất khử mà dùng **sulfide, thiosulfate** (hoặc H₂, Fe²⁺, NO₂⁻) → không giải phóng O₂; tích **hạt lưu huỳnh**.",
  ["Chúng có bacteriochlorophyll.", "", "Không phải lý do.", "Chúng có hệ màng quang hợp."], ["chromatophores", "purple sulfur bacteria"], "Purple sulfur bacteria release O2", src=SRC + " slide 47")
q("BAC-05", "not", 2, "Which agent does NOT act mainly by damaging the bacterial plasma membrane?",
  ["Alcohols", "Quaternary ammonium compounds", "Polymyxin", "Penicillin"], 3,
  "Slide 45: cồn, quats, polymyxin phá màng. **Penicillin** ức chế **tổng hợp thành** (transpeptidase).",
  ["Phá màng.", "Phá màng.", "Phá màng.", ""], ["polymyxin", "penicillin"])
q("BAC-05", "recall", 1, "In the fluid mosaic model, which membrane proteins serve mainly as transport channels?",
  ["Peripheral proteins", "Integral proteins", "Glycocalyx proteins", "Flagellin"], 1,
  "Slide 44: **integral proteins** = kênh vận chuyển; **peripheral proteins** = xúc tác, nâng đỡ.",
  ["Xúc tác/nâng đỡ.", "", "Không phải protein màng.", "Protein roi."], ["integral protein"], pool="mock")
q("BAC-05", "concept", 2, "Which property distinguishes active transport from facilitated diffusion?",
  ["Only active transport uses membrane proteins", "Active transport requires energy and can move substances against a gradient", "Facilitated diffusion moves water only", "Active transport occurs only in eukaryotes"], 1,
  "Cả hai đều dùng protein; **chỉ vận chuyển chủ động tốn năng lượng và đi ngược gradient**.",
  ["Cả hai đều dùng protein.", "", "Sai.", "Vi khuẩn có vận chuyển chủ động."], ["active transport"], pool="mock")
q("BAC-05", "application", 2, "Why can salting fish (15% NaCl) preserve it against most bacteria?",
  ["Salt denatures DNA directly", "The hypertonic environment draws water out of cells, causing plasmolysis", "Salt is an antibiotic", "Salt makes the medium hypotonic"], 1,
  "Muối tạo môi trường **ưu trương** → nước rời tế bào → **co nguyên sinh** → ức chế sinh trưởng.",
  ["Không phải cơ chế chính.", "", "Sai.", "Ngược lại."], ["plasmolysis", "hypertonic"], pool="mock")
q("BAC-05", "not", 2, "Which statement about the bacterial plasma membrane is NOT correct?",
  ["It is the site of ATP production", "It is selectively permeable", "Its phospholipids and proteins are fixed in place", "It is composed of phospholipids and proteins"], 2,
  "Slide 44: phospholipid và protein **di chuyển khá tự do** (khảm lỏng), **không cố định**.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["fluid mosaic"], pool="mock")

v("BAC-05", "plasma membrane", "màng sinh chất", "The phospholipid bilayer with proteins that encloses the cytoplasm.", "Polymyxin damages the plasma membrane.", ["cytoplasmic membrane"])
v("BAC-05", "phospholipid", "phospholipid", "A lipid with a polar phosphate head and nonpolar fatty-acid tails.", "Phospholipids form a bilayer.", ["phospholipids"])
v("BAC-05", "fluid mosaic", "mô hình khảm lỏng", "Model in which membrane lipids and proteins move freely.", "The fluid mosaic model describes membranes.", ["fluid mosaic model"])
v("BAC-05", "integral protein", "protein xuyên màng", "A protein embedded in or spanning the membrane.", "Integral proteins form transport channels.", ["integral proteins", "peripheral protein", "peripheral proteins"])
v("BAC-05", "selective permeability", "tính thấm chọn lọc", "Allowing some substances to pass while blocking others.", "Selective permeability is a key membrane function.", ["semipermeability", "semipermeable"])
v("BAC-05", "chromatophores", "thể mang sắc tố", "Membrane infoldings holding photosynthetic pigments in some bacteria.", "Photosynthetic enzymes lie in chromatophores.", ["chromatophore"])
v("BAC-05", "simple diffusion", "khuếch tán đơn giản", "Net movement from high to low concentration directly through the lipid bilayer.", "O2 enters by simple diffusion.")
v("BAC-05", "facilitated diffusion", "khuếch tán được hỗ trợ", "Passive movement down a gradient through a carrier protein (permease).", "Glucose can enter by facilitated diffusion.")
v("BAC-05", "permease", "permease (protein vận chuyển)", "A transporter protein that carries a solute across the membrane.", "Permeases carry amino acids.", ["permeases"])
v("BAC-05", "osmosis", "thẩm thấu", "Net movement of water across a selectively permeable membrane toward higher solute.", "Osmosis causes plasmolysis in salt.")
v("BAC-05", "hypertonic", "ưu trương", "A solution with a higher solute concentration than the cell.", "Hypertonic salt solutions cause plasmolysis.", ["hypotonic", "isotonic"])
v("BAC-05", "plasmolysis", "co nguyên sinh", "Shrinkage of the cytoplasm due to water loss.", "Salt causes plasmolysis.")
v("BAC-05", "active transport", "vận chuyển chủ động", "Energy-requiring transport against a gradient using carrier proteins.", "Active transport accumulates nutrients.")
v("BAC-05", "group translocation", "chuyển vị nhóm", "Transport in which the substance is chemically modified (e.g., phosphorylated) during transport.", "Glucose enters E. coli by group translocation.")

fc("BAC-05", "fact", "Peripheral vs integral membrane proteins?", "Peripheral: catalyze reactions, support. Integral: transport channels.")
fc("BAC-05", "fact", "Three agents that damage the bacterial membrane?", "Alcohols, quaternary ammonium compounds, polymyxin.")
fc("BAC-05", "fact", "Electron donors of purple sulfur bacteria?", "Sulfide, thiosulfate (some: H2, Fe2+, NO2−); no O2 released; sulfur granules formed.")
fc("BAC-05", "fact", "Hypo-, iso-, hypertonic: water direction?", "Hypotonic: in (swell/lysis). Isotonic: no net. Hypertonic: out (plasmolysis).")
fc("BAC-05", "trap", "TRUE/FALSE: facilitated diffusion requires ATP.", "FALSE – it is passive; it only needs a carrier protein.")

# ---------------------------------------------------------------- BAC-06
unit("BAC-06", "Cytoplasm, nucleoid, plasmids, ribosomes, inclusions and endospores", "H", 2, 25, SRC + ": slides 13, 51–56",
"""Đồ hộp tự làm (măng, cá, pate) được đun sôi 100 °C vẫn có thể gây **ngộ độc botulinum** chết người. Thủ phạm *Clostridium botulinum* tạo **nội bào tử (endospore)** – cấu trúc chịu được **nước sôi hàng giờ**. Muốn diệt nó, nhà máy đồ hộp phải dùng **121 °C dưới áp suất**. Nội bào tử khác gì một tế bào thường?""",
("Which statement about bacterial endospores is correct?",
 ["One vegetative cell forms many endospores to reproduce", "One cell forms one endospore, which is a resistant resting structure, not a means of reproduction", "Endospores are found in all bacteria", "Endospores are killed by boiling for 1 minute"], 1,
 "**1 tế bào → 1 nội bào tử → (nảy mầm) → 1 tế bào**. Nội bào tử để **sống sót**, không để sinh sản."),
[
("1. Tế bào chất và vùng nhân", """
- **Cytoplasm**: khoảng **80 % là nước**, chứa protein (enzyme), carbohydrate, lipid, ion vô cơ; đặc, bán lỏng. [fig]
- Vi khuẩn **không có** bộ khung tế bào dạng vi ống điển hình, **không có bào quan có màng**, không có dòng chảy tế bào chất. (Thực ra có protein khung tương đồng như MreB, FtsZ.) [mở rộng]
- **Nucleoid (vùng nhân)**: chứa **nhiễm sắc thể vi khuẩn** – thường là **một phân tử DNA mạch kép, dạng vòng**, **không có màng nhân**, không có histone điển hình.
"""),
("2. Plasmid (slide 13: \"plasmid?\")", """
- **Plasmid**: phân tử **DNA mạch kép, vòng, nhỏ**, **nằm ngoài nhiễm sắc thể**, **tự sao chép độc lập**.
- **Không cần thiết** cho sự sống trong điều kiện bình thường, nhưng mang gene **có lợi trong điều kiện đặc biệt**:
  - gene **kháng kháng sinh** (R plasmid) và kháng kim loại nặng;
  - gene **độc tố**, enzyme phân giải chất lạ;
  - gene **tiếp hợp** (F factor) – chuyển sang tế bào khác qua **pili**.
- Có thể mất đi hoặc được truyền giữa tế bào → nền tảng của **công nghệ DNA tái tổ hợp** (vector nhân dòng).
"""),
("3. Ribosome 70S", """
- Nơi **tổng hợp protein**. Vi khuẩn có ribosome **70S**, gồm **tiểu đơn vị nhỏ 30S** và **lớn 50S**.
- **S (Svedberg)** là **hệ số lắng** khi siêu ly tâm → **không cộng số học** (30 + 50 ≠ 70).
- Tế bào nhân thực có ribosome **80S** (40S + 60S) trong tế bào chất (ty thể/lục lạp có 70S).
- Khác biệt này là cơ sở của **độc tính chọn lọc**: **streptomycin, gentamicin** gắn **30S**; **erythromycin, chloramphenicol** gắn **50S**. [fig]
"""),
("4. Thể vùi – inclusions (slide 54)", """
Các hạt dự trữ/chức năng trong tế bào chất:
| Thể vùi | Chứa | Nhận biết / ý nghĩa |
|---|---|---|
| **Volutin** (**metachromatic granules**) | **phosphate vô cơ** (polyphosphate) | bắt màu **đỏ** với **methylene blue** (biến sắc) – đặc trưng *Corynebacterium diphtheriae* |
| **Polysaccharide granules** | **glycogen, tinh bột** | nhuộm **iodine** (glycogen nâu đỏ, tinh bột xanh) |
| **Lipid inclusions** | lipid (vd poly-β-hydroxybutyrate) | nhuộm **Sudan** (thuốc nhuộm tan trong mỡ) |
| **Sulfur granules** | **lưu huỳnh** | dự trữ năng lượng ở vi khuẩn oxy hóa lưu huỳnh |
| **Carboxysomes** | enzyme **ribulose 1,5-diphosphate carboxylase (RuBisCO)** | **cố định CO₂** |
| **Gas vacuoles** | các **túi khí** | giúp vi khuẩn thủy sinh **nổi** |
| **Magnetosomes** | **Fe₃O₄ (magnetite)** | định hướng theo **từ trường** |
"""),
("5. Nội bào tử – endospore (slide 13, 55–56)", """
**Endospore**: cấu trúc **ngủ, cực kỳ bền** hình thành **bên trong** tế bào của một số vi khuẩn **Gram dương**, chủ yếu ***Bacillus*** và ***Clostridium***, khi **thiếu chất dinh dưỡng**.

**Sporulation (tạo bào tử)** [fig]:
1. DNA sao chép; một **vách ngăn bào tử (spore septum)** tách một phần DNA + tế bào chất.
2. Màng tế bào mẹ bao quanh tạo **forespore** (tiền bào tử) với hai lớp màng.
3. Lớp **cortex** (peptidoglycan) hình thành giữa hai màng; ngoài cùng là **spore coat** (protein) dày.
4. Tế bào mẹ tự phân hủy → **giải phóng nội bào tử**.

**Vì sao bền?** Lõi **rất ít nước**, chứa **acid dipicolinic + Ca²⁺** bảo vệ DNA, protein SASP gắn DNA, các lớp vỏ dày. Chịu được **nhiệt, khô, bức xạ, hóa chất, acid**; sống sót hàng trăm–nghìn năm.

**Germination (nảy mầm)**: khi điều kiện thuận lợi (nhiệt, chất dinh dưỡng) → nội bào tử trở lại **tế bào sinh dưỡng (vegetative cell)**.

> **Không phải sinh sản**: 1 tế bào → 1 nội bào tử → 1 tế bào. Số lượng không tăng. (Khác **bào tử nấm** là cơ quan sinh sản – bài FUN.)

Ý nghĩa thực tế: phải dùng **autoclave 121 °C** mới diệt được; bệnh do vi khuẩn tạo bào tử: uốn ván (*C. tetani*), ngộ độc thịt (*C. botulinum*), bệnh than (*B. anthracis*), viêm ruột (*C. difficile*).
"""),
],
[
("Công nghệ đồ hộp: quy tắc 12D", """
Nhà máy đồ hộp thực phẩm ít acid (pH > 4,6) phải xử lý nhiệt đủ để giảm **10¹² lần** bào tử *C. botulinum* (**12D**) – thường ~121 °C trong vài phút tại tâm hộp. Bạn sẽ tính D-value ở bài CTL-01.
"""),
("Plasmid trong công nghệ sinh học", """
Plasmid là \"xe chở gene\": gắn gene insulin người vào plasmid, đưa vào *E. coli* → vi khuẩn tổng hợp insulin. Gene kháng ampicillin trên plasmid dùng để **chọn lọc** tế bào mang plasmid trên môi trường có kháng sinh.
"""),
("Magnetosome & carboxysome", """
Vi khuẩn hướng từ (*Magnetospirillum*) được nghiên cứu làm hạt nano từ tính cho y sinh. Carboxysome đang được \"cấy\" vào cây trồng để tăng hiệu suất quang hợp.
"""),
],
[
("Nucleoid and plasmids", "The **nucleoid** holds the bacterial chromosome: usually one **circular, double-stranded DNA**, no nuclear membrane. **Plasmids** are small circular DNA molecules that **replicate independently**, are not essential, and may carry genes for **antibiotic resistance**, toxins or conjugation.", "Plasmid: DNA vòng nhỏ, tự sao chép, không thiết yếu."),
("70S ribosomes", "Bacterial ribosomes are **70S** (30S + 50S subunits); eukaryotic cytoplasmic ribosomes are **80S**. S = sedimentation coefficient, not additive. Streptomycin targets 30S; erythromycin targets 50S.", "70S = 30S + 50S; khác 80S nhân thực."),
("Inclusions", "**Volutin/metachromatic granules** (phosphate, red with methylene blue); **polysaccharide granules** (glycogen, starch; iodine); **lipid inclusions** (Sudan dye); **sulfur granules**; **carboxysomes** (ribulose 1,5-diphosphate carboxylase, CO₂ fixation); **gas vacuoles**; **magnetosomes** (Fe₃O₄).", "7 loại thể vùi."),
("Endospores", "Formed inside some Gram-positive rods (*Bacillus, Clostridium*) when nutrients run out. Very little water, **dipicolinic acid + Ca²⁺**, thick cortex and coat → resistant to heat, drying, radiation and chemicals. **One cell → one spore**: not reproduction. Germination returns a vegetative cell.", "Nội bào tử: sống sót, không sinh sản."),
],
["Endospores are for reproduction", "70S = 30S + 50S arithmetic", "Plasmids are essential", "Volutin stains with iodine"])

q("BAC-06", "recall", 1, "Metachromatic granules (volutin) contain inorganic phosphate and appear red when stained with:",
  ["iodine", "Sudan dye", "methylene blue", "safranin"], 2,
  "Slide 54: **volutin** chứa phosphate vô cơ, **đỏ với methylene blue**.",
  ["Iodine nhuộm hạt polysaccharide.", "Sudan nhuộm lipid.", "", "Không đúng."], ["volutin"], "Volutin stains with iodine", src=SRC + " slide 54")
q("BAC-06", "recall", 1, "Which inclusion contains the enzyme ribulose 1,5-diphosphate carboxylase for CO2 fixation?",
  ["Magnetosome", "Carboxysome", "Gas vacuole", "Volutin"], 1,
  "**Carboxysome** chứa RuBisCO – cố định CO₂.",
  ["Chứa Fe₃O₄.", "", "Chứa túi khí.", "Chứa phosphate."], ["carboxysome"], src=SRC + " slide 54")
q("BAC-06", "concept", 2, "Why is endospore formation NOT considered a means of reproduction?",
  ["Endospores contain no DNA", "One vegetative cell produces only one endospore, which germinates into one cell", "Endospores are formed only by fungi", "Endospores divide by budding"], 1,
  "**1 tế bào → 1 bào tử → 1 tế bào**: số lượng không tăng. Nội bào tử là cấu trúc **sống sót**.",
  ["Nội bào tử chứa DNA.", "", "Nội bào tử là của vi khuẩn.", "Không."], ["endospore", "germination"], "Endospores are for reproduction")
q("BAC-06", "concept", 2, "Which feature contributes most to the heat resistance of endospores?",
  ["A large amount of water in the core", "Very low water content and dipicolinic acid with calcium in the core", "An outer membrane with LPS", "Numerous flagella"], 1,
  "Lõi **rất ít nước**, chứa **acid dipicolinic + Ca²⁺** bảo vệ DNA và protein; thêm cortex và spore coat dày.",
  ["Ngược lại.", "", "Không liên quan.", "Không liên quan."], ["endospore", "dipicolinic acid"])
q("BAC-06", "recall", 1, "Bacterial ribosomes are:",
  ["80S, with 40S and 60S subunits", "70S, with 30S and 50S subunits", "70S, with 20S and 50S subunits", "60S, with 30S and 30S subunits"], 1,
  "Vi khuẩn: **70S = 30S + 50S** (S là hệ số lắng, không cộng số học). Nhân thực: 80S = 40S + 60S.",
  ["Đó là ribosome nhân thực.", "", "Sai.", "Sai."], ["ribosome"], "70S = 30S + 50S arithmetic")
q("BAC-06", "concept", 2, "Plasmids are best described as:",
  ["essential chromosomes containing all housekeeping genes", "small, self-replicating extrachromosomal DNA molecules that may carry resistance genes", "RNA molecules that code for ribosomes", "protein granules for phosphate storage"], 1,
  "Plasmid: DNA vòng nhỏ, **ngoài nhiễm sắc thể**, **tự sao chép**, **không thiết yếu**, có thể mang gene kháng kháng sinh, độc tố, tiếp hợp.",
  ["Plasmid không thiết yếu.", "", "Sai.", "Đó là volutin."], ["plasmid"], "Plasmids are essential")
q("BAC-06", "application", 2, "A freshwater bacterium floats near the surface to capture light. Which inclusion most likely helps it?",
  ["Magnetosomes", "Gas vacuoles", "Lipid inclusions", "Sulfur granules"], 1,
  "**Gas vacuoles** (túi khí) giúp vi khuẩn thủy sinh **nổi** lên vùng có ánh sáng.",
  ["Định hướng từ trường.", "", "Dự trữ lipid.", "Dự trữ lưu huỳnh."], ["gas vacuole"])
q("BAC-06", "not", 2, "Which pair of inclusion and content is NOT correct?",
  ["Magnetosome – Fe3O4", "Polysaccharide granules – glycogen and starch", "Lipid inclusions – stained with Sudan dye", "Volutin – elemental sulfur"], 3,
  "**Volutin** chứa **phosphate vô cơ**; lưu huỳnh nằm ở **sulfur granules**.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["volutin"], pool="mock")
q("BAC-06", "recall", 1, "Endospores are produced mainly by which bacterial genera?",
  ["Escherichia and Salmonella", "Bacillus and Clostridium", "Streptococcus and Staphylococcus", "Neisseria and Vibrio"], 1,
  "Nội bào tử chủ yếu ở trực khuẩn Gram dương ***Bacillus*** (hiếu khí) và ***Clostridium*** (kỵ khí).",
  ["Gram âm, không tạo nội bào tử.", "", "Không tạo nội bào tử.", "Không tạo nội bào tử."], ["endospore"], pool="mock")
q("BAC-06", "concept", 2, "Streptomycin inhibits bacterial protein synthesis without killing human cells mainly because:",
  ["human cells have no ribosomes", "it binds the 30S subunit of 70S bacterial ribosomes, which differ from 80S eukaryotic ribosomes", "it blocks peptidoglycan", "it dissolves bacterial membranes"], 1,
  "Ribosome **70S** vi khuẩn khác **80S** nhân thực → thuốc gắn **30S** có độc tính chọn lọc.",
  ["Sai.", "", "Đó là penicillin.", "Đó là polymyxin."], ["ribosome", "selective toxicity"], pool="mock")
q("BAC-06", "not", 2, "Which is NOT true of the bacterial nucleoid?",
  ["It usually contains a single circular chromosome", "It is surrounded by a nuclear envelope", "It contains double-stranded DNA", "It lacks a membrane"], 1,
  "Vùng nhân **không có màng nhân** – đặc điểm nhân sơ.",
  ["Đúng.", "", "Đúng.", "Đúng."], ["nucleoid"], pool="mock")

v("BAC-06", "cytoplasm", "tế bào chất", "The substance inside the plasma membrane, about 80% water.", "Inclusions lie in the cytoplasm.", ["cytosol"])
v("BAC-06", "nucleoid", "vùng nhân", "The region containing the bacterial chromosome, without a membrane.", "The nucleoid holds circular DNA.")
v("BAC-06", "plasmid", "plasmid", "Small circular extrachromosomal DNA that replicates independently.", "R plasmids carry resistance genes.", ["plasmids"])
v("BAC-06", "ribosome", "ribosome", "The site of protein synthesis; 70S in bacteria, 80S in eukaryotes.", "Bacterial ribosomes are 70S.", ["ribosomes", "70S", "80S"])
v("BAC-06", "inclusions", "thể vùi", "Reserve deposits or specialized structures in the cytoplasm.", "Volutin is an inclusion.", ["inclusion"])
v("BAC-06", "volutin", "hạt volutin (hạt dị sắc)", "Phosphate reserve granules that stain red with methylene blue.", "Volutin granules are metachromatic.", ["metachromatic granules"])
v("BAC-06", "carboxysome", "carboxysome", "Inclusion containing ribulose 1,5-diphosphate carboxylase for CO2 fixation.", "Cyanobacteria have carboxysomes.", ["carboxysomes"])
v("BAC-06", "gas vacuole", "không bào khí", "Inclusion of gas vesicles that provides buoyancy.", "Gas vacuoles help cells float.", ["gas vacuoles"])
v("BAC-06", "magnetosome", "thể từ", "Inclusion containing iron oxide (Fe3O4) that orients cells in a magnetic field.", "Magnetosomes act like a compass.", ["magnetosomes"])
v("BAC-06", "endospore", "nội bào tử", "A resistant dormant structure formed inside some Gram-positive bacteria.", "Clostridium botulinum forms endospores.", ["endospores"])
v("BAC-06", "sporulation", "sự tạo bào tử", "The process of endospore formation.", "Sporulation starts when nutrients are depleted.", ["sporogenesis"])
v("BAC-06", "germination", "sự nảy mầm (bào tử)", "Return of an endospore to the vegetative state.", "Heat can trigger germination.")
v("BAC-06", "vegetative cell", "tế bào sinh dưỡng", "An actively growing cell, as opposed to a spore.", "An endospore germinates into a vegetative cell.", ["vegetative cells"])
v("BAC-06", "dipicolinic acid", "acid dipicolinic", "A compound that, with calcium, protects the endospore core.", "Dipicolinic acid contributes to heat resistance.")

fc("BAC-06", "fact", "Seven inclusions in the lecture?", "Volutin, polysaccharide granules, lipid inclusions, sulfur granules, carboxysomes, gas vacuoles, magnetosomes.")
fc("BAC-06", "fact", "Stains for volutin, polysaccharide and lipid inclusions?", "Methylene blue (red), iodine, Sudan dye.")
fc("BAC-06", "number", "Ribosome sizes: bacteria vs eukaryotes?", "70S (30S + 50S) vs 80S (40S + 60S).")
fc("BAC-06", "fact", "Two endospore-forming genera?", "Bacillus and Clostridium.")
fc("BAC-06", "trap", "TRUE/FALSE: endospore formation increases cell number.", "FALSE – one cell makes one endospore.")

# ---------------------------------------------------------------- BAC-07
unit("BAC-07", "Reproduction and classification of bacteria", "M", 2, 20, SRC + ": slides 57–73",
"""Trong 20 phút, một tế bào *E. coli* chia đôi. Sau 7 giờ (21 thế hệ), một tế bào thành **2²¹ ≈ 2 triệu** tế bào – nhưng làm sao phân loại hàng triệu loài vi khuẩn **nhìn giống nhau dưới kính**? Nhà khoa học chuyển từ **hình dạng** sang **trình tự rRNA** để vẽ cây tiến hóa.""",
("Why did bacterial classification move from phenotypic features (Gram stain, shape) to rRNA sequences?",
 ["Phenotypic features are too expensive to measure", "Phenotypic groupings do not provide a clear evolutionary history", "rRNA is found only in pathogens", "Gram stain no longer works"], 1,
 "Slide 61–62: phân loại theo đặc điểm tế bào **không phản ánh rõ lịch sử tiến hóa**. So sánh trình tự **rRNA (16S)** cho biết quan hệ họ hàng."),
[
("1. Các kiểu sinh sản (slide 70–73)", """
- **Binary fission (phân đôi)** – phổ biến nhất [fig]:
  1. Tế bào dài ra, **DNA nhân đôi**.
  2. Màng và thành **lõm vào** giữa tế bào, hai bản DNA tách ra hai đầu.
  3. **Vách ngăn (septum)** hình thành.
  4. Tách thành **hai tế bào con giống hệt** nhau.
- **Budding (nảy chồi)**: một chồi nhỏ mọc ra, lớn lên rồi tách – ví dụ ***Hyphomicrobium*** (slide 73).
- **Fragmentation (đứt đoạn)** sợi: vi khuẩn dạng sợi như xạ khuẩn đứt thành đoạn, mỗi đoạn thành tế bào mới. [fig]
- **Conidiospores** ở đầu sợi của **xạ khuẩn (actinomycetes, *Streptomyces*)**. [fig]

Số tế bào sau n thế hệ phân đôi: **N = N₀ × 2ⁿ** (chi tiết tính toán ở bài GRO-05).
"""),
("2. Chuyển gene ngang (liên hệ slide 21–22)", """
Không phải sinh sản nhưng làm thay đổi kiểu gene:
| Cơ chế | DNA đi bằng đường nào |
|---|---|
| **Transformation** (biến nạp) | tế bào nhận **DNA tự do** từ môi trường |
| **Conjugation** (tiếp hợp) | qua **pilus**, tiếp xúc tế bào (F⁺ → F⁻, Hfr) |
| **Transduction** (tải nạp) | **phage** mang DNA vi khuẩn |

Mẹo: **Tự do – Tiếp xúc – Phage**. [mở rộng: slide chỉ nêu pili chuẩn bị chuyển DNA]
"""),
("3. Tên khoa học", """
- **Danh pháp hai phần** (binomial): ***Genus species***, chi viết hoa, loài viết thường, in nghiêng: *Escherichia coli* → *E. coli*.
- Các bậc: Domain → Phylum → Class → Order → Family → Genus → Species; dưới loài có **strain** (chủng).
"""),
("4. Phân loại dựa trên đặc điểm tế bào – Bergey's Manual (slide 60–62)", """
***Bergey's Manual of Systematic Bacteriology***: vi khuẩn chia **4 divisions/phyla**. Mỗi ngành chia nhóm theo:
- **phản ứng nhuộm Gram**;
- **hình dạng** tế bào;
- **cách sắp xếp**;
- **nhu cầu oxy**;
- **khả năng di động**;
- **đặc điểm dinh dưỡng và trao đổi chất**.

Bốn ngành lịch sử [fig]: *Gracilicutes* (Gram âm, thành mỏng), *Firmicutes* (Gram dương, thành dày), *Tenericutes* (không thành – *Mycoplasma*), *Mendosicutes* (thành bất thường – archaea).

→ Nhược điểm (slide 61–62): **không cho thấy rõ lịch sử tiến hóa** của vi khuẩn.
"""),
("5. Phân loại dựa trên trình tự rRNA (slide 65–69)", """
- **Carl Woese (1977)** so sánh trình tự **16S rRNA** → đề xuất **3 miền (domains)**: **Bacteria, Archaea, Eukarya**. [fig]
- 16S rRNA thích hợp vì: có ở **mọi** tế bào nhân sơ, chức năng **bảo tồn**, có vùng biến đổi chậm và vùng thay đổi → dùng như "đồng hồ phân tử".
- Slide 69 – các ngành chính (hệ Bergey mới):
| Ngành | Gram | Ví dụ |
|---|---|---|
| **Proteobacteria** | phần lớn Gram âm | *E. coli, Salmonella, Pseudomonas, Vibrio* |
| **Firmicutes** | Gram dương (G+C thấp) | *Bacillus, Clostridium, Staphylococcus, Lactobacillus* |
| **Actinobacteria** | Gram dương (G+C cao) | *Streptomyces, Mycobacterium, Corynebacterium* |
| **Cyanobacteria** | Gram âm, quang hợp tạo O₂ | *Anabaena, Spirulina* |
| **Spirochaetes** | xoắn thể | *Treponema, Borrelia* |
| **Chlamydiae/Verrucomicrobia** | ký sinh nội bào | *Chlamydia* |
| **Deinococcus-Thermus** | Gram dương, chịu bức xạ/nhiệt | *Deinococcus radiodurans* |
| **Bacteroidetes/Chlorobi, Chloroflexi, Fusobacteria, Thermotogae** | Gram âm | |
| **Acidobacteria** | ngành mới, đa dạng, **ưa acid** | |
| **Aquificae** | sống môi trường **khắc nghiệt** | |
| **Planctomycetes** | | |
"""),
],
[
("Thực tế: định danh bằng 16S rRNA", """
Phòng thí nghiệm hiện đại khuếch đại gene **16S rDNA** bằng PCR, giải trình tự rồi **BLAST** với ngân hàng gene – nhận diện vi khuẩn trong 1–2 ngày, kể cả loài không nuôi cấy được. Bạn sẽ học chi tiết ở IDT-02.
"""),
("Mở rộng: vi khuẩn chịu bức xạ", """
*Deinococcus radiodurans* chịu được liều bức xạ gấp ~1000 lần liều gây chết người nhờ nhiều bản sao genome và hệ sửa chữa DNA mạnh – ứng viên xử lý chất thải phóng xạ.
"""),
],
[
("Reproduction", "Most bacteria reproduce by **binary fission** (DNA replicates, cell elongates, septum forms, two identical cells). Others: **budding** (*Hyphomicrobium*), **fragmentation** of filaments, **conidiospores** (actinomycetes). N = N₀ × 2ⁿ.", "Phân đôi, nảy chồi, đứt đoạn, bào tử đính."),
("Phenotypic classification", "*Bergey's Manual of Systematic Bacteriology*: **4 divisions/phyla**, grouped by **Gram reaction, cell shape, arrangement, oxygen requirement, motility, nutrition/metabolism**. Weakness: **no clear evolutionary history**.", "Phân loại theo đặc điểm: không rõ tiến hóa."),
("rRNA-based classification", "Comparing **16S rRNA** sequences (Woese) gives **3 domains** (Bacteria, Archaea, Eukarya) and phyla such as **Proteobacteria** (mostly Gram−), **Firmicutes** and **Actinobacteria** (Gram+), **Cyanobacteria**, **Spirochaetes**, **Deinococcus-Thermus** (Gram+).", "16S rRNA → cây tiến hóa, 3 miền."),
],
["Conjugation is reproduction", "Bergey's phenotypic groups show evolution", "Proteobacteria are Gram-positive"])

q("BAC-07", "recall", 1, "Most bacteria reproduce by:",
  ["budding", "binary fission", "sexual spores", "conjugation"], 1,
  "**Phân đôi (binary fission)** là kiểu sinh sản phổ biến nhất. Nảy chồi ở *Hyphomicrobium*; tiếp hợp là chuyển gene, không phải sinh sản.",
  ["Chỉ vài nhóm (Hyphomicrobium).", "", "Vi khuẩn không có bào tử hữu tính.", "Tiếp hợp không tăng số lượng."], ["binary fission"], "Conjugation is reproduction", src=SRC + " slides 71–72")
q("BAC-07", "recall", 1, "Hyphomicrobium is shown in the lecture as an example of bacterial reproduction by:",
  ["binary fission", "budding", "fragmentation", "endospore formation"], 1,
  "Slide 73: ***Hyphomicrobium*** sinh sản bằng **nảy chồi (budding)**.",
  ["Không.", "", "Không.", "Nội bào tử không phải sinh sản."], ["budding"], src=SRC + " slide 73")
q("BAC-07", "not", 2, "Which criterion is NOT used in Bergey's phenotypic grouping of bacteria described in the lecture?",
  ["Reaction to Gram stain", "Oxygen requirement", "Cell arrangement", "16S rRNA sequence"], 3,
  "Slide 60: Gram, hình dạng, sắp xếp, nhu cầu oxy, di động, dinh dưỡng/trao đổi chất. **16S rRNA** là cơ sở của phân loại **phân tử** (slide 65).",
  ["Có dùng.", "Có dùng.", "Có dùng.", ""], ["Bergey's Manual"], src=SRC + " slide 60")
q("BAC-07", "concept", 2, "The main weakness of classifying bacteria only by Gram reaction, shape and metabolism is that it:",
  ["cannot identify pathogens", "does not provide a clear evolutionary history of bacteria", "requires DNA sequencing", "applies only to archaea"], 1,
  "Slide 61–62: **\"Does not provide a clear evolutionary history of bacteria\"**.",
  ["Vẫn hỗ trợ nhận diện.", "", "Không cần DNA.", "Sai."], ["phylogeny"], "Bergey's phenotypic groups show evolution")
q("BAC-07", "concept", 2, "Why is 16S rRNA used to build phylogenetic trees of bacteria?",
  ["It is found only in pathogenic bacteria", "It is present in all prokaryotes and its sequence changes slowly, reflecting evolutionary relationships", "It codes for flagellin", "It determines the Gram reaction"], 1,
  "16S rRNA có ở **mọi** nhân sơ, chức năng **bảo tồn**, biến đổi chậm → phản ánh quan hệ tiến hóa.",
  ["Có ở mọi nhân sơ.", "", "Sai.", "Sai."], ["16S rRNA"])
q("BAC-07", "recall", 1, "According to the lecture, Firmicutes and Actinobacteria are:",
  ["Gram-negative", "Gram-positive", "archaea", "wall-less"], 1,
  "Slide 69: **Firmicutes (Gram+)**, **Actinobacteria (Gram+)**, Deinococcus-Thermus (Gram+); Proteobacteria phần lớn Gram âm.",
  ["Sai.", "", "Sai.", "Sai."], ["Firmicutes"], src=SRC + " slide 69")
q("BAC-07", "recall", 1, "Which phylum is described in the lecture as \"most Gram-negative\" and includes E. coli?",
  ["Firmicutes", "Proteobacteria", "Actinobacteria", "Deinococcus-Thermus"], 1,
  "**Proteobacteria** (phần lớn Gram âm) gồm *E. coli, Salmonella, Pseudomonas*.",
  ["Gram dương.", "", "Gram dương.", "Gram dương."], ["Proteobacteria"], "Proteobacteria are Gram-positive", pool="mock", src=SRC + " slide 69")
q("BAC-07", "application", 2, "A starting population of 500 cells undergoes 4 generations of binary fission with no death. How many cells are there?",
  ["2,000", "8,000", "4,000", "1,000"], 1,
  "N = N₀ × 2ⁿ = 500 × 2⁴ = 500 × 16 = **8.000**.",
  ["500 × 4 – nhân với n thay vì 2ⁿ.", "", "500 × 2³ – thiếu một thế hệ.", "Chỉ 1 thế hệ."], ["binary fission"], pool="mock", steps=["N = N₀ × 2ⁿ", "2⁴ = 16", "500 × 16 = 8000"])
q("BAC-07", "recall", 1, "Acidobacteria are described in the lecture as:",
  ["a new, diverse phylum associated with acidic conditions", "Gram-positive spore formers", "photosynthetic oxygen producers", "wall-less parasites"], 0,
  "Slide 69: **Acidobacteria – ngành mới, đa dạng, ưa acid**. Aquificae sống môi trường khắc nghiệt.",
  ["", "Sai.", "Đó là Cyanobacteria.", "Sai."], [], pool="mock", src=SRC + " slide 69")

v("BAC-07", "binary fission", "phân đôi", "Division of one cell into two identical daughter cells.", "E. coli reproduces by binary fission.")
v("BAC-07", "budding", "nảy chồi", "Reproduction by an outgrowth that enlarges and separates.", "Hyphomicrobium reproduces by budding.")
v("BAC-07", "fragmentation", "đứt đoạn", "Breaking of filaments into pieces that grow into new cells.", "Filamentous bacteria can reproduce by fragmentation.")
v("BAC-07", "conjugation", "tiếp hợp", "Transfer of DNA between cells through direct contact via a pilus.", "Conjugation can spread plasmids.")
v("BAC-07", "transformation", "biến nạp", "Uptake of free DNA from the environment.", "Griffith observed transformation.")
v("BAC-07", "transduction", "tải nạp", "Transfer of bacterial DNA by a bacteriophage.", "Transduction requires a phage.")
v("BAC-07", "Bergey's Manual", "Cẩm nang Bergey", "The reference for bacterial classification and identification.", "Bergey's Manual groups bacteria by Gram reaction and shape.", ["Bergey's Manual of Systematic Bacteriology"])
v("BAC-07", "16S rRNA", "rRNA 16S", "The RNA of the small ribosomal subunit used to infer bacterial phylogeny.", "16S rRNA sequences define the three domains.", ["16S rDNA", "rRNA"])
v("BAC-07", "phylogeny", "phát sinh chủng loại", "The evolutionary history of a group of organisms.", "rRNA reveals bacterial phylogeny.", ["phylogenetic"])
v("BAC-07", "Proteobacteria", "ngành Proteobacteria", "A large phylum of mostly Gram-negative bacteria.", "E. coli belongs to the Proteobacteria.")
v("BAC-07", "Firmicutes", "ngành Firmicutes", "Gram-positive bacteria with low G+C content.", "Bacillus is in the Firmicutes.", ["Actinobacteria"])
v("BAC-07", "domain", "miền (bậc phân loại cao nhất)", "The highest taxon: Bacteria, Archaea or Eukarya.", "Woese proposed three domains.", ["domains"])

fc("BAC-07", "fact", "Four modes of bacterial reproduction?", "Binary fission, budding (Hyphomicrobium), fragmentation, conidiospores (actinomycetes).")
fc("BAC-07", "fact", "Six criteria for Bergey's phenotypic groups?", "Gram reaction, cell shape, arrangement, oxygen requirement, motility, nutrition/metabolism.")
fc("BAC-07", "fact", "Weakness of phenotypic classification?", "It does not provide a clear evolutionary history.")
fc("BAC-07", "fact", "Gram reactions of Firmicutes, Actinobacteria, Deinococcus-Thermus, Proteobacteria?", "Gram+, Gram+, Gram+, mostly Gram−.")

# ---------------------------------------------------------------- BAC-08
unit("BAC-08", "Archaea", "M", 2, 15, SRC + ": slides 74–77",
"""Suối nước nóng Yellowstone ở 90 °C, hồ muối Chết mặn gấp 10 lần nước biển, dạ cỏ bò không có oxy – những nơi tưởng như không sinh vật nào sống nổi lại đầy **vi khuẩn cổ (Archaea)**. Enzyme **Taq polymerase** trong máy PCR của bạn cũng có \"họ hàng\" chịu nhiệt tương tự từ archaea (*Pfu* polymerase). Archaea nhìn giống vi khuẩn – vậy khác ở đâu?""",
("Which feature distinguishes archaea from bacteria?",
 ["Archaea have a nucleus", "Archaea lack peptidoglycan and have ether-linked membrane lipids", "Archaea have 80S ribosomes and mitochondria", "Archaea are all pathogens"], 1,
 "Archaea **không có peptidoglycan** (có pseudomurein hoặc lớp S) và lipid màng nối **ether** với chuỗi isoprenoid phân nhánh."),
[
("1. Archaea là gì?", """
- Một trong **ba miền** sự sống (Woese). **Nhân sơ** (không nhân), nhưng về mặt phân tử nhiều điểm **gần Eukarya** hơn Bacteria (RNA polymerase, histone-like protein…). [mở rộng]
- Hình dạng đa dạng: cầu, que, xoắn, dạng **vuông/phẳng** (*Haloarcula*), không đều.
- **Chưa phát hiện archaea gây bệnh** cho người.
"""),
("2. Thành tế bào (slide 76)", """
- **Không có peptidoglycan** điển hình → **kháng lysozyme và penicillin** tự nhiên.
- Một số có **pseudomurein** (pseudopeptidoglycan):
  - chứa **N-acetyl talosaminuronic acid (NAT)** **thay cho NAM**;
  - **không chứa D-amino acid**;
  - liên kết **β-1,3** thay vì β-1,4 (vì vậy lysozyme không cắt được).
- Nhiều archaea có **lớp S (S-layer)** bằng protein/glycoprotein; một số không có thành.
- Nhuộm Gram cho kết quả dương hoặc âm tùy loài nhưng không phản ánh cấu trúc như vi khuẩn.
"""),
("3. Màng sinh chất (slide 77)", """
| | Bacteria / Eukarya | Archaea |
|---|---|---|
| Liên kết glycerol – chuỗi kỵ nước | **ester** | **ether** (bền hơn với nhiệt, acid) |
| Chuỗi kỵ nước | acid béo thẳng | **isoprenoid phân nhánh** (phytanyl) |
| Cấu trúc | lớp kép | lớp kép **hoặc lớp đơn** (tetraether nối xuyên màng – ở loài ưa nhiệt) |
| Glycerol | D-glycerol | L-glycerol [mở rộng] |

Lớp đơn tetraether không tách đôi được khi nóng → giúp archaea ưa nhiệt giữ màng ổn định ở > 80 °C.
"""),
("4. Các nhóm sinh lý chính", """
| Nhóm | Môi trường | Ví dụ |
|---|---|---|
| **Methanogens** (sinh methane) | kỵ khí nghiêm ngặt: bùn, dạ cỏ, ruột, bể biogas; biến CO₂ + H₂ → **CH₄** | *Methanobacterium* |
| **Extreme halophiles** (cực ưa mặn) | muối **15–30 %**: hồ muối, ruộng muối | *Halobacterium* (sắc tố bacteriorhodopsin) |
| **Extreme thermophiles / hyperthermophiles** | **> 80 °C**, suối nóng, miệng phun thủy nhiệt | *Pyrodictium, Sulfolobus* |

> *Halobacterium* là **archaea** dù tên có chữ "bacterium" – đừng đoán miền theo tên.
"""),
("5. So sánh ba miền", """
| Đặc điểm | Bacteria | Archaea | Eukarya |
|---|---|---|---|
| Nhân có màng | không | không | **có** |
| Bào quan có màng | không | không | có |
| Thành | **peptidoglycan** | **pseudomurein / lớp S**, không peptidoglycan | cellulose, chitin hoặc không |
| Lipid màng | ester, acid béo | **ether, isoprenoid** | ester, acid béo |
| Ribosome | 70S | 70S | 80S |
| Nhạy kháng sinh (streptomycin, chloramphenicol) | có | **không** | không |
"""),
],
[
("Ứng dụng công nghiệp", """
- **Biogas**: methanogens trong bể ủ kỵ khí chuyển chất thải chăn nuôi thành CH₄ – năng lượng sạch cho nông hộ.
- **Enzyme chịu nhiệt**: DNA polymerase *Pfu* (*Pyrococcus furiosus*) dùng trong PCR độ chính xác cao.
- Methanogens trong dạ cỏ bò thải CH₄ – khí nhà kính mạnh gấp ~28 lần CO₂; nhiều nghiên cứu phụ gia thức ăn nhằm ức chế chúng.
"""),
],
[
("Archaea basics", "Prokaryotes forming a separate **domain**. No peptidoglycan; some have **pseudomurein** (NAT instead of NAM, **no D-amino acids**, β-1,3 links) or an S-layer. Not known to cause human disease.", "Không peptidoglycan; pseudomurein có NAT."),
("Archaeal membranes", "Lipids are **ether-linked** to glycerol and made of **branched isoprenoid** chains; some form **monolayers** (tetraethers) that are stable at high temperature. Bacterial lipids are ester-linked fatty acids.", "Liên kết ether, chuỗi isoprenoid."),
("Groups", "**Methanogens** (anaerobic, make CH₄), **extreme halophiles** (15–30 % salt, *Halobacterium*), **extreme thermophiles** (> 80 °C).", "Sinh methane, ưa mặn, ưa nhiệt."),
],
["Archaea have peptidoglycan", "Halobacterium is a bacterium", "Pseudomurein contains NAM"])

q("BAC-08", "recall", 1, "Pseudomurein, found in the walls of some archaea, differs from peptidoglycan because it contains:",
  ["N-acetyl talosaminuronic acid instead of NAM and no D-amino acids", "teichoic acid and LPS", "chitin and glucan", "more D-amino acids than peptidoglycan"], 0,
  "Slide 76: pseudomurein chứa **NAT thay NAM** và **không có D-amino acid**.",
  ["", "Không.", "Đó là thành nấm.", "Ngược lại."], ["pseudomurein"], "Pseudomurein contains NAM", src=SRC + " slide 76")
q("BAC-08", "concept", 2, "Why are archaea naturally resistant to penicillin and lysozyme?",
  ["They have an outer membrane like Gram-negative bacteria", "They lack typical peptidoglycan, the target of both agents", "They produce β-lactamase", "They have 80S ribosomes"], 1,
  "Penicillin và lysozyme đều nhắm **peptidoglycan**; archaea **không có** (pseudomurein với liên kết β-1,3 không bị lysozyme cắt).",
  ["Không phải lý do chung.", "", "Không phải lý do.", "Archaea có ribosome 70S."], ["pseudomurein"], "Archaea have peptidoglycan")
q("BAC-08", "concept", 2, "Archaeal membrane lipids differ from bacterial lipids in that they:",
  ["are ester-linked straight fatty acids", "are ether-linked branched isoprenoid chains, sometimes forming monolayers", "contain cholesterol", "lack glycerol"], 1,
  "Archaea: **ether + isoprenoid phân nhánh**, có thể tạo **lớp đơn tetraether** chịu nhiệt.",
  ["Đó là vi khuẩn.", "", "Sai.", "Có glycerol."], ["ether lipid"])
q("BAC-08", "recall", 1, "Archaea that produce methane from CO2 and H2 in anaerobic environments are called:",
  ["extreme halophiles", "methanogens", "thermophiles", "cyanobacteria"], 1,
  "**Methanogens** – kỵ khí nghiêm ngặt, tạo **CH₄** (bể biogas, dạ cỏ).",
  ["Ưa mặn.", "", "Ưa nhiệt.", "Vi khuẩn quang hợp."], ["methanogen"])
q("BAC-08", "not", 2, "Which statement about archaea is NOT correct?",
  ["They are prokaryotes", "Some live in extremely salty or hot environments", "Halobacterium is a member of the domain Bacteria", "They lack typical peptidoglycan"], 2,
  "***Halobacterium*** là **archaea** (cực ưa mặn) dù tên có \"bacterium\".",
  ["Đúng.", "Đúng.", "", "Đúng."], ["extreme halophile"], "Halobacterium is a bacterium")
q("BAC-08", "application", 2, "A prokaryote grows at 95 °C in a hydrothermal vent, is not inhibited by penicillin and has ether-linked membrane lipids. It is most likely:",
  ["a Gram-positive bacterium", "a hyperthermophilic archaeon", "a fungus", "a mycoplasma"], 1,
  "Nhiệt độ cực cao + không nhạy penicillin + **lipid ether** → **archaea ưa nhiệt cực độ**.",
  ["Vi khuẩn có lipid ester.", "", "Nấm là nhân thực, không sống ở 95 °C.", "Mycoplasma có lipid ester và sterol."], ["hyperthermophile", "ether lipid"], pool="mock")
q("BAC-08", "concept", 2, "Which feature do archaea share with bacteria rather than with eukaryotes?",
  ["Ether-linked lipids", "No membrane-bound nucleus and 70S ribosomes", "Pseudomurein", "Cellulose cell walls"], 1,
  "Archaea và Bacteria đều **nhân sơ**, không nhân có màng, ribosome **70S**.",
  ["Chỉ archaea có.", "", "Chỉ một số archaea.", "Ở thực vật."], ["prokaryote"], pool="mock")
q("BAC-08", "recall", 1, "Extreme halophiles are archaea that require:",
  ["temperatures above 80 °C", "high salt concentrations (about 15–30%)", "strictly anaerobic conditions to make methane", "low pH below 2 only"], 1,
  "Cực ưa mặn cần muối **cao** (15–30 %), ví dụ *Halobacterium*.",
  ["Đó là ưa nhiệt.", "", "Đó là methanogen.", "Không đúng."], ["extreme halophile"], pool="mock")

v("BAC-08", "archaea", "vi khuẩn cổ", "Prokaryotes of the domain Archaea, lacking peptidoglycan.", "Many archaea live in extreme environments.", ["archaeon", "Archaea"])
v("BAC-08", "pseudomurein", "pseudomurein (giả peptidoglycan)", "Archaeal wall polymer with NAT instead of NAM and no D-amino acids.", "Lysozyme cannot digest pseudomurein.", ["pseudopeptidoglycan"])
v("BAC-08", "ether lipid", "lipid liên kết ether", "Membrane lipid with branched isoprenoid chains ether-linked to glycerol.", "Archaeal membranes are made of ether lipids.", ["ether-linked"])
v("BAC-08", "methanogen", "vi sinh vật sinh methane", "Anaerobic archaeon that produces methane.", "Methanogens work in biogas digesters.", ["methanogens"])
v("BAC-08", "extreme halophile", "vi sinh vật cực ưa mặn", "An organism requiring very high salt concentrations.", "Halobacterium is an extreme halophile.", ["extreme halophiles"])
v("BAC-08", "hyperthermophile", "vi sinh vật ưa nhiệt cực độ", "An organism growing optimally above about 80 °C.", "Pyrodictium is a hyperthermophile.", ["extreme thermophile", "hyperthermophiles"])

fc("BAC-08", "fact", "Pseudomurein vs peptidoglycan?", "Pseudomurein has NAT (N-acetyl talosaminuronic acid) instead of NAM and no D-amino acids.")
fc("BAC-08", "fact", "Archaeal vs bacterial membrane lipids?", "Archaea: ether-linked branched isoprenoids (can form monolayers). Bacteria: ester-linked fatty acids.")
fc("BAC-08", "fact", "Three main physiological groups of archaea?", "Methanogens, extreme halophiles, extreme thermophiles.")
fc("BAC-08", "trap", "TRUE/FALSE: Halobacterium belongs to the domain Bacteria.", "FALSE – it is an archaeon.")
