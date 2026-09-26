from _lib import *

S5 = "5.Microbial Growth.pptx"
S6 = "6.The Growth of Bacterial Cultures.pptx"

# ---------------------------------------------------------------- GRO-01
unit("GRO-01", "Physical requirements: temperature, pH and osmotic pressure", "H", 2, 20, S5 + ": slides 1–10",
"""Tủ lạnh 4 °C giữ thịt tươi được vài ngày chứ **không mãi mãi** – vì có những vi khuẩn **ưa lạnh/chịu lạnh** vẫn mọc chậm ở nhiệt độ này và làm thịt hỏng. Ngược lại, suối nước nóng 80 °C vẫn đầy sự sống. Mỗi vi sinh vật có **nhiệt độ tối thiểu, tối ưu và tối đa** riêng, cùng với khoảng **pH** và **nồng độ muối** chịu được.""",
("Food kept in a refrigerator (4 °C) eventually spoils mainly because of:",
 ["thermophiles", "psychrotrophs that can grow slowly at low temperatures", "hyperthermophiles", "obligate anaerobes only"], 1,
 "**Psychrotrophs** (và psychrophiles) vẫn sinh trưởng chậm ở 0–7 °C → nguyên nhân chính làm hỏng thực phẩm bảo quản lạnh."),
[
("1. Nhiệt độ (slide 3–4)", """
Mỗi loài có 3 **nhiệt độ cơ bản**: **tối thiểu** (thấp nhất còn mọc), **tối ưu** (mọc nhanh nhất), **tối đa** (cao nhất còn mọc). Tối ưu thường **gần tối đa** hơn – trên tối ưu một chút, tốc độ rơi rất nhanh vì enzyme biến tính.

| Nhóm | Tên | Khoảng tối ưu (xấp xỉ) [fig] | Ví dụ/ghi chú |
|---|---|---|---|
| **Psychrophiles** | ưa lạnh | ~**15 °C** (mọc được ở 0 °C) | sống ở đại dương sâu, vùng cực |
| **Psychrotrophs** | chịu lạnh | 20–30 °C, nhưng **mọc được ở 0–7 °C** | **gây hỏng thực phẩm trong tủ lạnh** (*Listeria, Pseudomonas*) |
| **Mesophiles** | ưa ấm | **25–40 °C** (vi khuẩn gây bệnh ~**37 °C**) | phần lớn vi khuẩn, nấm |
| **Thermophiles** | ưa nhiệt | **50–60 °C** | suối nóng, ủ phân compost |
| **Hyperthermophiles** (extreme thermophiles) | ưa nhiệt cực độ | **≥ 80 °C** | chủ yếu **archaea** |

- Lạnh chủ yếu **kìm hãm**, không diệt; nóng quá ngưỡng tối đa làm hỏng protein, màng không hồi phục.
"""),
("2. pH (slide 5)", """
- **Phần lớn vi khuẩn mọc tốt ở pH 6,5–7,5**.
- **Rất ít vi khuẩn mọc được ở pH < 4**; một số **chịu acid (acid-tolerant)** như vi khuẩn lactic, *Acidithiobacillus*.
- **Nấm men và nấm mốc** thường mọc tốt ở **pH 5–6** (hơi acid) → môi trường nuôi nấm (Sabouraud, PDA) có pH thấp hơn.
- Vi sinh vật tạo acid/kiềm khi sinh trưởng → pH thay đổi → cần bổ sung **chất đệm (buffers)**: **peptone, amino acid, muối phosphate**…
- Phân loại theo pH: **acidophiles** (ưa acid), **neutrophiles** (trung tính), **alkaliphiles** (ưa kiềm). [mở rộng]
"""),
("3. Áp suất thẩm thấu (slide 6–9)", """
- Vi khuẩn **cần nước** để sinh trưởng (tế bào ~80 % là nước).
- **Áp suất thẩm thấu cao** rút nước ra khỏi tế bào. Khi tế bào ở trong dung dịch **ưu trương** (nồng độ chất tan cao hơn trong tế bào), nước đi ra qua màng → **co nguyên sinh (plasmolysis)** – tế bào chất co lại → ức chế sinh trưởng. Đây là nguyên lý bảo quản bằng **muối, đường**.
- **Extreme halophiles** (cực ưa mặn, **obligate halophiles**): **cần nồng độ muối cao** để sinh trưởng (~30 %; ví dụ archaea *Halobacterium*).
- **Facultative halophiles** (ưa mặn tùy nghi): **không cần** muối cao nhưng **mọc được ở nồng độ muối tới 2 %** – nồng độ ức chế nhiều sinh vật khác.
- ! Một vài loài facultative halophile **chịu được cả 15 % muối** (ví dụ *Staphylococcus aureus*).
- Trong môi trường **nhược trương** (nước cất), vi khuẩn có thành vẫn chịu được; mất thành → vỡ.
"""),
],
[
("Thực phẩm: \"vùng nguy hiểm\" 5–60 °C", """
Vi khuẩn gây bệnh thực phẩm (mesophiles) mọc nhanh nhất trong khoảng **5–60 °C**, đặc biệt ~37 °C. Quy tắc an toàn: giữ đồ nóng **> 60 °C**, đồ lạnh **< 5 °C**, không để thức ăn chín ở nhiệt độ phòng quá 2 giờ. *Listeria monocytogenes* là psychrotroph nguy hiểm vì mọc được cả trong tủ lạnh.
"""),
("Công nghệ: ủ phân compost", """
Đống ủ phân tự nóng lên **55–70 °C** do trao đổi chất của vi sinh vật: giai đoạn đầu mesophiles hoạt động, sau đó **thermophiles** thay thế và **diệt mầm bệnh, hạt cỏ dại**. Enzyme chịu nhiệt từ thermophiles (amylase, protease) dùng trong bột giặt.
"""),
],
[
("Temperature groups", "Each species has **minimum, optimum and maximum** growth temperatures. **Psychrophiles** (cold-loving, optimum ~15 °C), **psychrotrophs** (grow at 0–7 °C; spoil refrigerated food), **mesophiles** (25–40 °C; pathogens ~37 °C), **thermophiles** (50–60 °C), **hyperthermophiles** (≥ 80 °C).", "Ưa lạnh – ưa ấm – ưa nhiệt."),
("pH", "Most bacteria grow best at **pH 6.5–7.5**; very few below pH 4; some are acid-tolerant. **Yeasts and molds prefer pH 5–6**. Media contain **buffers** (peptone, amino acids, phosphate salts).", "Vi khuẩn 6,5–7,5; nấm 5–6."),
("Osmotic pressure", "Hypertonic solutions draw water out → **plasmolysis**. **Extreme halophiles** require high salt. **Facultative halophiles** do not require salt but grow at up to **2 %**; a few tolerate **15 %**.", "Co nguyên sinh; ưa mặn bắt buộc vs tùy nghi."),
],
["Refrigeration kills bacteria", "Molds prefer pH 7.5", "Facultative halophiles require high salt"])

q("GRO-01", "recall", 1, "According to the lecture, most bacteria grow best at pH:",
  ["2.0–3.5", "5.0–6.0", "6.5–7.5", "9.0–10.0"], 2,
  "Slide 5: **phần lớn vi khuẩn 6,5–7,5**; nấm men và nấm mốc 5–6.",
  ["Rất ít vi khuẩn mọc < 4.", "Đó là nấm men/mốc.", "", "Chỉ vi sinh vật ưa kiềm."], ["pH"], src=S5 + " slide 5")
q("GRO-01", "recall", 1, "Yeasts and molds generally grow best at pH:",
  ["5–6", "7–8", "9–10", "1–2"], 0,
  "Slide 5: **nấm men và nấm mốc pH 5–6**.",
  ["", "Gần trung tính của vi khuẩn.", "Kiềm.", "Quá acid."], ["pH"], "Molds prefer pH 7.5", src=S5 + " slide 5")
q("GRO-01", "concept", 2, "Facultative halophiles are organisms that:",
  ["require at least 30% salt", "do not require high salt but can grow at up to 2% salt (a few up to 15%)", "cannot tolerate any salt", "grow only in fresh water"], 1,
  "Slide 9: **facultative halophiles** không cần muối cao nhưng mọc được tới **2 %**; một vài loài chịu **15 %**.",
  ["Đó là extreme halophiles.", "", "Sai.", "Sai."], ["facultative halophile"], "Facultative halophiles require high salt", src=S5 + " slide 9")
q("GRO-01", "concept", 2, "What happens to a bacterial cell placed in a solution with a much higher solute concentration than its cytoplasm?",
  ["It swells and bursts", "Water leaves the cell and plasmolysis occurs", "Salt enters and the cell grows faster", "Nothing, because the wall is impermeable"], 1,
  "Slide 7: môi trường **ưu trương** → nước đi ra → **co nguyên sinh (plasmolysis)**.",
  ["Xảy ra ở nhược trương khi mất thành.", "", "Sai.", "Thành cho nước đi qua."], ["plasmolysis", "hypertonic"], src=S5 + " slide 7")
q("GRO-01", "application", 2, "Listeria can multiply in refrigerated ready-to-eat foods. It is best described as a:",
  ["thermophile", "psychrotroph", "hyperthermophile", "obligate halophile"], 1,
  "Mọc được ở 0–7 °C (tủ lạnh) nhưng tối ưu cao hơn → **psychrotroph**.",
  ["Ưa nóng.", "", "Ưa nhiệt cực độ.", "Cần muối cao."], ["psychrotroph"], "Refrigeration kills bacteria")
q("GRO-01", "concept", 2, "Why are buffers such as peptone, amino acids and phosphate salts added to culture media?",
  ["To provide trace elements only", "To resist pH changes caused by microbial metabolism", "To solidify the medium", "To kill contaminants"], 1,
  "Slide 5: vi sinh vật tạo acid/kiềm → pH thay đổi → cần **chất đệm** để giữ pH.",
  ["Không phải mục đích chính.", "", "Đó là agar.", "Sai."], ["buffer"])
q("GRO-01", "recall", 1, "Human pathogens are typically:",
  ["psychrophiles", "mesophiles with optimum near 37 °C", "thermophiles", "hyperthermophiles"], 1,
  "Mầm bệnh ở người là **mesophiles**, tối ưu ~37 °C (thân nhiệt).",
  ["Sai.", "", "Sai.", "Sai."], ["mesophile"], pool="mock")
q("GRO-01", "not", 2, "Which statement about temperature and microbial growth is NOT correct?",
  ["Each species has minimum, optimum and maximum growth temperatures", "Thermophiles grow best at about 50–60 °C", "Psychrophiles grow best at about 37 °C", "Low temperature generally slows growth rather than killing"], 2,
  "Psychrophiles tối ưu ~**15 °C**; 37 °C là của mesophiles.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["psychrophile"], pool="mock")
q("GRO-01", "recall", 1, "Organisms that require high salt concentrations for growth are called:",
  ["facultative halophiles", "extreme (obligate) halophiles", "psychrophiles", "acidophiles"], 1,
  "Slide 9: **extreme halophiles** cần nồng độ muối cao.",
  ["Không cần muối cao.", "", "Ưa lạnh.", "Ưa acid."], ["extreme halophile"], pool="mock")

v("GRO-01", "psychrophile", "vi sinh vật ưa lạnh", "An organism growing best at low temperatures (about 15 °C).", "Psychrophiles live in polar seas.", ["psychrophiles"])
v("GRO-01", "psychrotroph", "vi sinh vật chịu lạnh", "An organism that grows at 0–7 °C but has a higher optimum; spoils refrigerated food.", "Listeria is a psychrotroph.", ["psychrotrophs"])
v("GRO-01", "mesophile", "vi sinh vật ưa ấm", "An organism growing best at moderate temperatures (25–40 °C).", "Most pathogens are mesophiles.", ["mesophiles"])
v("GRO-01", "thermophile", "vi sinh vật ưa nhiệt", "An organism growing best at 50–60 °C.", "Thermophiles thrive in compost.", ["thermophiles"])
v("GRO-01", "optimum growth temperature", "nhiệt độ sinh trưởng tối ưu", "The temperature at which a species grows fastest.", "The optimum growth temperature of E. coli is 37 °C.", ["minimum growth temperature", "maximum growth temperature"])
v("GRO-01", "pH", "pH", "A measure of acidity; most bacteria prefer 6.5–7.5.", "Molds tolerate low pH.")
v("GRO-01", "buffer", "chất đệm", "A substance that resists changes in pH.", "Phosphate salts act as a buffer.", ["buffers"])
v("GRO-01", "facultative halophile", "vi sinh vật ưa mặn tùy nghi", "Does not require salt but tolerates up to 2% (some 15%).", "Staphylococcus aureus is a facultative halophile.", ["facultative halophiles"])

fc("GRO-01", "fact", "Five temperature groups?", "Psychrophiles (~15 °C), psychrotrophs (grow 0–7 °C), mesophiles (25–40 °C), thermophiles (50–60 °C), hyperthermophiles (≥80 °C).")
fc("GRO-01", "number", "pH optimum: bacteria vs yeasts/molds?", "Bacteria 6.5–7.5 (few below 4); yeasts/molds 5–6.")
fc("GRO-01", "number", "Facultative halophiles tolerate?", "Up to 2% salt; a few up to 15%.")
fc("GRO-01", "trap", "TRUE/FALSE: refrigeration sterilizes food.", "FALSE – it is bacteriostatic; psychrotrophs still grow.")

# ---------------------------------------------------------------- GRO-02
unit("GRO-02", "Chemical requirements: C, N, S, P, trace elements and growth factors", "H", 2, 20, S5 + ": slides 11–20",
"""Nông dân trồng đậu tương gần như **không cần bón đạm**. Bí mật nằm ở các **nốt sần trên rễ**: vi khuẩn *Rhizobium* sống cộng sinh, biến **N₂ trong không khí** thành dạng cây dùng được. Mỗi vi sinh vật cần **C, N, S, P**, nguyên tố vi lượng và đôi khi cả "vitamin" – nhưng lấy từ nguồn nào thì mỗi loài một khác.""",
("Soybean plants need little nitrogen fertilizer because:",
 ["their leaves absorb NH3 from air", "symbiotic bacteria in root nodules fix atmospheric N2", "they do not need nitrogen", "soil fungi produce nitrate"], 1,
 "Slide 16: vi khuẩn cố định đạm sống **cộng sinh với rễ cây họ đậu** (đậu tương, đậu, cỏ ba lá…) → **cố định N₂**, cả cây và vi khuẩn cùng dùng."),
[
("1. Carbon (slide 11–13)", """
- Ngoài nước, **carbon** là một trong những nhu cầu **quan trọng nhất**: là **bộ khung** của mọi hợp chất hữu cơ.
- **Một nửa khối lượng khô** của tế bào vi khuẩn là **carbon**.
- **Kiểu dinh dưỡng** [fig]:
| Kiểu | Nguồn năng lượng | Nguồn carbon | Ví dụ |
|---|---|---|---|
| **Chemoheterotroph** | hóa học (chất hữu cơ) | **hữu cơ** (protein, carbohydrate, lipid) – **cùng nguồn với năng lượng** | phần lớn vi khuẩn, nấm, động vật nguyên sinh |
| **Chemoautotroph** | hóa học (chất vô cơ: H₂S, NH₃, Fe²⁺) | **CO₂** | vi khuẩn nitrat hóa, oxy hóa lưu huỳnh |
| **Photoautotroph** | ánh sáng | **CO₂** | vi khuẩn lam, tảo |
| **Photoheterotroph** | ánh sáng | hữu cơ | vi khuẩn không lưu huỳnh màu tía/lục [mở rộng] |
"""),
("2. Nitơ, lưu huỳnh, phospho (slide 15–17)", """
Cần để tổng hợp **protein, DNA, RNA, ATP, phospholipid**…

**Nitơ (N)**:
- Nhiều vi khuẩn **phân giải thực phẩm chứa protein** và hợp chất chứa N khác; loài khác lấy N từ **NH₄⁺, NO₃⁻**…
- **Vi khuẩn lam (cyanobacteria)** dùng trực tiếp **N₂ khí quyển** – **cố định đạm (nitrogen fixation)**.
- Vi sinh vật cố định đạm có loài **sống tự do** (chủ yếu trong đất), loài **cộng sinh với rễ cây họ đậu** (cỏ ba lá, đậu tương, cỏ linh lăng, đậu, đậu Hà Lan) – N cố định được **cả cây và vi khuẩn** sử dụng.

**Lưu huỳnh (S)**:
- Tổng hợp **amino acid chứa S** (cysteine, methionine) và **vitamin** như **thiamine, biotin**.
- Nguồn: **SO₄²⁻, H₂S, amino acid chứa S**.

**Phospho (P)**:
- Cần cho **acid nucleic**, **phospholipid** màng, và **liên kết năng lượng của ATP**.
- Nguồn quan trọng: **PO₄³⁻** (phosphate).
"""),
("3. Nguyên tố vi lượng (slide 18)", """
- **Trace elements**: **Fe²⁺, Cu²⁺, Mo, Zn²⁺**… cần với lượng **rất nhỏ**; phần lớn là **cofactor** của enzyme.
- Bên cạnh đó **K⁺, Mg²⁺, Ca²⁺**… là các yếu tố quan trọng cho sinh trưởng, cũng là cofactor enzyme (cần lượng lớn hơn).
- Thường **không cần bổ sung** vì có sẵn trong **nước máy** và các thành phần môi trường.
"""),
("4. Yếu tố sinh trưởng hữu cơ (slide 19–20)", """
- **Organic growth factors**: hợp chất hữu cơ **thiết yếu** mà sinh vật **không tự tổng hợp được** → phải lấy **trực tiếp từ môi trường**. Với người, nhóm quan trọng là **vitamin**.
- Phần lớn vitamin là **coenzyme** – cofactor hữu cơ enzyme cần để hoạt động.
- Nhiều vi khuẩn **tự tổng hợp mọi vitamin**; một số thiếu enzyme → vitamin đó là yếu tố sinh trưởng. Yếu tố sinh trưởng khác: **amino acid, purine, pyrimidine**.
- Vi sinh vật có nhu cầu dinh dưỡng phức tạp gọi là **fastidious** (khó nuôi). [mở rộng]
"""),
],
[
("Nông nghiệp: phân bón vi sinh", """
Chế phẩm **Rhizobium** (nốt sần cây họ đậu), **Azotobacter** (cố định N tự do), vi khuẩn **phân giải lân** (hòa tan phosphate khó tan) được bán làm **phân vi sinh** ở Việt Nam – giảm phân hóa học, cải tạo đất. Vi khuẩn lam *Anabaena* cộng sinh với bèo hoa dâu (*Azolla*) từng là "phân xanh" cho lúa nước.
"""),
("Công nghệ lên men: công thức môi trường", """
Khi thiết kế môi trường công nghiệp, kỹ sư tính **tỉ lệ C:N** (ví dụ SCP ~10:1 – bài APP-02), bổ sung nguồn N rẻ (urê, (NH₄)₂SO₄), P (KH₂PO₄), Mg (MgSO₄) và dựa vào nước/nguyên liệu thô (rỉ đường, bột ngô) để cung cấp vi lượng và vitamin.
"""),
],
[
("Carbon", "Carbon is the backbone of organic compounds; **half the dry weight** of a bacterium is carbon. **Chemoheterotrophs** get carbon from their energy source (organic compounds). **Chemoautotrophs** and **photoautotrophs** use **CO₂**.", "Nửa khối lượng khô là carbon."),
("N, S, P", "N, S, P are needed for proteins, DNA, RNA, ATP, phospholipids. N from proteins, **NH₄⁺, NO₃⁻**, or **N₂ by nitrogen fixation** (cyanobacteria; symbionts of legume roots). **S**: S-amino acids, **thiamine, biotin**; sources SO₄²⁻, H₂S. **P**: nucleic acids, phospholipids, **ATP**; source PO₄³⁻.", "N – cố định đạm; S – thiamine, biotin; P – ATP."),
("Trace elements and growth factors", "**Trace elements** (Fe, Cu, Mo, Zn) are needed in tiny amounts as enzyme **cofactors** and are usually present in tap water. **Organic growth factors** are organic compounds an organism cannot synthesize (vitamins as **coenzymes**, amino acids, purines, pyrimidines).", "Vi lượng = cofactor; yếu tố sinh trưởng = hữu cơ không tự tổng hợp."),
],
["Trace elements must always be added", "Chemoautotrophs use glucose as carbon source", "All cyanobacteria fix nitrogen"])

q("GRO-02", "recall", 1, "About what fraction of the dry weight of a typical bacterial cell is carbon?",
  ["One tenth", "One quarter", "One half", "Nine tenths"], 2,
  "Slide 11: **một nửa khối lượng khô** là carbon.",
  ["Sai.", "Sai.", "", "Sai."], ["carbon"], src=S5 + " slide 11")
q("GRO-02", "concept", 2, "A bacterium obtains energy by oxidizing H2S and uses CO2 as its carbon source. It is a:",
  ["chemoheterotroph", "chemoautotroph", "photoautotroph", "photoheterotroph"], 1,
  "Năng lượng **hóa học** (H₂S) + carbon từ **CO₂** = **chemoautotroph**.",
  ["Dùng carbon hữu cơ.", "", "Năng lượng ánh sáng.", "Ánh sáng + hữu cơ."], ["chemoautotroph"], "Chemoautotrophs use glucose as carbon source")
q("GRO-02", "recall", 1, "Sulfur is used by bacteria to synthesize:",
  ["nucleic acids and ATP", "sulfur-containing amino acids and vitamins such as thiamine and biotin", "phospholipids only", "peptidoglycan"], 1,
  "Slide 17: S → **amino acid chứa S**, **thiamine, biotin**.",
  ["Đó là P.", "", "Đó là P.", "Sai."], ["sulfur"], src=S5 + " slide 17")
q("GRO-02", "recall", 1, "Phosphorus is essential for bacterial synthesis of:",
  ["nucleic acids, membrane phospholipids and ATP", "thiamine and biotin", "chitin", "flagellin only"], 0,
  "Slide 17: P cần cho **acid nucleic, phospholipid, liên kết năng lượng ATP**; nguồn PO₄³⁻.",
  ["", "Đó là S.", "Sai.", "Sai."], ["phosphorus"], src=S5 + " slide 17")
q("GRO-02", "concept", 2, "An organic compound that an organism needs but cannot synthesize, and must obtain from the environment, is called:",
  ["a trace element", "an organic growth factor", "an inoculum", "a buffer"], 1,
  "Slide 19: **organic growth factor** (vitamin, amino acid, purine, pyrimidine).",
  ["Vi lượng là nguyên tố vô cơ.", "", "Sai.", "Sai."], ["organic growth factor"])
q("GRO-02", "concept", 2, "Why are trace elements usually not added to laboratory media?",
  ["They are toxic", "They are assumed to be naturally present in tap water and other media components", "Bacteria do not need them", "They precipitate agar"], 1,
  "Slide 18: vi lượng thường **có sẵn trong nước máy** và các thành phần môi trường.",
  ["Không phải lý do.", "", "Vẫn cần, với lượng rất nhỏ.", "Sai."], ["trace elements"], "Trace elements must always be added", src=S5 + " slide 18")
q("GRO-02", "not", 2, "Which statement about nitrogen fixation is NOT correct according to the lecture?",
  ["Cyanobacteria can use atmospheric N2", "Some nitrogen fixers are free-living in soil", "Some live symbiotically with legume roots", "The fixed nitrogen is used only by the plant, never by the bacterium"], 3,
  "Slide 16: N cố định trong cộng sinh được **cả cây và vi khuẩn** sử dụng.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["nitrogen fixation"], pool="mock")
q("GRO-02", "recall", 1, "Most vitamins function in cells as:",
  ["structural proteins", "coenzymes (organic cofactors of enzymes)", "energy storage granules", "cell wall components"], 1,
  "Slide 19: phần lớn vitamin là **coenzyme**.",
  ["Sai.", "", "Sai.", "Sai."], ["coenzyme"], pool="mock")
q("GRO-02", "concept", 2, "Chemoheterotrophs differ from photoautotrophs because chemoheterotrophs:",
  ["use light and CO2", "obtain both energy and most carbon from organic compounds", "use inorganic compounds for energy and CO2 for carbon", "cannot use proteins"], 1,
  "Slide 12: chemoheterotroph lấy **carbon từ chính nguồn năng lượng** – chất hữu cơ.",
  ["Photoautotroph.", "", "Chemoautotroph.", "Sai."], ["chemoheterotroph"], pool="mock")

v("GRO-02", "chemoheterotroph", "hóa dị dưỡng", "Uses organic compounds for energy and carbon.", "E. coli is a chemoheterotroph.", ["chemoheterotrophs"])
v("GRO-02", "chemoautotroph", "hóa tự dưỡng", "Uses inorganic chemicals for energy and CO2 for carbon.", "Nitrifying bacteria are chemoautotrophs.", ["chemoautotrophs"])
v("GRO-02", "photoautotroph", "quang tự dưỡng", "Uses light for energy and CO2 for carbon.", "Cyanobacteria are photoautotrophs.", ["photoautotrophs"])
v("GRO-02", "nitrogen fixation", "cố định đạm", "Conversion of atmospheric N2 into usable nitrogen compounds.", "Rhizobium performs nitrogen fixation in legume roots.")
v("GRO-02", "trace elements", "nguyên tố vi lượng", "Elements needed in tiny amounts, e.g., Fe, Cu, Mo, Zn.", "Trace elements are present in tap water.", ["trace element"])
v("GRO-02", "cofactor", "đồng yếu tố", "A non-protein helper required by some enzymes.", "Mg2+ is an enzyme cofactor.", ["cofactors"])
v("GRO-02", "coenzyme", "coenzyme", "An organic cofactor, often derived from a vitamin.", "NAD+ is a coenzyme.", ["coenzymes"])
v("GRO-02", "organic growth factor", "yếu tố sinh trưởng hữu cơ", "An essential organic compound an organism cannot synthesize.", "Vitamins are organic growth factors for some bacteria.", ["organic growth factors", "growth factor"])

fc("GRO-02", "fact", "Carbon fraction of bacterial dry weight?", "About one half.")
fc("GRO-02", "fact", "Uses of N, S, P?", "N: proteins, nucleic acids. S: S-amino acids, thiamine, biotin. P: nucleic acids, phospholipids, ATP.")
fc("GRO-02", "fact", "Nitrogen fixers in the lecture?", "Cyanobacteria; free-living soil bacteria; symbionts of legume roots (clover, soybean, alfalfa, beans, peas).")
fc("GRO-02", "fact", "Examples of organic growth factors?", "Vitamins (coenzymes), amino acids, purines, pyrimidines.")

# ---------------------------------------------------------------- GRO-03
unit("GRO-03", "Oxygen requirements and toxic forms of oxygen", "H", 2, 20, S5 + ": slides 21–27",
"""Vết thương sâu do đạp đinh gỉ nguy hiểm hơn vết xước ngoài da – vì trong mô sâu **không có oxy**, nơi lý tưởng cho *Clostridium tetani* (uốn ván), một vi khuẩn **kỵ khí bắt buộc**: oxy **giết** nó. Nhưng tại sao oxy – thứ nuôi sống chúng ta – lại độc với nó?""",
("Why is oxygen toxic to obligate anaerobes?",
 ["Oxygen dissolves their cell walls", "They lack enzymes such as superoxide dismutase and catalase to neutralize toxic forms of oxygen", "Oxygen blocks their flagella", "They use oxygen as a nutrient too quickly"], 1,
 "Trao đổi chất có oxy tạo **superoxide, H₂O₂**… Kỵ khí bắt buộc **thiếu SOD và catalase** nên bị các dạng oxy độc phá hủy."),
[
("1. Năm nhóm theo nhu cầu oxy (slide 21–22)", """
Vi khuẩn **dùng O₂** tạo được **nhiều năng lượng** hơn từ chất dinh dưỡng.
| Nhóm | Đặc điểm | Vị trí mọc trong ống thạch thioglycolate [fig] |
|---|---|---|
| **Obligate aerobes** (hiếu khí bắt buộc) | **cần O₂** để sống | **trên bề mặt** |
| **Facultative anaerobes** (kỵ khí tùy nghi) | **dùng O₂ khi có**; khi không có thì **lên men hoặc hô hấp kỵ khí** | khắp ống, **dày nhất ở trên** |
| **Obligate anaerobes** (kỵ khí bắt buộc) | **không dùng** O₂; phần lớn **bị O₂ làm hại** | **chỉ ở đáy** |
| **Aerotolerant anaerobes** (kỵ khí chịu oxy) | **lên men**, không dùng O₂ nhưng **chịu được** O₂; vi khuẩn lactic có **SOD** trung hòa superoxide | **đều khắp ống** |
| **Microaerophiles** (vi hiếu khí) | hiếu khí nhưng cần **lượng O₂ nhỏ** (thấp hơn không khí) | **dải hẹp dưới bề mặt** |

Ví dụ [mở rộng]: *Pseudomonas, Micrococcus* (hiếu khí bắt buộc); *E. coli, S. cerevisiae* (kỵ khí tùy nghi); *Clostridium* (kỵ khí bắt buộc); *Lactobacillus, Streptococcus* (chịu oxy); *Campylobacter, Helicobacter* (vi hiếu khí).
"""),
("2. Các dạng oxy độc (slide 23–25)", """
| Dạng | Mô tả | Enzyme trung hòa |
|---|---|---|
| **Singlet oxygen** (¹O₂) | O₂ bình thường được **nâng lên trạng thái năng lượng cao**, **cực kỳ hoạt động** | carotenoid (sắc tố) [mở rộng] |
| **Superoxide radicals** (O₂•⁻, superoxide anion) | hình thành **lượng nhỏ trong hô hấp bình thường** của sinh vật dùng O₂ làm chất nhận electron cuối (tạo nước). Kỵ khí bắt buộc khi gặp O₂ cũng tạo superoxide. **Rất độc**: cướp electron của phân tử bên cạnh → phản ứng dây chuyền | **Superoxide dismutase (SOD)**: O₂•⁻ + O₂•⁻ + 2H⁺ → H₂O₂ + O₂ |
| **Hydrogen peroxide** (H₂O₂) | sản phẩm của SOD, vẫn độc | **Catalase**: 2H₂O₂ → 2H₂O + O₂; **Peroxidase**: H₂O₂ + 2H⁺ → 2H₂O |
| **Hydroxyl radical** (•OH) | dạng hoạt động mạnh nhất, tạo từ H₂O₂ hoặc bức xạ ion hóa | – |

- **Mọi sinh vật muốn sống trong không khí phải có SOD** để trung hòa superoxide.
- Enzyme theo nhóm: hiếu khí bắt buộc & kỵ khí tùy nghi: **SOD + catalase**; chịu oxy: **SOD**, không catalase; kỵ khí bắt buộc: **không có (hoặc rất ít)**. [fig]
- Xét nghiệm **catalase** (nhỏ H₂O₂ → sủi bọt O₂) giúp phân biệt *Staphylococcus* (+) với *Streptococcus* (−). [mở rộng]
"""),
("3. Nuôi cấy kỵ khí (slide 26–27)", """
- **Bình kỵ khí (anaerobic jar)**: gói tạo khí khi thêm nước: **NaHCO₃ + NaBH₄ + H₂O → H₂ + CO₂**; H₂ kết hợp O₂ trên **chất xúc tác palladium** → H₂O → loại O₂. Có chỉ thị methylene blue (không màu khi hết O₂). [fig]
- **Môi trường khử (reducing media)** chứa **sodium thioglycolate** kết hợp với O₂ hòa tan (bài GRO-04).
- Slide 27: **Các vi sinh vật khác cũng có nhu cầu vật lý & hóa học tương tự vi khuẩn.**
"""),
],
[
("Y tế: vết thương sâu và uốn ván", """
Vết thương đâm sâu, dập nát, ít máu nuôi → **môi trường kỵ khí** → bào tử *C. tetani* nảy mầm, tiết độc tố thần kinh. Vì vậy vết thương sâu cần **làm sạch, mở rộng** (đưa O₂ vào) và **tiêm phòng uốn ván**. Liệu pháp **oxy cao áp** điều trị hoại thư sinh hơi (*C. perfringens*).
"""),
("Công nghệ: sục khí trong nồi lên men", """
Nồi lên men hiếu khí (sản xuất penicillin, acid citric, SCP) phải **sục khí và khuấy** liên tục vì O₂ tan rất kém trong nước (~7–8 mg/L ở 25 °C). Lên men kỵ khí (ethanol, biogas, acid lactic) thì loại oxy. Hiểu nhóm oxy của vi sinh vật quyết định thiết kế thiết bị.
"""),
],
[
("Five oxygen groups", "**Obligate aerobes** require O₂. **Facultative anaerobes** use O₂ when present, otherwise ferment or respire anaerobically. **Obligate anaerobes** cannot use O₂ and are harmed by it. **Aerotolerant anaerobes** ferment but tolerate O₂ (lactic acid bacteria have **SOD**). **Microaerophiles** need less O₂ than air.", "5 nhóm theo oxy."),
("Toxic oxygen", "**Singlet oxygen**: high-energy, very reactive O₂. **Superoxide** (O₂•⁻): formed in small amounts during normal aerobic respiration; neutralized by **superoxide dismutase (SOD)** → H₂O₂ + O₂. **H₂O₂** removed by **catalase** (→ H₂O + O₂) or **peroxidase**. All organisms growing in air must make SOD.", "SOD → catalase/peroxidase."),
("Anaerobic culture", "**Anaerobic jar**: NaHCO₃ + NaBH₄ + H₂O → H₂ + CO₂; H₂ removes O₂ on a palladium catalyst. **Reducing media** contain sodium thioglycolate.", "Bình kỵ khí; môi trường thioglycolate."),
],
["Aerotolerant anaerobes use O2 for respiration", "Microaerophiles grow at the surface", "Singlet oxygen is the same as superoxide", "Obligate anaerobes have catalase"])

q("GRO-03", "concept", 2, "In a tube of thioglycolate medium, growth appears evenly throughout the tube. The organism is most likely:",
  ["an obligate aerobe", "an obligate anaerobe", "an aerotolerant anaerobe", "a microaerophile"], 2,
  "Mọc **đều khắp ống** = không dùng O₂ nhưng **chịu được** → **aerotolerant anaerobe**.",
  ["Mọc ở bề mặt.", "Mọc ở đáy.", "", "Dải hẹp dưới bề mặt."], ["aerotolerant anaerobe"], src=S5 + " slide 22")
q("GRO-03", "concept", 2, "Growth appears only as a narrow band slightly below the surface of a thioglycolate tube. The organism is a:",
  ["facultative anaerobe", "microaerophile", "obligate anaerobe", "obligate aerobe"], 1,
  "Cần **ít O₂ hơn không khí** → dải hẹp dưới bề mặt → **microaerophile**.",
  ["Mọc khắp, dày ở trên.", "", "Ở đáy.", "Ở bề mặt."], ["microaerophile"], "Microaerophiles grow at the surface")
q("GRO-03", "recall", 1, "Which enzyme converts superoxide radicals into hydrogen peroxide and oxygen?",
  ["Catalase", "Peroxidase", "Superoxide dismutase", "Transpeptidase"], 2,
  "**SOD**: O₂•⁻ + O₂•⁻ + 2H⁺ → **H₂O₂ + O₂**.",
  ["Catalase phân hủy H₂O₂.", "Peroxidase khử H₂O₂.", "", "Enzyme tạo peptidoglycan."], ["superoxide dismutase"], src=S5 + " slide 24")
q("GRO-03", "concept", 2, "Why must all organisms growing in atmospheric oxygen produce superoxide dismutase?",
  ["To produce ATP", "Because superoxide radicals formed during aerobic metabolism are extremely toxic", "To digest peptidoglycan", "To fix nitrogen"], 1,
  "Slide 24: superoxide **rất độc** (cướp electron gây phản ứng dây chuyền) → sinh vật sống trong không khí **phải có SOD**.",
  ["Sai.", "", "Sai.", "Sai."], ["superoxide", "superoxide dismutase"], src=S5 + " slide 24")
q("GRO-03", "recall", 1, "Lactic acid bacteria are fermentative and cannot use oxygen for growth but tolerate it well. They are:",
  ["obligate aerobes", "aerotolerant anaerobes", "obligate anaerobes", "microaerophiles"], 1,
  "Slide 22: **aerotolerant anaerobes** – vi khuẩn lactic có **SOD** trung hòa superoxide.",
  ["Sai.", "", "Bị O₂ làm hại.", "Cần O₂ ít."], ["aerotolerant anaerobe"], "Aerotolerant anaerobes use O2 for respiration", src=S5 + " slide 22")
q("GRO-03", "concept", 2, "Facultative anaerobes grow best near the top of a thioglycolate tube because:",
  ["oxygen is toxic to them at the bottom", "aerobic respiration yields more energy than fermentation", "they are microaerophiles", "they need light"], 1,
  "Slide 21: dùng O₂ tạo **nhiều năng lượng hơn** → mọc dày ở phía có O₂, nhưng vẫn mọc khắp ống.",
  ["O₂ không độc với chúng.", "", "Sai.", "Sai."], ["facultative anaerobe"])
q("GRO-03", "recall", 1, "Singlet oxygen is:",
  ["an anion formed during respiration", "normal molecular oxygen boosted into a higher-energy, extremely reactive state", "hydrogen peroxide", "an enzyme"], 1,
  "Slide 23: **singlet oxygen** = O₂ được **nâng lên trạng thái năng lượng cao**, cực kỳ hoạt động. Khác superoxide (anion).",
  ["Đó là superoxide.", "", "Sai.", "Sai."], ["singlet oxygen"], "Singlet oxygen is the same as superoxide")
q("GRO-03", "recall", 1, "Organisms that require molecular oxygen to live are:",
  ["obligate aerobes", "aerotolerant anaerobes", "obligate anaerobes", "facultative anaerobes"], 0,
  "Slide 21: **obligate aerobes** cần O₂ để sống.",
  ["", "Không dùng O₂.", "Bị O₂ hại.", "Không bắt buộc cần O₂."], ["obligate aerobe"], pool="mock")
q("GRO-03", "application", 2, "A bacterium bubbles vigorously when a drop of H2O2 is added to its colony. It possesses:",
  ["superoxide dismutase only", "catalase", "a capsule", "nitrogenase"], 1,
  "Sủi bọt O₂ = **catalase**: 2H₂O₂ → 2H₂O + **O₂**.",
  ["SOD không phân hủy H₂O₂.", "", "Sai.", "Sai."], ["catalase"], "Obligate anaerobes have catalase", pool="mock")
q("GRO-03", "concept", 2, "In an anaerobic jar, the gas-generating packet reacts: NaHCO3 + NaBH4 + H2O → H2 + CO2. How is oxygen then removed?",
  ["CO2 displaces O2 out of the jar", "H2 combines with O2 on a palladium catalyst to form water", "NaBH4 absorbs O2 directly", "O2 is frozen out"], 1,
  "H₂ + O₂ → H₂O nhờ **xúc tác palladium** → loại oxy.",
  ["Không.", "", "Không.", "Không."], ["anaerobic jar"], pool="mock", src=S5 + " slide 26")
q("GRO-03", "not", 2, "Which statement about obligate anaerobes is NOT correct?",
  ["They are unable to use O2 for energy-yielding reactions", "Most are harmed by O2", "They grow at the bottom of thioglycolate tubes", "They grow best at the surface of an agar slant exposed to air"], 3,
  "Kỵ khí bắt buộc **không** mọc ở bề mặt tiếp xúc không khí.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["obligate anaerobe"], pool="mock")

v("GRO-03", "obligate aerobe", "hiếu khí bắt buộc", "An organism that requires O2.", "Pseudomonas is an obligate aerobe.", ["obligate aerobes"])
v("GRO-03", "obligate anaerobe", "kỵ khí bắt buộc", "An organism that cannot use O2 and is harmed by it.", "Clostridium is an obligate anaerobe.", ["obligate anaerobes"])
v("GRO-03", "aerotolerant anaerobe", "kỵ khí chịu oxy", "Ferments, cannot use O2, but tolerates it.", "Lactobacillus is an aerotolerant anaerobe.", ["aerotolerant anaerobes"])
v("GRO-03", "microaerophile", "vi hiếu khí", "An aerobe requiring less O2 than air.", "Campylobacter is a microaerophile.", ["microaerophiles"])
v("GRO-03", "superoxide", "gốc superoxide", "The toxic radical O2•− formed during aerobic metabolism.", "Superoxide is neutralized by SOD.", ["superoxide radical", "superoxide radicals"])
v("GRO-03", "superoxide dismutase", "superoxide dismutase (SOD)", "Enzyme converting superoxide to H2O2 and O2.", "All aerobes make superoxide dismutase.", ["SOD"])
v("GRO-03", "catalase", "catalase", "Enzyme converting H2O2 to water and O2.", "Staphylococcus is catalase-positive.")
v("GRO-03", "peroxidase", "peroxidase", "Enzyme reducing H2O2 to water.", "Peroxidase removes hydrogen peroxide.")
v("GRO-03", "singlet oxygen", "oxy đơn bội (singlet oxygen)", "O2 boosted to a higher-energy, very reactive state.", "Singlet oxygen damages cells.")
v("GRO-03", "anaerobic jar", "bình kỵ khí", "A sealed container in which O2 is removed by H2 on a palladium catalyst.", "Clostridium is incubated in an anaerobic jar.")

fc("GRO-03", "fact", "Five oxygen groups and tube positions?", "Obligate aerobe: top. Facultative: throughout, densest top. Obligate anaerobe: bottom. Aerotolerant: evenly. Microaerophile: narrow band below surface.")
fc("GRO-03", "fact", "SOD and catalase reactions?", "SOD: 2 O2•− + 2H+ → H2O2 + O2. Catalase: 2 H2O2 → 2 H2O + O2.")
fc("GRO-03", "fact", "Anaerobic jar gas reaction (slide)?", "NaHCO3 + NaBH4 + H2O → H2 + CO2; H2 + O2 → H2O on palladium.")
fc("GRO-03", "trap", "TRUE/FALSE: aerotolerant anaerobes respire with O2.", "FALSE – they ferment; they only tolerate O2 (SOD).")

# ---------------------------------------------------------------- GRO-04
unit("GRO-04", "Culture media and pure cultures", "H", 2, 25, S5 + ": slides 28–41",
"""Mẫu nước giếng cần kiểm tra *E. coli* – nhưng trong đó có hàng trăm loài vi khuẩn khác. Nếu cấy lên thạch dinh dưỡng thường, bạn sẽ thấy "một rừng" khuẩn lạc. Giải pháp: dùng môi trường **chọn lọc** (ức chế loài không mong muốn) và **phân biệt** (làm *E. coli* đổi màu khác). Rồi dùng **cấy ria** để thu **khuẩn lạc thuần**.""",
("MacConkey agar contains bile salts and crystal violet (inhibit Gram-positives) and lactose with a pH indicator (lactose fermenters turn pink). This medium is:",
 ["only selective", "only differential", "both selective and differential", "chemically defined and reducing"], 2,
 "Muối mật + crystal violet **ức chế Gram dương → chọn lọc**; lactose + chỉ thị pH làm **khuẩn lạc lên men lactose màu hồng → phân biệt**."),
[
("1. Môi trường nuôi cấy – khái niệm (slide 28–29)", """
- **Culture medium**: môi trường chứa **chất dinh dưỡng** được chuẩn bị cho vi sinh vật **sinh trưởng trong phòng thí nghiệm**.
- **Tiêu chuẩn** của một môi trường:
  1. **phải chứa đúng chất dinh dưỡng** cho vi sinh vật cụ thể;
  2. **đủ ẩm**, **pH điều chỉnh phù hợp**, **mức oxy thích hợp**;
  3. **ban đầu phải vô trùng**;
  4. **ủ ở nhiệt độ thích hợp**.
- **Inoculum** (giống cấy): vi sinh vật đưa vào môi trường để bắt đầu sinh trưởng.
- **Culture** (canh trường/nuôi cấy): vi sinh vật **sinh trưởng và nhân lên** trong/trên môi trường.
- **Môi trường pha sẵn (ready-to-use)**: chỉ cần thêm nước và tiệt trùng.
"""),
("2. Agar và các dạng môi trường (slide 29)", """
- **Agar**: **polysaccharide phức tạp** chiết từ **tảo biển** (tảo đỏ *Gelidium, Gracilaria* – PRO-05); là **chất làm đông**.
  - **Nóng chảy ở ~100 °C**, nhưng **giữ trạng thái lỏng tới dưới ~40 °C** → đổ đĩa ở 45–50 °C không làm chết vi khuẩn; ủ 37 °C (thậm chí 60 °C) thạch vẫn đông.
  - Rất ít vi sinh vật phân giải được agar → không bị "ăn" mất.
- Các dạng: **deep agar** (thạch đứng trong ống), **slant** (thạch nghiêng), **agar plate** (đĩa thạch Petri), và **broth** (môi trường lỏng).
"""),
("3. Phân loại theo thành phần (slide 30–31)", """
| Loại | Định nghĩa | Ví dụ |
|---|---|---|
| **Chemically defined medium** (xác định hóa học) | **biết chính xác thành phần hóa học** | glucose + muối vô cơ (nuôi *E. coli*); môi trường nghiên cứu nhu cầu dinh dưỡng |
| **Complex medium** (phức tạp) | gồm dịch chiết **nấm men, thịt, thực vật** hoặc **protein thủy phân (peptone)**; thành phần **thay đổi nhẹ theo từng lô** | nutrient broth/agar, LB, PDA |
"""),
("4. Phân loại theo chức năng (slide 32–37)", """
| Loại | Nguyên lý | Ví dụ |
|---|---|---|
| **Reducing media** (môi trường khử) | chứa **sodium thioglycolate** kết hợp hóa học với **O₂ hòa tan** → loại O₂ | nuôi **kỵ khí**; ống thioglycolate |
| **Selective media** (chọn lọc) | **ức chế** vi khuẩn không mong muốn, **khuyến khích** vi sinh vật cần tìm | thạch muối mannitol (7,5 % NaCl – *Staphylococcus*); Sabouraud (pH thấp – nấm) |
| **Differential media** (phân biệt) | giúp **phân biệt khuẩn lạc** loài cần tìm với loài khác **trên cùng đĩa** | thạch máu (tan máu), EMB, MacConkey |
| **Enrichment media** (tăng sinh) | thường **lỏng**; tạo điều kiện cho **một loài ít ỏi** ban đầu **tăng lên mức phát hiện được**, còn loài khác thì không | canh selenite tăng sinh *Salmonella* |

- Enrichment cũng là **một dạng chọn lọc**, nhưng mục đích là **nâng số lượng rất nhỏ** lên mức phát hiện.
- Một môi trường có thể vừa **chọn lọc vừa phân biệt** (MacConkey, mannitol salt agar).
"""),
("5. Khuẩn lạc và nuôi cấy thuần (slide 38–41)", """
- **Colony** (khuẩn lạc): về lý thuyết phát sinh từ **một bào tử hoặc một tế bào sinh dưỡng**, hoặc từ **một nhóm cùng loài dính nhau** thành cụm, chuỗi → vì vậy đếm là **CFU**.
- **Pure culture** (nuôi cấy thuần): chỉ chứa **một loài**.
- **Streak plate method** (cấy ria): dùng que cấy **ria mẫu thành nhiều vùng** trên mặt thạch, mỗi vùng pha loãng dần → vùng cuối có **khuẩn lạc tách rời** → cấy chuyển một khuẩn lạc sang môi trường mới → nuôi cấy thuần.
"""),
],
[
("Kiểm nghiệm thực phẩm & nước", """
Quy trình tìm *Salmonella* trong thực phẩm (ISO 6579): **tiền tăng sinh** (canh peptone đệm) → **tăng sinh chọn lọc** (RVS, MKTTn) → **cấy phân lập** trên thạch chọn lọc–phân biệt (XLD) → **khẳng định sinh hóa** (IDT-01). Mỗi bước dùng đúng một loại môi trường trong bài.
"""),
("Lab CH3004", """
Bạn sẽ pha môi trường (cân, hòa tan, chỉnh pH, hấp 121 °C), đổ đĩa khi thạch còn ~45–50 °C, làm thạch nghiêng giữ giống và **cấy ria 4 vùng** để phân lập. Hiểu tính chất agar (đông < 40 °C) giúp bạn không đổ đĩa quá nóng (đọng hơi nước) hay quá nguội (vón cục).
"""),
],
[
("Culture medium basics", "A **culture medium** supplies nutrients for lab growth. Criteria: right **nutrients**, adequate **moisture**, adjusted **pH**, suitable **oxygen**, **initially sterile**, incubated at the proper **temperature**. **Inoculum** = microbes introduced; **culture** = microbes growing. **Agar** (from seaweed) melts at ~100 °C and stays liquid until < 40 °C.", "Agar chảy ~100 °C, đông < 40 °C."),
("Defined vs complex", "**Chemically defined**: exact chemical composition known. **Complex**: yeast, meat or plant extracts or protein digests; composition varies slightly from batch to batch.", "Xác định vs phức tạp."),
("Functional media", "**Reducing** (sodium thioglycolate removes O₂). **Selective** (suppress unwanted, encourage desired). **Differential** (distinguish colonies on one plate). **Enrichment** (usually liquid; increases very small numbers of the desired organism to detectable levels).", "Khử – chọn lọc – phân biệt – tăng sinh."),
("Pure cultures", "A **colony** arises from a single cell or spore or a clump of the same organism. The **streak plate** spreads cells so isolated colonies form → **pure culture**.", "Cấy ria → khuẩn lạc tách rời."),
],
["Complex media have exactly known composition", "Enrichment media distinguish colonies", "Agar solidifies at 100 °C", "One colony always comes from one cell"])

q("GRO-04", "recall", 1, "Agar melts at about 100 °C. At what temperature does melted agar solidify?",
  ["Just below 100 °C", "Below about 40 °C", "Below 0 °C", "At 121 °C"], 1,
  "Slide 29: agar **chảy ~100 °C**, **giữ lỏng tới < 40 °C**.",
  ["Sai.", "", "Sai.", "Sai."], ["agar"], "Agar solidifies at 100 °C", src=S5 + " slide 29")
q("GRO-04", "recall", 1, "A medium whose exact chemical composition is known is called:",
  ["complex medium", "chemically defined medium", "enrichment medium", "differential medium"], 1,
  "Slide 30: **chemically defined medium**.",
  ["Thành phần thay đổi theo lô.", "", "Chức năng tăng sinh.", "Chức năng phân biệt."], ["chemically defined medium"], src=S5 + " slide 30")
q("GRO-04", "concept", 2, "Sodium thioglycolate is added to some media in order to:",
  ["inhibit Gram-positive bacteria", "chemically combine with dissolved oxygen so anaerobes can grow", "change color with lactose fermentation", "solidify the medium"], 1,
  "Slide 32: **reducing media** – thioglycolate **kết hợp với O₂ hòa tan** → loại O₂.",
  ["Chọn lọc.", "", "Phân biệt.", "Agar."], ["reducing medium", "thioglycolate"], src=S5 + " slide 32")
q("GRO-04", "concept", 2, "What is the main difference between an enrichment medium and a differential medium?",
  ["Enrichment media increase very small numbers of a desired organism to detectable levels; differential media make colonies look different", "They are identical", "Differential media are always liquid", "Enrichment media contain no nutrients"], 0,
  "Slide 35–36: **enrichment** (thường lỏng) nâng số lượng ít ỏi lên mức phát hiện; **differential** giúp phân biệt khuẩn lạc trên cùng đĩa.",
  ["", "Khác nhau.", "Thường là đĩa thạch.", "Sai."], ["enrichment medium", "differential medium"], "Enrichment media distinguish colonies")
q("GRO-04", "concept", 2, "Why is a complex medium such as nutrient broth said to vary from batch to batch?",
  ["It contains extracts or protein digests whose exact composition is not known", "It is not sterilized", "It contains antibiotics", "It uses different agar"], 0,
  "Slide 31: dịch chiết nấm men, thịt, peptone → thành phần **thay đổi nhẹ theo lô**.",
  ["", "Sai.", "Sai.", "Sai."], ["complex medium"], "Complex media have exactly known composition")
q("GRO-04", "concept", 2, "Why is a colony counted as a colony-forming unit (CFU) rather than as one cell?",
  ["Colonies always come from exactly one cell", "A colony may arise from a single cell or from a clump or chain of cells", "Colonies contain only dead cells", "CFU is a unit of weight"], 1,
  "Slide 38: khuẩn lạc có thể từ **một tế bào/bào tử** hoặc **một cụm/chuỗi** → đơn vị là CFU.",
  ["Không luôn đúng.", "", "Sai.", "Sai."], ["colony", "CFU"], "One colony always comes from one cell")
q("GRO-04", "not", 1, "Which is NOT a criterion of a culture medium listed in the lecture?",
  ["It must contain the right nutrients", "It must initially be sterile", "It must contain an antibiotic", "It should have a properly adjusted pH"], 2,
  "Tiêu chuẩn: đúng dinh dưỡng, đủ ẩm, pH, oxy, **vô trùng ban đầu**, ủ đúng nhiệt độ. Kháng sinh **không** bắt buộc.",
  ["Có.", "Có.", "", "Có."], ["culture medium"], src=S5 + " slide 28")
q("GRO-04", "application", 2, "Mannitol salt agar contains 7.5% NaCl (only staphylococci grow) and mannitol with phenol red (S. aureus turns it yellow). It is:",
  ["selective only", "differential only", "selective and differential", "reducing"], 2,
  "NaCl 7,5 % → **chọn lọc**; mannitol + phenol red → **phân biệt**.",
  ["Thiếu phần phân biệt.", "Thiếu phần chọn lọc.", "", "Không liên quan."], ["selective medium", "differential medium"], pool="mock")
q("GRO-04", "recall", 1, "Microbes introduced into a culture medium to initiate growth are called:",
  ["a culture", "an inoculum", "a colony", "a medium"], 1,
  "Slide 29: **inoculum**; vi sinh vật mọc lên gọi là **culture**.",
  ["Culture là vi sinh vật đang mọc.", "", "Sai.", "Sai."], ["inoculum"], pool="mock")
q("GRO-04", "concept", 2, "The streak plate method is used to:",
  ["count bacteria precisely", "obtain isolated colonies and thus pure cultures", "remove oxygen", "sterilize media"], 1,
  "Slide 39–41: cấy ria tách tế bào → **khuẩn lạc tách rời** → **nuôi cấy thuần**.",
  ["Không phải phương pháp định lượng.", "", "Sai.", "Sai."], ["streak plate", "pure culture"], pool="mock")
q("GRO-04", "not", 2, "Which statement about selective media is NOT correct?",
  ["They suppress the growth of unwanted bacteria", "They encourage growth of the desired microbes", "They always make colonies different colors", "They may be combined with differential features"], 2,
  "Tạo **màu khác nhau** là đặc điểm của môi trường **phân biệt**, không bắt buộc ở môi trường chọn lọc.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["selective medium"], pool="mock")

v("GRO-04", "culture medium", "môi trường nuôi cấy", "Nutrient material prepared for growing microbes in the lab.", "Nutrient agar is a culture medium.", ["culture media", "media", "medium"])
v("GRO-04", "inoculum", "giống cấy", "Microbes introduced into a medium to start growth.", "Add 1 mL of inoculum to the flask.")
v("GRO-04", "culture", "canh trường (nuôi cấy)", "Microbes growing and multiplying in or on a medium.", "A pure culture contains one species.", ["cultures"])
v("GRO-04", "agar", "thạch (agar)", "A seaweed polysaccharide used to solidify media.", "Agar melts at about 100 °C.", ["agar plate", "slant", "deep agar"])
v("GRO-04", "chemically defined medium", "môi trường xác định hóa học", "A medium whose exact chemical composition is known.", "Glucose–salts medium is chemically defined.")
v("GRO-04", "complex medium", "môi trường phức tạp", "A medium with extracts or digests of unknown exact composition.", "Nutrient broth is a complex medium.", ["complex media", "peptone", "yeast extract"])
v("GRO-04", "reducing medium", "môi trường khử", "A medium with sodium thioglycolate that removes dissolved O2.", "Anaerobes grow in reducing medium.", ["reducing media", "thioglycolate"])
v("GRO-04", "selective medium", "môi trường chọn lọc", "A medium that suppresses unwanted microbes and favors desired ones.", "MacConkey is a selective medium.", ["selective media"])
v("GRO-04", "differential medium", "môi trường phân biệt", "A medium that makes colonies of different microbes look different.", "Blood agar is a differential medium.", ["differential media"])
v("GRO-04", "enrichment medium", "môi trường tăng sinh", "Usually liquid medium that increases small numbers of a desired microbe.", "Selenite broth is an enrichment medium.", ["enrichment media", "enrichment culture"])
v("GRO-04", "colony", "khuẩn lạc", "A visible mass of cells arising from one cell, spore or clump.", "Pick one colony to start a pure culture.", ["colonies"])
v("GRO-04", "streak plate", "cấy ria (phương pháp)", "Spreading an inoculum over agar in zones to obtain isolated colonies.", "The streak plate gives isolated colonies.", ["streak plate method"])

fc("GRO-04", "fact", "Four criteria of a culture medium?", "Right nutrients; moisture, pH, oxygen; initially sterile; proper incubation temperature.")
fc("GRO-04", "number", "Agar melting and solidifying temperatures?", "Melts ~100 °C; stays liquid until below ~40 °C.")
fc("GRO-04", "fact", "Reducing, selective, differential, enrichment media?", "Reducing: thioglycolate removes O2. Selective: suppress unwanted. Differential: colonies look different. Enrichment: raise small numbers to detectable levels (usually liquid).")
fc("GRO-04", "trap", "TRUE/FALSE: enrichment medium and differential medium mean the same.", "FALSE.")

# ---------------------------------------------------------------- GRO-05
unit("GRO-05", "Binary fission, generation time and the growth curve", "H", 3, 30, S6 + ": slides 1–12",
"""Một tế bào *E. coli* chia đôi mỗi 20 phút. Nếu điều kiện lý tưởng kéo dài, sau **48 giờ** khối lượng vi khuẩn sẽ vượt **khối lượng Trái Đất**! Điều đó không xảy ra vì dinh dưỡng cạn và chất thải tích tụ – quần thể đi qua **4 pha**: tiềm phát, lũy thừa, cân bằng, suy vong. Biết **thời gian thế hệ** giúp dự đoán khi nào sữa để ngoài bị hỏng.""",
("A culture has 10^4 cells/mL at 6 h and 10^8 cells/mL at 10 h during exponential growth. What is the generation time?",
 ["1 h", "about 0.3 h (18 min)", "4 h", "0.1 h"], 1,
 "Slide 9: g = log2 × (t − t₀)/(log Nt − log N₀) = 0,301 × 4/4 = **0,301 h ≈ 18 phút**."),
[
("1. Phân đôi (slide 3–5)", """
- Vi khuẩn sinh sản chủ yếu bằng **phân đôi (binary fission)** [fig]: tế bào dài ra → **DNA nhân đôi** → màng và thành **lõm vào** → **vách ngăn** → hai tế bào con.
- Mỗi lần phân chia số tế bào **nhân đôi**: 1 → 2 → 4 → 8 → … = **2ⁿ** sau n thế hệ. Tăng trưởng **lũy thừa** → vẽ **log số tế bào** theo thời gian được đường thẳng.
"""),
("2. Thời gian thế hệ (slide 6–7)", """
- **Generation time (g)**: thời gian để **một tế bào phân chia** (và **quần thể tăng gấp đôi**).
- Thay đổi nhiều **giữa các loài** và theo **điều kiện môi trường** (nhiệt độ, dinh dưỡng…).
- **Phần lớn vi khuẩn: 1–3 giờ**; một số cần **> 24 giờ** mỗi thế hệ (vd *Mycobacterium tuberculosis* ~18–24 h). *E. coli* trong điều kiện tối ưu ~20 phút. [mở rộng]
"""),
("3. Công thức tính (slide 8–9)", """
| Công thức | Ý nghĩa |
|---|---|
| **Nt = N₀ × 2ⁿ** | số tế bào sau n thế hệ |
| **log Nt = log N₀ + n × log 2** | lấy log hai vế |
| **n = (log Nt − log N₀) / log 2** | số thế hệ trong khoảng (t − t₀) |
| **g = (t − t₀) / n** | thời gian thế hệ |
| **g = log 2 × (t − t₀) / (log Nt − log N₀)** | công thức gộp |

Ký hiệu: **t₀** – thời điểm có N₀ tế bào; **t** – thời điểm có Nt tế bào; **n** – số thế hệ trong khoảng (t − t₀). **log 2 = 0,301**.

**Ví dụ slide 9**: nồi lên men có vi khuẩn ở pha sinh trưởng: **10⁴ tế bào/mL lúc 6 h**, **10⁸ tế bào/mL lúc 10 h**.
g = 0,301 × (10 − 6)/(8 − 4) = 0,301 × 4/4 = **0,301 h** (≈ 18 phút). Số thế hệ n = 4/0,301 ≈ **13,3**.

⚠ Chỉ áp dụng trong **pha lũy thừa**. Dùng **log₁₀** nhất quán; nhớ chia cho **log 2** chứ không phải nhân.
"""),
("4. Đường cong sinh trưởng và 4 pha (slide 10–12)", """
Trong **nuôi cấy mẻ (batch culture)** – môi trường không bổ sung, không lấy ra [fig]:
| Pha | Đặc điểm | Vì sao |
|---|---|---|
| **Lag phase** (tiềm phát) | **số tế bào gần như không đổi**; tế bào hoạt động trao đổi chất mạnh, tổng hợp enzyme, **thích nghi** | làm quen môi trường mới |
| **Log (exponential) phase** (lũy thừa) | số tế bào **tăng theo cấp số nhân**, g ngắn nhất và ổn định; tế bào **nhạy nhất** với kháng sinh, bức xạ | dinh dưỡng dồi dào |
| **Stationary phase** (cân bằng) | số tế bào **mới sinh = số chết** → tổng không đổi | **cạn dinh dưỡng**, **tích tụ chất thải**, pH thay đổi; bắt đầu tạo nội bào tử, chất chuyển hóa bậc 2 (kháng sinh) |
| **Death (decline) phase** (suy vong) | số chết **> số sinh** → giảm (cũng theo log) | môi trường cạn kiệt |

- Pha lag dài hơn nếu giống cấy già, hoặc chuyển sang môi trường khác hẳn. [mở rộng]
- Nuôi cấy **liên tục (chemostat)** giữ tế bào ở pha log bằng cách bổ sung môi trường mới và lấy dịch ra liên tục. [mở rộng]
"""),
],
[
("An toàn thực phẩm: vì sao đồ ăn để ngoài 4 giờ nguy hiểm", """
Giả sử thức ăn nhiễm 100 tế bào *S. aureus* (g ≈ 30 phút ở 30 °C). Sau 4 giờ = **8 thế hệ**: 100 × 2⁸ = **25.600 tế bào**; sau 8 giờ (16 thế hệ) ≈ **6,5 triệu** – đủ tạo độc tố ruột gây ngộ độc. Đây là lý do "không để quá 2 giờ ở nhiệt độ phòng".
"""),
("Công nghiệp: thu sản phẩm đúng pha", """
- **Sinh khối, chất chuyển hóa bậc 1** (ethanol, acid amin, enzyme): thu ở **cuối pha log** (APP-01).
- **Chất chuyển hóa bậc 2** (penicillin): hình thành chủ yếu ở **pha cân bằng (idiophase)** (APP-04).
- Giống cấy nên lấy ở **pha log** để rút ngắn pha lag trong nồi lên men lớn.
"""),
],
[
("Generation time", "**Generation time** = time for a cell to divide and the population to **double**. It varies with the organism and conditions; most bacteria **1–3 h**, some **> 24 h**.", "Phần lớn vi khuẩn 1–3 h."),
("Formulas", "Nt = N₀·2ⁿ; log Nt = log N₀ + n·log 2; **n = (log Nt − log N₀)/log 2**; **g = (t − t₀)/n = log 2·(t − t₀)/(log Nt − log N₀)**. Example: 10⁴ at 6 h, 10⁸ at 10 h → g = 0.301·4/4 = **0.301 h**.", "g = 0,301 × Δt / Δlog N."),
("Growth curve", "Batch culture phases: **lag** (no increase; adapting, synthesizing enzymes), **log/exponential** (constant doubling; most sensitive to drugs), **stationary** (births = deaths; nutrients exhausted, wastes accumulate), **death/decline** (deaths exceed births).", "Tiềm phát → lũy thừa → cân bằng → suy vong."),
],
["No metabolic activity in lag phase", "Stationary phase means all cells are dead", "Multiply by log 2 instead of dividing to get n", "Generation time is the same for all bacteria"])

q("GRO-05", "calc", 3, "A culture grows from 2 × 10³ cells/mL to 6.4 × 10⁴ cells/mL in 2.5 hours of exponential growth. What is the generation time?",
  ["20 min", "30 min", "50 min", "25 min"], 1,
  "Nt/N₀ = 6,4 × 10⁴ / 2 × 10³ = 32 = 2⁵ → **n = 5**. g = 150 phút / 5 = **30 phút**.",
  ["Tính 7,5 thế hệ.", "", "Tính 3 thế hệ.", "Tính 6 thế hệ."], ["generation time"],
  steps=["Nt/N₀ = 64000/2000 = 32", "n = log 32 / log 2 = 5", "g = 150 phút / 5 = 30 phút"])
q("GRO-05", "calc", 2, "Starting with 100 cells, how many cells are present after 6 generations of exponential growth?",
  ["600", "6,400", "3,200", "12,800"], 1,
  "Nt = 100 × 2⁶ = 100 × 64 = **6.400**.",
  ["Nhân n thay vì 2ⁿ.", "", "Chỉ 5 thế hệ.", "7 thế hệ."], ["binary fission"],
  steps=["Nt = N₀ × 2ⁿ", "2⁶ = 64", "100 × 64 = 6400"])
q("GRO-05", "concept", 2, "During which phase of a batch growth curve are cells most sensitive to antibiotics and radiation?",
  ["Lag phase", "Log (exponential) phase", "Stationary phase", "Death phase"], 1,
  "Pha **log**: tế bào phân chia mạnh, tổng hợp thành, DNA liên tục → **nhạy nhất**.",
  ["Chưa phân chia mạnh.", "", "Ít phân chia.", "Tế bào đang chết."], ["log phase"])
q("GRO-05", "concept", 2, "In the stationary phase, the number of viable cells remains constant because:",
  ["cells stop metabolism completely", "the number of new cells equals the number of dying cells", "all cells form spores", "the medium is replaced continuously"], 1,
  "Pha cân bằng: **số sinh ra = số chết** do cạn dinh dưỡng, tích tụ chất thải.",
  ["Vẫn có hoạt động.", "", "Chỉ một số loài tạo bào tử.", "Đó là nuôi liên tục."], ["stationary phase"], "Stationary phase means all cells are dead")
q("GRO-05", "concept", 2, "What happens during the lag phase?",
  ["Cells divide at maximum rate", "There is little or no increase in cell number, but cells are metabolically active and adapting", "Cells die faster than they divide", "Toxic wastes accumulate and growth stops"], 1,
  "Pha **lag**: số tế bào gần như không tăng nhưng tế bào **tích cực tổng hợp enzyme, thích nghi**.",
  ["Pha log.", "", "Pha suy vong.", "Pha cân bằng."], ["lag phase"], "No metabolic activity in lag phase")
q("GRO-05", "recall", 1, "According to the lecture, the generation time of most bacteria is:",
  ["1–3 minutes", "1–3 hours", "1–3 days", "exactly 20 minutes"], 1,
  "Slide 7: **phần lớn 1–3 giờ**; một số > 24 giờ.",
  ["Quá ngắn.", "", "Quá dài với đa số.", "Chỉ E. coli trong điều kiện tối ưu."], ["generation time"], "Generation time is the same for all bacteria", src=S6 + " slide 7")
q("GRO-05", "calc", 3, "Exponential growth: N0 = 10⁵ cells/mL at t0 = 0; Nt = 10⁷ cells/mL at t = 2 h. Calculate the generation time (log 2 = 0.301).",
  ["0.301 h", "0.602 h", "1.0 h", "0.15 h"], 0,
  "g = 0,301 × 2/(7 − 5) = 0,301 × 2/2 = **0,301 h** (≈ 18 phút).",
  ["", "Quên chia cho Δlog = 2.", "Sai.", "Chia đôi thừa."], ["generation time"],
  steps=["g = log 2 × (t − t₀)/(log Nt − log N₀)", "= 0,301 × 2/(7 − 5)", "= 0,301 h"])
q("GRO-05", "calc", 3, "How many generations occur when a population increases from 10⁴ to 10⁸ cells? (log 2 = 0.301)",
  ["4", "about 13.3", "about 1.2", "40"], 1,
  "n = (8 − 4)/0,301 = 4/0,301 ≈ **13,3** thế hệ.",
  ["Quên chia log 2.", "", "Nhân thay vì chia.", "Sai."], ["generation time"], "Multiply by log 2 instead of dividing to get n", pool="mock",
  steps=["n = (log Nt − log N₀)/log 2", "= (8 − 4)/0,301", "≈ 13,3"])
q("GRO-05", "not", 2, "Which statement about the phases of bacterial growth is NOT correct?",
  ["In the lag phase there is little cell division", "In the log phase cells divide at a constant rate", "In the stationary phase nutrients are plentiful and growth is fastest", "In the death phase deaths exceed new cells"], 2,
  "Pha cân bằng: **dinh dưỡng cạn**, chất thải tích tụ; tăng trưởng nhanh nhất là pha log.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["stationary phase"], pool="mock")
q("GRO-05", "calc", 3, "A bacterium with a generation time of 20 min starts at 50 cells. How many cells are there after 2 hours of exponential growth?",
  ["300", "3,200", "6,400", "1,600"], 1,
  "2 h = 120 phút → n = 120/20 = **6** → 50 × 2⁶ = **3.200**.",
  ["Nhân 50 × 6.", "", "Tính 7 thế hệ.", "Tính 5 thế hệ."], ["generation time"], pool="mock",
  steps=["n = 120/20 = 6", "2⁶ = 64", "50 × 64 = 3200"])
q("GRO-05", "data", 2, "A growth curve shows: 0–2 h: 10⁶ cells/mL (constant); 2–6 h: rises to 10⁹; 6–10 h: stays at 10⁹; after 10 h: falls. Which interval is the log phase?",
  ["0–2 h", "2–6 h", "6–10 h", "after 10 h"], 1,
  "Tăng từ 10⁶ lên 10⁹ = **pha log (2–6 h)**. 0–2 h lag; 6–10 h stationary; sau 10 h death.",
  ["Lag.", "", "Stationary.", "Death."], ["log phase"], pool="mock")

we("WE-03", "GRO-05", "Generation time from the lecture example",
"""A fermenter contains bacteria in the growth phase: 10⁴ cells/mL at 6 h and 10⁸ cells/mL at 10 h.
Calculate (a) the number of generations and (b) the generation time. Use log 2 = 0.301.""",
[S("t − t₀ = ? h", 4),
 S("log Nt − log N₀ = ?", 4),
 S("n = (log Nt − log N₀)/log 2 = ? (1 decimal)", 13.3, hint="4 / 0,301"),
 S("g = (t − t₀)/n = ? h (3 decimals)", 0.301),
 S("Convert g to minutes = ? min", 18.06, hint="0,301 × 60")],
"n ≈ 13.3 generations; g = 0.301 h ≈ 18 min.",
"Công thức gộp: g = log 2 × Δt / Δlog N = 0,301 × 4/4 = 0,301 h. Đây đúng là ví dụ slide 9.")

we("WE-04", "GRO-05", "Generation time from counts that are not powers of ten",
"""During exponential growth a culture has 3.0 × 10⁵ cells/mL at 1.0 h and 2.4 × 10⁷ cells/mL at 4.0 h.
Find the number of generations and the generation time (minutes). log 2 = 0.301.""",
[S("log N₀ = log(3.0 × 10⁵) = ? (2 decimals)", 5.48, hint="log 3 = 0,477"),
 S("log Nt = log(2.4 × 10⁷) = ? (2 decimals)", 7.38, hint="log 2,4 = 0,380"),
 S("Δlog N = ? (2 decimals)", 1.90),
 S("n = Δlog N / 0.301 = ? (1 decimal)", 6.3),
 S("g = 180 min / n = ? min", 28.5, hint="180 / 6,32")],
"n ≈ 6.3 generations; g ≈ 28.5 min.",
"Kiểm tra nhanh: Nt/N₀ = 80 ≈ 2^6,32 → hợp lý. Sai lầm thường gặp: quên đổi 3 h sang 180 phút, hoặc lấy log sai phần định trị.")

we("WE-05", "GRO-05", "Predicting cell numbers in food left at room temperature",
"""Cooked rice contains 200 cells/g of Bacillus cereus. At 30 °C its generation time is 30 min and the lag phase lasts 1 h.
Estimate the number of cells after 5 h at 30 °C, assuming exponential growth after the lag.""",
[S("Time in exponential phase = 5 − 1 = ? h", 4),
 S("Number of generations n = 4 h / 0.5 h = ?", 8),
 S("2ⁿ = ?", 256),
 S("Nt = 200 × 256 = ? cells/g", 51200)],
"About 5.1 × 10⁴ cells/g after 5 h.",
"Trừ pha lag trước khi tính số thế hệ. Nếu không có pha lag, kết quả sẽ là 200 × 2¹⁰ = 204.800 – gấp 4 lần.")

v("GRO-05", "generation time", "thời gian thế hệ", "Time required for a cell to divide and the population to double.", "The generation time of E. coli can be 20 min.", ["doubling time"])
v("GRO-05", "growth curve", "đường cong sinh trưởng", "A plot of log cell number versus time in a batch culture.", "The growth curve has four phases.")
v("GRO-05", "batch culture", "nuôi cấy mẻ (theo chu kỳ)", "Culture in a closed vessel without adding medium or removing products.", "A batch culture passes through lag, log, stationary and death phases.")
v("GRO-05", "lag phase", "pha tiềm phát", "Phase with little cell division while cells adapt and make enzymes.", "The lag phase is short if the inoculum is young.")
v("GRO-05", "log phase", "pha lũy thừa (log)", "Phase of constant exponential division.", "Cells in log phase are most sensitive to antibiotics.", ["exponential phase", "logarithmic phase"])
v("GRO-05", "stationary phase", "pha cân bằng (ổn định)", "Phase in which new cells balance dying cells.", "Antibiotics are made in the stationary phase.")
v("GRO-05", "death phase", "pha suy vong (chết)", "Phase in which deaths exceed new cells.", "Numbers fall logarithmically in the death phase.", ["decline phase"])
v("GRO-05", "exponential growth", "tăng trưởng lũy thừa", "Growth in which the population doubles every generation.", "Exponential growth gives a straight line on a log plot.")

fc("GRO-05", "fact", "Formula for generation time?", "g = log 2 × (t − t₀) / (log Nt − log N₀); n = (log Nt − log N₀)/log 2.")
fc("GRO-05", "number", "Lecture example result?", "10⁴ at 6 h → 10⁸ at 10 h: g = 0.301 h (~18 min).")
fc("GRO-05", "number", "Typical generation time of most bacteria?", "1–3 h; some > 24 h.")
fc("GRO-05", "fact", "Four phases of a batch growth curve?", "Lag, log (exponential), stationary, death (decline).")
fc("GRO-05", "trap", "TRUE/FALSE: cells are inactive in the lag phase.", "FALSE – they are metabolically active, making enzymes; they just don't divide much.")

# ---------------------------------------------------------------- GRO-06
unit("GRO-06", "Direct counts: counting chambers, plate count, serial dilution, filtration and MPN", "H", 3, 30, S6 + ": slides 13–27",
"""Tiêu chuẩn nước uống: **0 CFU *E. coli* / 100 mL**. Làm sao phát hiện được vài con vi khuẩn trong 100 mL nước? Không thể nhìn dưới kính – phải **lọc** cả 100 mL qua màng rồi đặt màng lên thạch. Còn với sữa chứa hàng triệu vi khuẩn/mL, ta **pha loãng** nhiều lần mới đếm được. Mỗi mật độ cần một phương pháp khác nhau.""",
("To count coliform bacteria in drinking water with very few bacteria, the best direct method is:",
 ["direct microscopic count", "membrane filtration of a large volume followed by incubation of the filter on agar", "turbidity", "dry weight"], 1,
 "Slide 21–22: **lọc** một thể tích lớn qua màng giữ vi khuẩn → đặt màng lên thạch → đếm khuẩn lạc. Phù hợp mẫu **rất ít vi khuẩn**."),
[
("1. Đếm trực tiếp dưới kính hiển vi (slide 13–17)", """
- Tính dựa trên **số tế bào đếm được trong một thể tích xác định** của dịch chứa tế bào; dịch phải được **pha loãng** tới mật độ đếm được.
- **Buồng đếm Petroff-Hausser** (cho vi khuẩn) [fig]:
  - **25 ô lớn × 16 ô nhỏ = 400 ô nhỏ**; tổng diện tích **1 mm²**; chiều sâu **0,02 mm**.
  - Thể tích toàn lưới: 1 mm² × 0,02 mm = 0,02 mm³ = **2 × 10⁻⁵ mL** (1 mL = 1000 mm³).
- **Buồng đếm hồng cầu (hemocytometer)** (cho nấm men, tế bào lớn): sâu **0,1 mm** → thể tích 1 mm² là **10⁻⁴ mL**.
| Buồng | h_c | V_c (1 mm²) |
|---|---|---|
| Hemocytometer | 0,1 mm | **10⁻⁴ mL** |
| Petroff-Hausser | 0,02 mm | **2 × 10⁻⁵ mL** |
- **Mật độ = (số tế bào đếm / thể tích đếm) × hệ số pha loãng**.
- Ưu: nhanh, không cần ủ. Nhược: **đếm cả tế bào chết**, khó đếm vi khuẩn di động, cần mật độ cao (~10⁷/mL). [mở rộng]
"""),
("2. Đếm khuẩn lạc – plate count (slide 18–20)", """
- Dùng được cho **cả vi khuẩn và nấm men**.
- **Nguyên lý**: một tế bào sống sẽ sinh trưởng, phân chia qua nhiều thế hệ tạo **một khuẩn lạc – CFU (colony forming unit)**. Đếm khuẩn lạc → số tế bào sống trong một thể tích dịch.
- Phải **pha loãng** dịch tế bào tới mức thích hợp để đếm được (thường **30–300 khuẩn lạc/đĩa**).
- **Pha loãng liên tiếp (serial dilution)**: 1 mL mẫu + 9 mL nước muối sinh lý = 10⁻¹; tiếp tục → 10⁻², 10⁻³… [fig]
- Cấy: **đổ đĩa (pour plate)** – 1 mL mẫu trộn với thạch nóng chảy ~45 °C; **trải đĩa (spread plate)** – 0,1 mL trải trên mặt thạch.
- **CFU/mL = số khuẩn lạc / (thể tích cấy (mL) × độ pha loãng)** = số khuẩn lạc × hệ số pha loãng / thể tích cấy.
- Ví dụ: 0,1 mL từ ống 10⁻⁵ cho 150 khuẩn lạc → 150/(0,1 × 10⁻⁵) = **1,5 × 10⁸ CFU/mL**.
- Ưu: chỉ đếm **tế bào sống**, độ nhạy cao. Nhược: cần **24–48 h**, cụm tế bào = 1 CFU.
"""),
("3. Lọc màng – filtration (slide 21–22)", """
- Cho **thể tích lớn** mẫu (100 mL nước, đồ uống) qua **màng lọc** có lỗ nhỏ giữ vi khuẩn (~0,45 μm).
- Đặt màng lên **đĩa thạch** (hoặc đệm thấm môi trường) → ủ → khuẩn lạc mọc trên màng → đếm.
- Dùng khi **số lượng vi khuẩn rất ít** (kiểm tra coliform trong nước uống).
"""),
("4. Phương pháp MPN – Most Probable Number (slide 23–27)", """
- **Nguyên lý**: **càng nhiều** vi khuẩn trong mẫu, **càng cần pha loãng nhiều** mới đến mức **không còn vi khuẩn** nào mọc trong các ống của dãy pha loãng.
- Thực hiện: cấy **nhiều ống lặp** (thường **3 hoặc 5 ống**) ở mỗi mức pha loãng (vd 10 mL, 1 mL, 0,1 mL mẫu) vào môi trường lỏng → ủ → **ghi dấu hiệu sinh trưởng** (đục, sinh khí trong ống Durham, đổi màu) = ống dương tính.
- Tổ hợp số ống dương tính (vd **5-3-1**) → tra **bảng MPN** → số vi khuẩn **có khả năng nhất** trong 100 mL (kèm khoảng tin cậy 95 %). [fig]
- Là **ước lượng thống kê**; dùng khi vi khuẩn **không mọc trên thạch** hoặc cần phát hiện bằng đặc tính trong môi trường lỏng (coliform: lên men lactose sinh khí).
"""),
("5. So sánh các phương pháp trực tiếp", """
| Phương pháp | Đếm gì | Ưu | Nhược |
|---|---|---|---|
| Buồng đếm | mọi tế bào (sống + chết) | nhanh | cần mật độ cao; không phân biệt sống/chết |
| Plate count | tế bào sống (CFU) | nhạy, chỉ sống | 24–48 h; cụm = 1 CFU |
| Lọc màng | tế bào sống trong thể tích lớn | phát hiện mật độ rất thấp | mẫu đục làm tắc màng |
| MPN | ước lượng thống kê tế bào sống | dùng môi trường lỏng, đặc tính sinh hóa | kém chính xác, cần bảng tra |
"""),
],
[
("Tiêu chuẩn vi sinh Việt Nam (tham khảo)", """
- **QCVN 01-1:2018/BYT** (nước sạch sinh hoạt): *E. coli* và coliform chịu nhiệt **< 1 CFU/100 mL** – kiểm bằng **lọc màng** hoặc **MPN**.
- Sữa tươi nguyên liệu, thực phẩm: chỉ tiêu **tổng vi sinh vật hiếu khí** (TPC) bằng **đổ đĩa**, tính CFU/g hoặc CFU/mL.
Đây chính là các kỹ thuật bạn thực hành ở lab CH3004.
"""),
],
[
("Direct microscopic count", "Count cells in a known volume of a diluted suspension. **Petroff-Hausser**: 25 × 16 = **400 small squares**, area **1 mm²**, depth **0.02 mm** → **2 × 10⁻⁵ mL**. Hemocytometer: depth **0.1 mm** → **10⁻⁴ mL**. Cells/mL = count ÷ volume × dilution factor.", "Petroff-Hausser: 2×10⁻⁵ mL; hồng cầu: 10⁻⁴ mL."),
("Plate count", "A living cell grows into a **colony (CFU)**; works for bacteria and yeast. **Serial dilution** then pour or spread plate; count plates with **30–300** colonies. **CFU/mL = colonies ÷ (volume plated × dilution)**.", "CFU/mL = số KL / (V × độ pha loãng)."),
("Filtration and MPN", "**Filtration**: large volumes through a membrane that retains bacteria; filter placed on agar (few bacteria, e.g., water). **MPN**: replicate tubes in a dilution series; the more bacteria, the more dilution is needed before no tubes grow; positive-tube pattern → **MPN table** (statistical estimate).", "Lọc màng cho mẫu loãng; MPN = ước lượng thống kê."),
],
["Direct counts distinguish live and dead cells", "CFU always equals number of cells", "Multiply colonies by volume plated", "MPN is an exact count"])

q("GRO-06", "calc", 2, "0.1 mL of a 10⁻⁴ dilution is spread on a plate and 85 colonies develop. What is the concentration in the original sample?",
  ["8.5 × 10⁵ CFU/mL", "8.5 × 10⁶ CFU/mL", "8.5 × 10⁴ CFU/mL", "8.5 × 10⁷ CFU/mL"], 1,
  "CFU/mL = 85 / (0,1 × 10⁻⁴) = 85 × 10⁵ = **8,5 × 10⁶ CFU/mL**.",
  ["Quên chia cho 0,1 mL.", "", "Sai hai bậc.", "Thừa một bậc."], ["CFU", "serial dilution"], "Multiply colonies by volume plated",
  steps=["V × d = 0,1 × 10⁻⁴ = 10⁻⁵", "85 / 10⁻⁵ = 8,5 × 10⁶ CFU/mL"])
q("GRO-06", "recall", 1, "The Petroff-Hausser counting chamber described in the lecture has a total area of 1 mm² and a depth of 0.02 mm. What is the volume over the whole grid?",
  ["10⁻⁴ mL", "2 × 10⁻⁵ mL", "2 × 10⁻² mL", "10⁻³ mL"], 1,
  "V = 1 mm² × 0,02 mm = 0,02 mm³ = 0,02 × 10⁻³ mL = **2 × 10⁻⁵ mL**.",
  ["Đó là buồng sâu 0,1 mm.", "", "Chưa đổi mm³ sang mL.", "Sai."], ["Petroff-Hausser chamber"], src=S6 + " slide 16",
  steps=["V = 1 × 0,02 = 0,02 mm³", "1 mL = 1000 mm³", "0,02 mm³ = 2 × 10⁻⁵ mL"])
q("GRO-06", "calc", 3, "In a Petroff-Hausser chamber (whole grid = 2 × 10⁻⁵ mL), 60 bacteria are counted over the entire grid of an undiluted sample. What is the concentration?",
  ["1.2 × 10⁶ cells/mL", "3.0 × 10⁶ cells/mL", "6.0 × 10⁵ cells/mL", "1.2 × 10⁻³ cells/mL"], 1,
  "C = 60 / (2 × 10⁻⁵) = **3,0 × 10⁶ tế bào/mL**.",
  ["Nhân thay vì chia.", "", "Dùng thể tích 10⁻⁴ mL.", "Nhân với thể tích."], ["Petroff-Hausser chamber"],
  steps=["C = N / V", "60 / (2 × 10⁻⁵) = 3 × 10⁶"])
q("GRO-06", "concept", 2, "What is the principle of the MPN method?",
  ["Counting colonies on a membrane", "The more bacteria in a sample, the more dilution is needed before no bacteria remain to grow in the tubes", "Measuring light absorbance", "Weighing dried cells"], 1,
  "Slide 23: **càng nhiều vi khuẩn, càng phải pha loãng nhiều** mới hết vi khuẩn trong ống → ước lượng thống kê bằng bảng MPN.",
  ["Lọc màng.", "", "Độ đục.", "Khối lượng khô."], ["MPN"], "MPN is an exact count", src=S6 + " slide 23")
q("GRO-06", "concept", 2, "Why is the plate count reported as colony-forming units rather than cells?",
  ["Because dead cells also form colonies", "Because a colony may arise from a clump or chain of cells, not necessarily from one cell", "Because colonies are counted under a microscope", "Because CFU measures dry weight"], 1,
  "Một khuẩn lạc có thể từ **một cụm/chuỗi** tế bào → đơn vị là **CFU**.",
  ["Tế bào chết không tạo khuẩn lạc.", "", "Sai.", "Sai."], ["CFU"], "CFU always equals number of cells")
q("GRO-06", "not", 2, "Which is NOT a characteristic of the direct microscopic count?",
  ["It is fast", "It requires no incubation", "It counts only living cells", "It needs a known chamber volume"], 2,
  "Đếm trực tiếp **đếm cả tế bào chết**; plate count mới chỉ đếm tế bào sống.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["direct microscopic count"], "Direct counts distinguish live and dead cells")
q("GRO-06", "calc", 3, "A 1-mL sample is diluted: 1 mL into 99 mL (tube A), then 1 mL of A into 9 mL (tube B). 1 mL of B is pour-plated and gives 142 colonies. What is the original concentration?",
  ["1.42 × 10³ CFU/mL", "1.42 × 10⁵ CFU/mL", "1.42 × 10⁴ CFU/mL", "1.42 × 10⁶ CFU/mL"], 1,
  "Pha loãng: 1/100 × 1/10 = **10⁻³**. CFU/mL = 142/(1 × 10⁻³) = **1,42 × 10⁵**.",
  ["Chỉ tính 10⁻¹.", "", "Chỉ tính 10⁻².", "Tính 10⁻⁴."], ["serial dilution"],
  steps=["Ống A: 1/100 = 10⁻²", "Ống B: 10⁻² × 1/10 = 10⁻³", "142 / (1 × 10⁻³) = 1,42 × 10⁵ CFU/mL"])
q("GRO-06", "application", 2, "Which plate should be used for counting? Dilutions 10⁻⁴, 10⁻⁵, 10⁻⁶ (1 mL plated) gave: too many to count, 215 colonies, 19 colonies.",
  ["10⁻⁴ plate", "10⁻⁵ plate (215 colonies)", "10⁻⁶ plate (19 colonies)", "Average all three"], 1,
  "Chọn đĩa có **30–300** khuẩn lạc → đĩa 10⁻⁵ (215). CFU/mL = 215/10⁻⁵ = 2,15 × 10⁷.",
  ["Không đếm được.", "", "Dưới 30, sai số thống kê lớn.", "Không trộn đĩa ngoài khoảng."], ["plate count"], pool="mock")
q("GRO-06", "recall", 1, "The membrane filtration method is most useful when:",
  ["the sample contains very few bacteria in a large volume", "the sample is very dense", "bacteria are dead", "measuring dry weight"], 0,
  "Slide 21–22: lọc thể tích lớn → phù hợp mẫu **rất ít vi khuẩn** (nước uống).",
  ["", "Mẫu đặc nên pha loãng và đổ đĩa.", "Không phát hiện tế bào chết.", "Sai."], ["membrane filtration"], pool="mock")
q("GRO-06", "calc", 2, "A yeast suspension is counted in a hemocytometer (depth 0.1 mm). 250 cells are found in 1 mm² of an undiluted sample. What is the concentration?",
  ["2.5 × 10⁵ cells/mL", "2.5 × 10⁶ cells/mL", "2.5 × 10⁷ cells/mL", "1.25 × 10⁷ cells/mL"], 1,
  "V = 1 mm² × 0,1 mm = 10⁻⁴ mL → 250/10⁻⁴ = **2,5 × 10⁶ tế bào/mL**.",
  ["Sai một bậc.", "", "Dùng thể tích Petroff-Hausser sai.", "Dùng 2 × 10⁻⁵ mL."], ["counting chamber"], pool="mock",
  steps=["V = 10⁻⁴ mL", "250 / 10⁻⁴ = 2,5 × 10⁶"])
q("GRO-06", "not", 2, "Which statement about the MPN method is NOT correct?",
  ["It uses replicate tubes at several dilutions", "Signs of growth (turbidity, gas) mark positive tubes", "It gives an exact count of cells", "The result is read from a statistical table"], 2,
  "MPN là **ước lượng thống kê** (số có khả năng nhất), không phải đếm chính xác.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["MPN"], pool="mock")

we("WE-06", "GRO-06", "Serial dilution and plate count",
"""A milk sample is diluted by transferring 1 mL into 9 mL of saline six times in series (10⁻¹ to 10⁻⁶). 0.1 mL of each of the 10⁻⁴, 10⁻⁵ and 10⁻⁶ dilutions is spread on plates, giving 1,850, 176 and 21 colonies.
(a) Which plate is countable? (b) Calculate CFU/mL of the milk.""",
[S("Countable range is 30–300. Which dilution? (answer as the exponent, e.g., −5)", -5),
 S("Volume plated × dilution = 0.1 × 10⁻⁵ = 10^? ", -6),
 S("CFU/mL = 176 / 10⁻⁶ = ? × 10⁸ (2 decimals)", 1.76)],
"The 10⁻⁵ plate (176 colonies) → 1.76 × 10⁸ CFU/mL.",
"Nhớ nhân thêm hệ số của thể tích cấy 0,1 mL (×10). Đĩa 21 khuẩn lạc < 30 nên không dùng.")

we("WE-07", "GRO-06", "Petroff-Hausser count with dilution",
"""A bacterial culture is diluted 1:10. In a Petroff-Hausser chamber (400 small squares over 1 mm², depth 0.02 mm), 5 randomly chosen large squares (each = 16 small squares) contain a total of 48 cells.
Find the concentration in the original culture.""",
[S("Area counted = 5 large squares × (1/25 mm²) = ? mm²", 0.2),
 S("Volume counted = 0.2 mm² × 0.02 mm = ? mm³", 0.004),
 S("Convert to mL: 0.004 mm³ = ? × 10⁻⁶ mL", 4),
 S("Cells/mL in diluted sample = 48 / (4 × 10⁻⁶) = ? × 10⁷", 1.2),
 S("Original = × 10 → ? × 10⁸ cells/mL", 1.2)],
"1.2 × 10⁸ cells/mL in the original culture.",
"Luôn tính **đúng thể tích thực sự đã đếm** (5 ô lớn chứ không phải toàn lưới), rồi mới nhân hệ số pha loãng.")

we("WE-08", "GRO-06", "Reading an MPN result",
"""Five tubes each were inoculated with 10 mL, 1 mL and 0.1 mL of a water sample. Positive tubes: 5, 3, 1.
The 5-tube MPN table gives an index of 110 MPN/100 mL for the combination 5-3-1 (95% limits 40–300).
(a) What does "5-3-1" mean? (b) Estimate bacteria per mL.""",
[S("How many tubes were positive at the 1 mL level?", 3),
 S("MPN per 100 mL = ?", 110),
 S("MPN per mL = 110/100 = ?", 1.1)],
"5 of 5 tubes at 10 mL, 3 of 5 at 1 mL, 1 of 5 at 0.1 mL were positive; MPN ≈ 110/100 mL ≈ 1.1/mL (95% CI 40–300/100 mL).",
"MPN là **ước lượng thống kê** – luôn báo kèm khoảng tin cậy; không phải số đếm chính xác.")

v("GRO-06", "direct microscopic count", "đếm trực tiếp dưới kính hiển vi", "Counting cells in a known volume with a counting chamber.", "The direct microscopic count includes dead cells.")
v("GRO-06", "Petroff-Hausser chamber", "buồng đếm Petroff-Hausser", "Counting chamber for bacteria: 400 small squares, 1 mm², depth 0.02 mm.", "Bacteria are counted in a Petroff-Hausser chamber.", ["Petroff-Hausser"])
v("GRO-06", "serial dilution", "pha loãng liên tiếp", "Stepwise dilution of a sample, e.g., tenfold each step.", "Serial dilution gives countable plates.", ["serial dilutions"])
v("GRO-06", "pour plate", "đổ đĩa (cấy trộn)", "Mixing a sample with melted agar before it solidifies.", "Pour plates use 1 mL of sample.", ["spread plate"])
v("GRO-06", "membrane filtration", "lọc màng", "Collecting bacteria from a large volume on a membrane filter placed on agar.", "Drinking water is tested by membrane filtration.")
v("GRO-06", "MPN", "số có khả năng nhất", "Most probable number: a statistical estimate from positive tubes in a dilution series.", "Coliforms are estimated by MPN.", ["most probable number"])

fc("GRO-06", "number", "Petroff-Hausser dimensions?", "25 × 16 = 400 small squares; 1 mm²; depth 0.02 mm; volume 2 × 10⁻⁵ mL.")
fc("GRO-06", "fact", "CFU/mL formula?", "Colonies ÷ (volume plated in mL × dilution).")
fc("GRO-06", "number", "Countable plate range?", "30–300 colonies.")
fc("GRO-06", "fact", "MPN principle?", "The more bacteria, the more dilution needed before no tubes grow; read from an MPN table.")
fc("GRO-06", "trap", "TRUE/FALSE: MPN gives an exact count.", "FALSE – it is a statistical estimate.")

# ---------------------------------------------------------------- GRO-07
unit("GRO-07", "Indirect methods: turbidity/OD, dry weight, metabolic activity; building a batch growth curve", "H", 3, 20, S6 + ": slides 28–33",
"""Nhà nghiên cứu cần theo dõi *E. coli* sinh trưởng **mỗi 30 phút** trong 10 giờ. Đếm khuẩn lạc thì phải chờ 1 ngày mới có kết quả. Giải pháp: đo **độ đục (OD₆₀₀)** bằng máy quang phổ – **mất 10 giây**. Nhưng độ đục phản ánh **sinh khối**, không phân biệt tế bào sống hay chết.""",
("A spectrophotometer reads 10% transmittance for a culture. What is its optical density (OD)?",
 ["0.1", "1.0", "2.0", "10"], 1,
 "Slide 30: **OD = 2 − log(%T)** = 2 − log 10 = 2 − 1 = **1,0**."),
[
("1. Độ đục – turbidity (slide 28–30)", """
- Vi khuẩn sinh trưởng làm dịch nuôi **đục**. Đo bằng **máy quang phổ (spectrophotometer)**:
  - Chùm sáng đi qua dịch tế bào tới **bộ thu (detector)**: **càng nhiều tế bào, càng ít ánh sáng tới bộ thu**.
  - Sự thay đổi ánh sáng chuyển thành **% độ truyền qua (% transmittance, %T)**.
- **Độ hấp thụ (absorbance) hay mật độ quang (optical density – OD)**: **OD = 2 − log(%T)**.
  - %T = 100 → OD = 0; %T = 10 → OD = 1; %T = 1 → OD = 2.
- Thường đo ở **600 nm (OD₆₀₀)**.
- **Cần pha loãng khi OD₆₀₀ > 0,7** (ngoài vùng tuyến tính).
- Quy đổi (slide): **OD₆₀₀ = 1 ≈ 8 × 10⁸ tế bào *E. coli*/mL**; ***S. cerevisiae*: ≈ 3 × 10⁷ tế bào/mL** (tế bào men to hơn nên cùng OD ít tế bào hơn).
- Ưu: **nhanh, không phá mẫu**. Nhược: **không phân biệt sống/chết**; cần ≥ 10⁶–10⁷ tế bào/mL mới đục; không dùng được cho nấm sợi.
"""),
("2. Khối lượng khô – dry weight (slide 31)", """
1. **Ly tâm** dịch tế bào → tách và thu **sinh khối**.
2. **Rửa** sinh khối (loại môi trường còn bám).
3. **Sấy** ở nhiệt độ thích hợp để tế bào **chỉ mất nước**, tới **khối lượng không đổi** → cân (g/L).
- Là phương pháp chính cho **nấm sợi** và trong công nghiệp (g DCW/L).
"""),
("3. Dựa vào hoạt động trao đổi chất (slide 32)", """
- Giả định lượng **sản phẩm trao đổi chất** (acid, CO₂, ATP) hoặc **cơ chất tiêu thụ** (O₂, glucose) **tỉ lệ với số tế bào**.
- Ví dụ: đo **lượng acid** tạo ra, **CO₂** thải ra, **O₂ tiêu thụ**, **ATP** (phát quang luciferase – kiểm tra vệ sinh bề mặt), khử thuốc nhuộm (resazurin, MTT). [mở rộng]
"""),
("4. Xây dựng đường cong sinh trưởng nuôi cấy mẻ (slide 33)", """
Các bước:
1. Chuẩn bị **giống vi khuẩn đã hoạt hóa** để cấy.
2. Chuẩn bị **môi trường lỏng** trong dụng cụ thích hợp.
3. **Cấy** giống vào môi trường.
4. **Nuôi** trong điều kiện thích hợp (nhiệt độ, lắc…).
5. **Lấy mẫu định kỳ**, xác định **mật độ sinh khối** bằng phương pháp phù hợp (OD, đếm khuẩn lạc, khối lượng khô…) **cho đến khi sinh khối giảm** theo thời gian nuôi.
6. **Vẽ đường cong** biểu diễn sự phụ thuộc của lượng sinh khối vào thời gian nuôi (log sinh khối – thời gian) → xác định các pha và **g**.
"""),
("5. Tổng hợp: chọn phương pháp nào?", """
| Câu hỏi | Phương pháp phù hợp |
|---|---|
| Cần kết quả **ngay**, theo dõi liên tục | **OD** |
| Chỉ tế bào **sống** | **plate count**, lọc màng, MPN |
| Mẫu **rất loãng** (nước) | **lọc màng**, MPN |
| **Nấm sợi**, công nghiệp | **khối lượng khô** |
| Tổng số tế bào (sống + chết) | **buồng đếm** |
"""),
],
[
("Lab và công nghiệp", """
- Trong lab sinh học phân tử, người ta cấy *E. coli* qua đêm, pha loãng rồi đợi đến **OD₆₀₀ ≈ 0,4–0,6** (giữa pha log) mới cảm ứng biểu hiện protein hay làm tế bào khả biến.
- Nồi lên men công nghiệp gắn **cảm biến quang học/điện dung** đo sinh khối trực tuyến, **cảm biến O₂ hòa tan, CO₂ khí thải** – chính là "phương pháp dựa trên trao đổi chất" ở quy mô lớn.
- Máy đo **ATP** cầm tay kiểm tra độ sạch bề mặt chế biến thực phẩm chỉ trong 15 giây.
"""),
],
[
("Turbidity", "A spectrophotometer measures light passing through a culture; more cells → less light reaches the detector → lower **% transmittance**. **OD = 2 − log(%T)**. Dilute when **OD₆₀₀ > 0.7**. **OD₆₀₀ = 1 ≈ 8 × 10⁸ *E. coli*/mL** (≈ 3 × 10⁷ *S. cerevisiae*/mL).", "OD = 2 − log %T; pha loãng khi > 0,7."),
("Dry weight and metabolic activity", "**Dry weight**: centrifuge, wash, dry to **constant mass**, weigh. **Metabolic activity**: measure products (acid, CO₂, ATP) or consumption (O₂) assumed proportional to cell number.", "Khối lượng khô; hoạt động trao đổi chất."),
("Batch growth curve", "Activate the inoculum → prepare liquid medium → inoculate → incubate → **sample periodically** and measure biomass until it declines → **plot biomass (log) vs time**.", "6 bước dựng đường cong sinh trưởng."),
],
["OD distinguishes live and dead cells", "OD = log(%T)", "Same OD means same cell number for yeast and E. coli"])

q("GRO-07", "calc", 2, "A culture shows 25% transmittance. What is its OD? (log 25 = 1.40)",
  ["1.40", "0.60", "0.25", "2.60"], 1,
  "OD = 2 − log(%T) = 2 − 1,40 = **0,60**.",
  ["Quên lấy 2 trừ.", "", "Nhầm %T với OD.", "Cộng thay vì trừ."], ["optical density"], "OD = log(%T)",
  steps=["OD = 2 − log %T", "= 2 − 1,40 = 0,60"])
q("GRO-07", "recall", 1, "According to the lecture, a culture should be diluted before measurement when OD600 is greater than about:",
  ["0.1", "0.7", "2.0", "5.0"], 1,
  "Slide 30: **cần pha loãng khi OD₆₀₀ > 0,7**.",
  ["Quá thấp.", "", "Quá cao.", "Quá cao."], ["optical density"], src=S6 + " slide 30")
q("GRO-07", "calc", 2, "An E. coli culture has OD600 = 0.35. Using OD600 = 1 ≈ 8 × 10⁸ cells/mL, estimate the cell density.",
  ["2.8 × 10⁸ cells/mL", "8 × 10⁸ cells/mL", "3.5 × 10⁷ cells/mL", "2.3 × 10⁹ cells/mL"], 0,
  "Tỉ lệ tuyến tính: 0,35 × 8 × 10⁸ = **2,8 × 10⁸ tế bào/mL**.",
  ["", "Đó là OD = 1.", "Sai.", "Chia thay vì nhân."], ["optical density"],
  steps=["C = OD × 8 × 10⁸", "= 0,35 × 8 × 10⁸ = 2,8 × 10⁸"])
q("GRO-07", "concept", 2, "Why does the same OD600 = 1 correspond to about 8 × 10⁸ E. coli/mL but only about 3 × 10⁷ S. cerevisiae/mL?",
  ["Yeast cells are larger, so fewer cells scatter the same amount of light", "Yeasts are transparent", "E. coli absorbs no light", "OD measures only live cells"], 0,
  "Tế bào nấm men **lớn hơn nhiều** → mỗi tế bào tán xạ nhiều ánh sáng hơn → cùng OD thì ít tế bào hơn.",
  ["", "Sai.", "Sai.", "OD không phân biệt sống/chết."], ["optical density"], "Same OD means same cell number for yeast and E. coli")
q("GRO-07", "not", 2, "Which is NOT a limitation of turbidity measurement?",
  ["It does not distinguish live from dead cells", "It needs fairly dense cultures", "It is slow, requiring 24–48 h incubation", "It is unsuitable for filamentous molds"], 2,
  "OD rất **nhanh** (vài giây). Chờ 24–48 h là nhược điểm của **plate count**.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["turbidity"], "OD distinguishes live and dead cells")
q("GRO-07", "recall", 1, "In the dry weight method, cells are dried until:",
  ["they turn black", "they reach a constant mass", "exactly 1 hour", "they form spores"], 1,
  "Slide 31: sấy đến khi tế bào **chỉ mất nước và đạt khối lượng không đổi**.",
  ["Sai.", "", "Không cố định thời gian.", "Sai."], ["dry weight"], src=S6 + " slide 31")
q("GRO-07", "concept", 2, "When constructing a batch growth curve, until when should samples be taken?",
  ["Only for the first hour", "Until the amount of biomass decreases with culture time", "Until the medium is sterile", "Only once at the end"], 1,
  "Slide 33: lấy mẫu định kỳ **cho đến khi sinh khối giảm** → thấy đủ 4 pha.",
  ["Không đủ.", "", "Sai.", "Không đủ."], ["growth curve"], src=S6 + " slide 33")
q("GRO-07", "calc", 2, "What is the OD of a sample with 1% transmittance?",
  ["0", "1", "2", "0.01"], 2,
  "OD = 2 − log 1 = 2 − 0 = **2**.",
  ["%T = 100.", "%T = 10.", "", "Sai."], ["optical density"], pool="mock",
  steps=["log 1 = 0", "OD = 2 − 0 = 2"])
q("GRO-07", "application", 2, "A researcher must follow bacterial growth every 30 min without waiting for incubation. The best method is:",
  ["plate counts", "turbidity (OD600)", "MPN", "dry weight"], 1,
  "OD cho kết quả **ngay lập tức**, không phá mẫu.",
  ["Cần 24–48 h.", "", "Cần ủ.", "Chậm, cần nhiều mẫu."], ["turbidity"], pool="mock")
q("GRO-07", "concept", 2, "Methods based on metabolic activity assume that:",
  ["cells are all dead", "the amount of a metabolic product or substrate used is proportional to the number of cells", "turbidity equals dry weight", "colonies come from single cells"], 1,
  "Giả định lượng **sản phẩm/cơ chất tiêu thụ tỉ lệ số tế bào**.",
  ["Sai.", "", "Sai.", "Sai."], ["metabolic activity"], pool="mock")

we("WE-09", "GRO-07", "From % transmittance to cell density",
"""An E. coli culture diluted 1:4 reads 20% transmittance at 600 nm. Use OD = 2 − log(%T), log 20 = 1.301, and OD600 = 1 ≈ 8 × 10⁸ cells/mL.
(a) OD of the diluted sample? (b) Is it in the reliable range (≤ 0.7)? (c) Cell density of the undiluted culture?""",
[S("OD = 2 − 1.301 = ? (3 decimals)", 0.699),
 S("Is OD ≤ 0.7? (1 = yes, 0 = no)", 1),
 S("Cells/mL in diluted sample = 0.699 × 8 × 10⁸ = ? × 10⁸ (2 decimals)", 5.59),
 S("Undiluted = × 4 → ? × 10⁹ cells/mL (2 decimals)", 2.24)],
"OD ≈ 0.70 (just within range); undiluted ≈ 2.2 × 10⁹ cells/mL.",
"Khi đo mẫu đã pha loãng, **nhân lại hệ số pha loãng**. Nếu OD > 0,7 phải pha loãng thêm rồi đo lại.")

we("WE-10", "GRO-07", "Reading a growth curve and finding g from OD data",
"""OD600 readings of a batch culture (OD proportional to cell number):
t (h):   0     1     2     3     4     5     6     7
OD600: 0.020 0.021 0.040 0.080 0.160 0.320 0.450 0.460
(a) Identify the lag phase. (b) Find the generation time during log phase. (c) When does stationary phase begin?""",
[S("The lag phase ends at t = ? h", 1),
 S("From 2 h to 5 h, OD increases from 0.040 to 0.320: fold increase = ?", 8),
 S("Number of generations n = log₂ 8 = ?", 3),
 S("g = 3 h / 3 = ? h", 1),
 S("Stationary phase begins at about t = ? h", 6)],
"Lag 0–1 h; log phase 1–5 h with g = 1 h (OD doubles each hour); stationary from about 6 h.",
"Trong pha log, OD **gấp đôi sau mỗi g**. Nhận diện pha log bằng các khoảng thời gian bằng nhau có hệ số tăng bằng nhau.")

v("GRO-07", "turbidity", "độ đục", "Cloudiness of a culture caused by cells scattering light.", "Turbidity increases as bacteria grow.")
v("GRO-07", "spectrophotometer", "máy quang phổ", "An instrument measuring light transmitted through a sample.", "OD is read on a spectrophotometer.")
v("GRO-07", "transmittance", "độ truyền quang", "The percentage of light passing through a sample (%T).", "Higher cell density lowers transmittance.", ["% transmittance", "percent transmittance"])
v("GRO-07", "optical density", "mật độ quang (OD)", "Absorbance; OD = 2 − log(%T).", "Dilute when optical density exceeds 0.7.", ["OD", "absorbance", "OD600"])
v("GRO-07", "metabolic activity", "hoạt động trao đổi chất", "Production of products or use of substrates, used to estimate cell numbers.", "CO2 production reflects metabolic activity.")

fc("GRO-07", "fact", "OD formula?", "OD = 2 − log(%T).")
fc("GRO-07", "number", "OD600 = 1 corresponds to?", "~8 × 10⁸ E. coli/mL; ~3 × 10⁷ S. cerevisiae/mL. Dilute if OD > 0.7.")
fc("GRO-07", "fact", "Dry weight steps?", "Centrifuge → wash → dry to constant mass → weigh.")
fc("GRO-07", "fact", "Six steps to construct a batch growth curve?", "Activate inoculum; prepare liquid medium; inoculate; cultivate; sample periodically until biomass declines; plot biomass vs time.")
