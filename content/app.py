from _lib import *

SCP = "Week-13 SCP reference (Sharif et al., Aquaculture 2021)"
ETH = "Week-14 Ethanol reference (Azolla filiculoides, Appl Biochem Biotechnol)"
PEN = "Week-15 Penicillin reference"

# ---------------------------------------------------------------- APP-01
unit("APP-01", "Single-cell protein (SCP): definition, composition and microbial sources", "M", 1, 20, SCP + ": sections 1–3, 8",
"""Thế giới cần thêm hàng chục triệu tấn protein mỗi năm, trong khi **bột cá** – nguyên liệu chính của thức ăn thủy sản – ngày càng đắt và khan hiếm. Một bồn lên men 100 m³ nuôi vi khuẩn *Methylophilus* hay nấm men có thể tạo ra lượng protein bằng cả cánh đồng đậu nành rộng hàng trăm hecta – và không phụ thuộc mùa vụ. Đó là **protein đơn bào (SCP)**.""",
("What is the protein content of SCP on a dry-matter basis according to the reference?",
 ["5–10%", "20–30%", "60–82%", "95–100%"], 2,
 "Tài liệu: SCP có **60–82% protein** trên chất khô, ngoài ra còn carbohydrate, nucleic acid, chất béo, khoáng, vitamin."),
[
("1. SCP là gì?", """
- **Single-cell protein (SCP) / protein đơn bào**: **sinh khối vi sinh vật** (tế bào khô hoặc protein chiết từ tế bào) của **vi khuẩn, nấm men, nấm sợi, vi tảo** dùng làm **thực phẩm hoặc thức ăn chăn nuôi**.
- Không phải protein tinh khiết: ngoài **protein 60–82% (chất khô)** còn có **carbohydrate, nucleic acid, chất béo, khoáng và vitamin**.
- Giàu **amino acid thiết yếu** như **lysine**, methionine (thiếu ở nhiều nguồn thực vật) → **thay thế bột cá, bột đậu nành** đắt tiền.
- Sản phẩm mục tiêu là **chính tế bào (sinh khối)** – khác ethanol (APP-03, chất chuyển hóa sơ cấp) và penicillin (APP-04, chất chuyển hóa thứ cấp).
- Mycoprotein từ nấm sợi (*Fusarium venenatum* – Quorn™) cũng được xếp vào SCP dù không phải \"đơn bào\".
"""),
("2. Ưu điểm dinh dưỡng và sản xuất", """
- **Sinh trưởng rất nhanh**: vi khuẩn **20–120 phút** (30 phút–2 h), nấm men **40 phút–3 h**, tảo **3–6 h** (2–4 h), nấm sợi 2–4 h. Tài liệu có chỗ ghi vi khuẩn và nấm men nhân đôi \"5–15 phút\" – con số quá thấp, học theo khoảng 20 phút–2 h. [mở rộng]
- **Hàm lượng protein cao (30–70%)** so với thực vật và động vật; dùng được **toàn bộ tế bào** (cây trồng, vật nuôi thì không).
- **Hồ sơ amino acid**: SCP vi khuẩn **gần giống protein cá**; SCP nấm men **gần giống protein đậu nành**.
- **Thiếu amino acid chứa lưu huỳnh (methionine, cysteine)**, giàu **lysine** → cần **bổ sung methionine, cysteine** khi làm thức ăn.
- **Vitamin**: vi khuẩn giàu **B12**, tảo giàu **vitamin A**; nhóm B (riboflavin, thiamine, pyridoxine, niacin, folic acid, biotin...).
- **Không phụ thuộc khí hậu, mùa vụ**, sản xuất quanh năm, ít đất; tận dụng **phụ phẩm, chất thải** làm cơ chất.
"""),
("3. Bốn nguồn vi sinh vật", """
| Nguồn | Protein | Nucleic acid | Điểm mạnh | Hạn chế | Ví dụ |
|---|---|---|---|---|---|
| **Vi khuẩn** | cao (đến ~**80%**; *Pseudomonas* trên paraffin **69%**) | **cao nhất** (RNA) | thế hệ **20–120 phút**; dùng nhiều cơ chất (tinh bột, đường, **methanol, ethanol**, dầu mỏ); protein \"tốt hơn nấm men, nấm\" | RNA cao, **nội độc tố (endotoxin)**, dễ nhiễm, tế bào nhỏ khó thu | ***Methylophilus methylotrophus*** (**thế hệ 2 h**, Pruteen), *Bacillus*, *Cellulomonas*, *Rhodopseudomonas*, *Pseudomonas* |
| **Tảo** | đến **70%** (SCP tảo ~**40%**) | **thấp: 3–8%** | **omega-3**, khoáng, vitamin, chlorophyll; dùng **năng lượng mặt trời, CO₂** | **mọc chậm, mật độ thấp 1–2 g/L**; thành cellulose khó tiêu | ***Spirulina*** (thực ra là **vi khuẩn lam**; người Aztec Mexico thu hoạch), ***Chlorella***, *Scenedesmus* |
| **Nấm sợi** | **30–50%** | **7–10%** | hồ sơ amino acid đạt chuẩn **FAO**; giàu **lysine, threonine**; nhiều vitamin B; dễ lọc | thiếu **cysteine, methionine**; mọc nhanh hơn nấm men nhưng **dễ nhiễm tạp**; có thể tạo **độc tố nấm** | ***Fusarium venenatum*** (mycoprotein – giảm insulin và đường huyết), ***Paecilomyces variotii* (quy trình Pekilo, Phần Lan)** |
| **Nấm men** | 45–55% [mở rộng] | cao | an toàn (GRAS), dễ tiêu hóa hơn nấm sợi | RNA cao | *Saccharomyces cerevisiae*, *Candida utilis*, ***Kluyveromyces fragilis*** (trên whey tạo được amino acid chứa S) |

- **Quy trình Pekilo (Phần Lan)**: nuôi **nấm sợi *Paecilomyces variotii*** trên **đường pentose, dịch thủy phân gỗ, nước thải sulfite** (ngành giấy) → SCP cho **thức ăn gia súc**.
"""),
],
[
("SCP ở Việt Nam và thế giới", """
- Công ty **Calysta, Unibio** sản xuất SCP từ **khí methane** bằng vi khuẩn *Methylococcus* cho thức ăn cá hồi, tôm.
- **Men bia thải** (*S. cerevisiae*) từ các nhà máy bia Việt Nam được sấy làm thức ăn chăn nuôi – một dạng SCP tận dụng phụ phẩm.
- **Spirulina** nuôi ở Ninh Thuận/Bình Thuận làm thực phẩm chức năng.
"""),
],
[
("SCP definition and composition", "**Single-cell protein** is microbial biomass (bacteria, yeasts, fungi, algae) used as food/feed. Protein **60–82% of dry matter**; also carbohydrates, nucleic acids, fats, minerals, vitamins. Rich in **lysine**; **deficient in S-amino acids (methionine, cysteine)**. Bacterial SCP resembles **fish protein**; yeast SCP resembles **soy protein**.", "SCP 60–82% protein."),
("Sources", "**Bacteria**: generation 20–120 min, e.g., *Methylophilus* (2 h); high RNA, endotoxins. **Algae**: protein up to 70%, **nucleic acid 3–8%**, omega-3, but slow growth (1–2 g/L); *Spirulina*, *Chlorella*. **Fungi**: protein **30–50%**, **nucleic acid 7–10%**, FAO-standard amino acids, rich in lysine and threonine; *Fusarium venenatum* mycoprotein; **Pekilo** process with ***Paecilomyces variotii*** (Finland).", "Vi khuẩn, tảo, nấm."),
],
["SCP is pure protein", "Algae have the highest nucleic acid content", "Fungal SCP is rich in methionine and cysteine", "Spirulina is a eukaryotic alga"])

q("APP-01", "recall", 1, "According to the reference, SCP contains how much protein on a dry-matter basis?",
  ["10–20%", "30–40%", "60–82%", "90–99%"], 2,
  "SCP: **60–82% protein** (chất khô).",
  ["Quá thấp.", "Nấm sợi 30–50%.", "", "SCP không phải protein tinh khiết."], ["single-cell protein"], "SCP is pure protein", src=SCP)
q("APP-01", "recall", 1, "The Pekilo process in Finland produced SCP using which organism?",
  ["Methylophilus methylotrophus", "Paecilomyces variotii (a filamentous fungus)", "Spirulina maxima", "Saccharomyces cerevisiae"], 1,
  "**Pekilo**: nấm sợi ***Paecilomyces variotii*** trên đường pentose, dịch thủy phân gỗ, nước thải sulfite.",
  ["Vi khuẩn methanol.", "", "Tảo lam.", "Nấm men."], ["Pekilo"], src=SCP)
q("APP-01", "recall", 1, "Which SCP source has the LOWEST nucleic acid content according to the reference?",
  ["Bacteria", "Algae (3–8%)", "Fungi (7–10%)", "Yeasts"], 1,
  "Tảo **3–8%**; nấm **7–10%**; vi khuẩn cao nhất.",
  ["Cao nhất.", "", "Cao hơn tảo.", "Cao."], ["nucleic acid"], "Algae have the highest nucleic acid content", src=SCP)
q("APP-01", "concept", 2, "SCP is described as deficient in which amino acids, so that supplementation is required when used as feed?",
  ["Lysine and threonine", "Methionine and cysteine (sulfur-containing)", "Glycine and alanine", "Glutamate and aspartate"], 1,
  "SCP thiếu amino acid **chứa lưu huỳnh**: **methionine, cysteine**; giàu lysine.",
  ["SCP giàu lysine, threonine.", "", "Sai.", "Sai."], ["amino acid"], "Fungal SCP is rich in methionine and cysteine", src=SCP)
q("APP-01", "recall", 1, "Fungi cultivated for SCP contain how much protein according to the reference?",
  ["3–8%", "30–50%", "60–82%", "above 90%"], 1,
  "Nấm: **30–50% protein**; amino acid đạt chuẩn FAO.",
  ["Nucleic acid tảo.", "", "SCP chung.", "Sai."], ["mycoprotein"], src=SCP)
q("APP-01", "concept", 2, "The amino acid profile of bacterial SCP most closely resembles that of:",
  ["soy protein", "fish protein", "wheat gluten", "gelatin"], 1,
  "SCP vi khuẩn **giống protein cá**; SCP nấm men **giống protein đậu nành**.",
  ["Nấm men.", "", "Sai.", "Sai."], ["single-cell protein"], src=SCP)
q("APP-01", "recall", 1, "Methylophilus, a bacterial SCP producer, has a generation time of about:",
  ["2 hours", "2 days", "2 weeks", "20 seconds"], 0,
  "Tài liệu: *Methylophilus* spp. có thời gian thế hệ **2 h**.",
  ["", "Sai.", "Sai.", "Sai."], ["generation time"], src=SCP)
q("APP-01", "not", 2, "Which is NOT a listed advantage of algae as SCP sources?",
  ["Protein content up to 70%", "Good source of omega-3 fatty acids", "Low nucleic acid content (3–8%)", "Very fast growth to high density (>50 g/L)"], 3,
  "Tảo **mọc chậm, mật độ thấp (1–2 g/L)** – là nhược điểm.",
  ["Có.", "Có.", "Có.", ""], ["algae"], src=SCP)
q("APP-01", "recall", 1, "Which organism is the source of mycoprotein mentioned in the reference?",
  ["Fusarium venenatum", "Chlorella vulgaris", "Bacillus subtilis", "Penicillium chrysogenum"], 0,
  "Mycoprotein từ ***Fusarium venenatum*** – được báo cáo làm giảm insulin và đường huyết.",
  ["", "Tảo.", "Vi khuẩn.", "Sản xuất penicillin."], ["mycoprotein"], pool="mock")
q("APP-01", "not", 2, "Which is NOT a component of SCP besides protein, according to the reference?",
  ["Carbohydrates", "Nucleic acids", "Vitamins and minerals", "Peptidoglycan-free pure amino acids only"], 3,
  "SCP gồm protein + carbohydrate, nucleic acid, chất béo, khoáng, vitamin; không phải amino acid tinh khiết.",
  ["Có.", "Có.", "Có.", ""], ["single-cell protein"], pool="mock")
q("APP-01", "concept", 2, "Why is vitamin B12 mentioned as an advantage of bacterial SCP?",
  ["Bacteria cannot make B12", "Bacteria are reported to contain high vitamin B12, while algae are rich in vitamin A", "B12 is toxic", "Only fungi make B12"], 1,
  "Tài liệu: **vi khuẩn giàu B12**, **tảo giàu vitamin A**.",
  ["Ngược.", "", "Sai.", "Sai."], ["single-cell protein"], pool="mock")
q("APP-01", "application", 2, "A feed company wants an SCP with the lowest nucleic acid content to reduce uric-acid risk. Which source fits best?",
  ["Bacterial SCP", "Algal SCP", "Fungal SCP", "Yeast SCP"], 1,
  "**Tảo 3–8%** nucleic acid – thấp nhất.",
  ["RNA cao nhất.", "", "7–10%.", "Cao."], ["nucleic acid"], pool="mock")

v("APP-01", "single-cell protein", "protein đơn bào (SCP)", "Microbial biomass used as a protein source for food or feed.", "Single-cell protein can replace fish meal.", ["SCP"])
v("APP-01", "biomass", "sinh khối", "The mass of cells produced.", "Biomass is harvested by centrifugation.")
v("APP-01", "mycoprotein", "protein nấm (mycoprotein)", "Protein-rich biomass of filamentous fungi, e.g., Fusarium venenatum.", "Mycoprotein is used in meat substitutes.")
v("APP-01", "Pekilo", "quy trình Pekilo", "Finnish process growing Paecilomyces variotii on wood hydrolysates and sulfite waste for feed SCP.", "The Pekilo process used pentoses.", ["Paecilomyces variotii"])
v("APP-01", "Methylophilus", "vi khuẩn Methylophilus", "Methanol-using bacterium with a 2-h generation time used for SCP.", "Methylophilus grows on methanol.", ["Methylophilus methylotrophus"])
v("APP-01", "Spirulina", "tảo xoắn Spirulina", "Cyanobacterium harvested as food; protein-rich.", "Spirulina was eaten in Mexico.")
v("APP-01", "Chlorella", "tảo Chlorella", "Eukaryotic green microalga used as feed.", "Chlorella is an algal SCP source.")
v("APP-01", "fish meal", "bột cá", "Protein-rich feed made from fish, a target for SCP replacement.", "SCP replaced fish meal in salmon diets.", ["fishmeal"])
v("APP-01", "essential amino acid", "amino acid thiết yếu", "Amino acid that must be supplied in the diet, e.g., lysine.", "SCP is rich in essential amino acids.", ["essential amino acids", "lysine", "methionine"])

fc("APP-01", "number", "SCP protein content (dry matter)?", "60–82%.")
fc("APP-01", "number", "Nucleic acid: algae vs fungi?", "Algae 3–8%; fungi 7–10%; bacteria highest.")
fc("APP-01", "fact", "SCP amino acid limitation?", "Deficient in S-amino acids (methionine, cysteine); rich in lysine.")
fc("APP-01", "fact", "Pekilo process?", "Finland; filamentous fungus Paecilomyces variotii on pentoses, wood hydrolysates, sulfite waste; animal feed.")
fc("APP-01", "fact", "Bacterial vs yeast SCP amino acid profile?", "Bacterial ≈ fish protein; yeast ≈ soy protein.")

# ---------------------------------------------------------------- APP-02
unit("APP-02", "SCP production: substrates, C:N ratio, fermentation types, challenges and aquaculture use", "M", 2, 25, SCP + ": sections 4–13",
"""Nước thải nhà máy đường, bia, sữa có **BOD rất cao** – thải thẳng ra sông gây ô nhiễm, xử lý thì tốn tiền. Nếu dùng chính dòng thải đó làm môi trường nuôi vi sinh vật tạo SCP, BOD giảm tới **~80%** và ta thu thêm protein. Nhưng muốn tế bào tạo protein, phải cấp đủ **nitrogen** theo đúng **tỉ lệ C:N**.""",
("Which C:N ratio is reported as most appropriate for SCP production media?",
 ["1:1", "10:1", "100:1", "1:10"], 1,
 "Tỉ lệ **C:N = 10:1** được báo cáo là thích hợp nhất (giống tỉ lệ trong tế bào vi sinh vật)."),
[
("1. Cơ chất (substrate)", """
- Vi sinh vật cần **mono- và disaccharide** làm \"viên gạch\" → carbohydrate là cơ chất phổ biến (dễ có, năng lượng cao).
- Cơ chất khác: **rỉ đường (molasses), whey (váng sữa), tinh bột, alkane, hydrocarbon**, methanol, ethanol; phụ phẩm **nông nghiệp, công nghiệp**.
- **Chi phí cơ chất = 45–75% tổng chi phí sản xuất SCP**; phần lớn là **nguồn carbon**, amonia chỉ **7–15%** tổng cơ chất.
- **CO₂ khí quyển miễn phí** (cho tảo) nhưng tốn năng lượng **khuấy** để hòa tan vào dịch tảo đặc.
- **Chất thải nông – công nghiệp**: rẻ, dồi dào, chiếm **20–30%** chi phí; dùng chúng **giảm BOD ~80%** và giảm chi phí xử lý chất thải. Chất thải rắn (**cellulose**) cần **tiền xử lý đặc biệt, đắt**.
- **Hydrocarbon** (khí tự nhiên, dầu mỏ) chiếm **30–70%** chi phí; **không tái tạo**, đắt, **gây tranh cãi chính trị** vì cạnh tranh với nhiên liệu.
"""),
("2. Nguồn nitrogen và tỉ lệ C:N", """
- Nguồn N: **amonia, muối amoni, nitrate**.
- **C:N = 10:1** thích hợp nhất (bằng tỉ lệ trong tế bào vi sinh vật), tuy khác nhau giữa các loài.
  - **Tỉ lệ cao hơn** (thừa C): **amonia cạn trước khi đường được dùng hết** → không đạt sinh khối mong muốn.
  - **Tỉ lệ 1:1** (thừa N): phần lớn **amonia không vào được tế bào, bị lãng phí**.
- Nhớ: protein cần **N**; khi N giới hạn, thêm đường không tạo thêm protein.
"""),
("3. Quy trình sản xuất công nghiệp (Hình 1)", """
**Phát triển (development)**: **sàng lọc** chủng từ đất, không khí, nước → **tối ưu bằng đột biến, chọn lọc**, kỹ thuật di truyền → tối ưu điều kiện nuôi → xác định cấu trúc tế bào, con đường chuyển hóa → nâng cấp thiết bị, kỹ thuật quy trình → **bảo hộ, an toàn**, cấp phép.

**Sản xuất**: chọn chủng → **lên men** (chìm hoặc rắn) trên cơ chất phù hợp → tăng sinh khối → **thu hoạch** → xử lý tiếp: **tinh sạch, phá tế bào, rửa, chiết protein** → sấy.

**Thu hồi tế bào**: **vi khuẩn – ly tâm (centrifugation)**; **nấm sợi – lọc (filtration)**. Nên thu hồi tối đa nước vì chứa chất dinh dưỡng hòa tan.
"""),
("4. Ba kiểu lên men", """
| Kiểu | Đặc điểm (theo tài liệu) |
|---|---|
| **Lên men chìm (submerged)** | cơ chất luôn ở **dạng lỏng** chứa đủ dinh dưỡng; trong **fermenter** vận hành **liên tục**, sinh khối thu liên tục; **ly tâm hoặc lọc rồi sấy**; cần **sục khí** và **làm mát** (sinh nhiệt) |
| **Lên men bán rắn (semisolid)** | chuẩn bị cơ chất quan trọng (dạng rắn); **vốn đầu tư và chi phí vận hành cao**; hệ đa pha: trộn, khuấy, truyền O₂ từ bọt khí qua pha lỏng tới tế bào, truyền nhiệt; thiết bị **U-loop fermenter**; nguồn C: hydrocarbon khí, n-alkene, ethanol, methanol, polysaccharide, rỉ đường, nước thải bia |
| **Lên men rắn (solid-state)** | cơ chất **rắn** (**cám mì, cám gạo**) trải trên **khay phẳng** sau khi cấy; **độ ẩm 60–65%**; sản phẩm: SCP, enzyme, thức ăn, acid hữu cơ, ethanol, sắc tố, vitamin B, hương liệu |

- Lưu ý: \"chìm/rắn\" nói về **môi trường vật lý**; \"mẻ/fed-batch/liên tục\" nói về **chế độ cấp liệu** – hai trục khác nhau (nuôi chìm cũng có thể chạy mẻ). [mở rộng]
"""),
("5. Thách thức khi dùng SCP", """
- **Yếu tố kháng dinh dưỡng chính: nucleic acid cao** → tăng **acid uric huyết thanh** → **sỏi thận**. **70–80% nitrogen** ở dạng amino acid, phần còn lại là nucleic acid (đặc điểm của vi sinh vật mọc nhanh).
- **Thành tế bào không tiêu hóa được** ở động vật dạ dày đơn và gia cầm.
- Tế bào sống phải được **bất hoạt trước khi dùng** (màu, vị khó chịu; nguy cơ nhiễm trùng da, tiêu hóa, buồn nôn).
- **Nấm sợi**: mọc nhanh hơn nấm men nhưng **nguy cơ nhiễm tạp cao hơn**. **Vi khuẩn**: **RNA cao, nguy cơ nhiễm tạp, nội độc tố**.
- **Độc tố**: **mycotoxin** (nấm), **cyanotoxin** (vi khuẩn lam); chất gây ung thư khi đột biến.
- Tảo \"không có độc tố\" (theo tài liệu) nhưng **mọc chậm, mật độ 1–2 g/L**.
- Khắc phục: **tối ưu quy trình lên men**, chọn chủng và cơ chất phù hợp; **loại nucleic acid** bằng xử lý lý – hóa (vd sốc nhiệt kích hoạt RNase nội sinh [mở rộng]).
"""),
("6. Ứng dụng trong nuôi trồng thủy sản", """
- SCP thay **bột cá / bột đậu nành** trong khẩu phần cá hồi, cá hồi vân, tôm... Ví dụ trong tài liệu:
  - nấm men *K. marxianus, C. utilis, S. cerevisiae* thay bột cá/đậu nành đến **~24%** không ảnh hưởng tăng trưởng;
  - khẩu phần cá hồi Đại Tây Dương chứa **36% SCP vi khuẩn**; SCP vi khuẩn (*Methylococcus*) chiếm tới **38%** protein khẩu phần cá hồi vân và **52%** ở cá hồi không ảnh hưởng xấu;
  - bột biofloc đến **30%** trong khẩu phần tôm.
- Kết quả phụ thuộc **loài, giai đoạn, loại SCP, khẩu phần nền** – không suy rộng cho mọi loài.
"""),
],
[
("Kinh tế tuần hoàn", """
Mô hình **\"chất thải → SCP → thức ăn → thủy sản\"** giúp giảm BOD nước thải và giảm phụ thuộc bột cá nhập khẩu. Nhưng sản phẩm từ chất thải vẫn phải qua **kiểm tra an toàn** (kim loại nặng, độc tố, vi sinh vật gây bệnh). Liên hệ CTL: tế bào phải được **bất hoạt** (sấy, gia nhiệt) trước khi dùng.
"""),
],
[
("Substrates and costs", "Carbohydrates (mono/disaccharides), **molasses, whey, starch, alkanes, hydrocarbons**, agro-industrial wastes. **Substrate = 45–75% of total cost**, mostly the carbon source (ammonia 7–15%). Wastes are cheap (20–30% of cost) and reduce **BOD by ~80%**; hydrocarbons (30–70% of cost) are non-renewable and controversial.", "Cơ chất 45–75% chi phí."),
("C:N ratio and processes", "N sources: ammonia, ammonium salts, nitrate. **C:N = 10:1** is most appropriate; higher ratio → ammonia runs out before sugar; **1:1** → ammonia wasted. **Submerged** (liquid, continuous, centrifuge/filter, aeration + cooling), **semisolid** (high capital/operating cost, U-loop fermenter), **solid-state** (wheat/rice bran on flat beds, **moisture 60–65%**). Bacteria recovered by **centrifugation**, filamentous fungi by **filtration**.", "C:N 10:1."),
("Challenges", "Main anti-nutritional factor: **high nucleic acid** → serum **uric acid** → **kidney stones**; 70–80% of N is amino acid. Indigestible cell walls; live cells must be inactivated; fungi: contamination risk; bacteria: RNA, contamination, **endotoxins**; **mycotoxins, cyanotoxins**; algae slow (1–2 g/L).", "Nucleic acid → acid uric."),
],
["A C:N ratio of 1:1 is optimal", "Filamentous fungi are recovered by centrifugation", "Solid-state fermentation needs no moisture"])

q("APP-02", "recall", 1, "What proportion of total SCP production cost is typically due to substrates?",
  ["5–10%", "20–30%", "45–75%", "over 95%"], 2,
  "Cơ chất = **45–75%** tổng chi phí (chủ yếu nguồn carbon).",
  ["Sai.", "Chất thải nông–công nghiệp.", "", "Sai."], ["substrate"], src=SCP)
q("APP-02", "concept", 2, "What happens if the C:N ratio of the medium is much higher than 10:1?",
  ["Ammonia is wasted because it cannot enter cells", "Ammonia disappears before all sugars are consumed, so the required biomass is not obtained", "Cells grow faster", "Nucleic acid content falls to zero"], 1,
  "Thừa C → **amonia cạn trước khi đường được dùng hết** → không đạt sinh khối. (1:1 thì amonia bị lãng phí.)",
  ["Đó là tỉ lệ 1:1.", "", "Sai.", "Sai."], ["C:N ratio"], "A C:N ratio of 1:1 is optimal", src=SCP)
q("APP-02", "recall", 1, "In SCP production, bacteria and filamentous fungi are usually recovered respectively by:",
  ["filtration; centrifugation", "centrifugation; filtration", "distillation; extraction", "sedimentation; distillation"], 1,
  "Vi khuẩn nhỏ → **ly tâm**; nấm sợi → **lọc**.",
  ["Ngược.", "", "Sai.", "Sai."], ["centrifugation"], "Filamentous fungi are recovered by centrifugation", src=SCP)
q("APP-02", "recall", 1, "Solid-state fermentation for SCP uses substrates such as wheat or rice bran spread on flat beds at a moisture level of:",
  ["5–10%", "20–30%", "60–65%", "95–100%"], 2,
  "Độ ẩm **60–65%**.",
  ["Quá khô.", "Sai.", "", "Là lên men chìm."], ["solid-state fermentation"], "Solid-state fermentation needs no moisture", src=SCP)
q("APP-02", "concept", 2, "Why is high nucleic acid content the main anti-nutritional factor of SCP?",
  ["It causes vitamin deficiency", "It raises serum uric acid, which can lead to kidney stones", "It is indigestible fiber", "It lowers protein content to zero"], 1,
  "Nucleic acid (purine) → **acid uric** huyết thanh ↑ → **sỏi thận**.",
  ["Sai.", "", "Đó là thành tế bào.", "Sai."], ["nucleic acid", "uric acid"], src=SCP)
q("APP-02", "not", 2, "Which statement about submerged fermentation for SCP (as described in the reference) is NOT correct?",
  ["The substrate is in liquid form with all nutrients", "It is carried out in a fermenter operated continuously", "Aeration and cooling are needed because heat is generated", "It uses dry bran on flat trays with 60–65% moisture"], 3,
  "Khay cám ẩm 60–65% là **lên men rắn**.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["submerged fermentation"], src=SCP)
q("APP-02", "recall", 1, "Using agro-industrial wastes for SCP production reduces their biological oxygen demand (BOD) by almost:",
  ["10%", "30%", "80%", "100%"], 2,
  "Giảm BOD **gần 80%** và giảm chi phí xử lý.",
  ["Sai.", "Sai.", "", "Sai."], ["BOD"], src=SCP)
q("APP-02", "concept", 2, "Why are hydrocarbons considered a problematic substrate for SCP?",
  ["They contain no carbon", "They are non-renewable, expensive (30–70% of cost) and politically controversial because they are also fuels", "They are toxic to all bacteria", "They contain too much nitrogen"], 1,
  "Hydrocarbon từ khí/dầu **không tái tạo**, đắt, cạnh tranh nhiên liệu.",
  ["Sai.", "", "Nhiều vi khuẩn dùng được.", "Sai."], ["substrate"], pool="mock")
q("APP-02", "recall", 1, "According to the reference, semisolid fermentation for SCP:",
  ["requires low investment", "requires high capital investment and operating cost; a U-loop fermenter is used to study mass and energy transport", "uses no oxygen", "is only used for algae"], 1,
  "Lên men bán rắn: **vốn và chi phí vận hành cao**; **U-loop fermenter**.",
  ["Ngược.", "", "Sai.", "Sai."], ["semisolid fermentation"], pool="mock")
q("APP-02", "not", 2, "Which is NOT listed as a limitation of bacterial SCP?",
  ["High RNA content", "Risk of contamination", "Endotoxins", "Very low protein content (below 10%)"], 3,
  "Vi khuẩn có protein **cao**; hạn chế là RNA, nhiễm tạp, nội độc tố.",
  ["Có.", "Có.", "Có.", ""], ["endotoxin"], pool="mock")
q("APP-02", "calc", 2, "A batch culture's dry biomass rises from 2 to 14 g/L while the substrate falls from 50 to 20 g/L. What is the biomass yield on substrate consumed (Yx/s)?",
  ["0.28 g/g", "0.40 g/g", "0.47 g/g", "0.70 g/g"], 1,
  "Y = (14 − 2)/(50 − 20) = 12/30 = **0,40 g/g**.",
  ["Dùng 14/50 – sai cơ sở.", "", "Dùng 14/30.", "Sai."], ["biomass yield"], pool="mock")
q("APP-02", "calc", 2, "100 kg of dry biomass contains 45% protein, and processing retains 90% of the protein. How much protein remains in the product?",
  ["40.5 kg", "45 kg", "50 kg", "90 kg"], 0,
  "100 × 0,45 × 0,90 = **40,5 kg**.",
  ["", "Quên hệ số thu hồi.", "Sai.", "Sai."], ["single-cell protein"])

v("APP-02", "substrate", "cơ chất", "The raw material microbes use for growth.", "Molasses is a common substrate.", ["substrates"])
v("APP-02", "molasses", "rỉ đường", "Sugar-rich by-product of sugar refining used as a substrate.", "Yeast SCP is grown on molasses.")
v("APP-02", "whey", "váng sữa (whey)", "Lactose-rich by-product of cheese making.", "Kluyveromyces grows on whey.")
v("APP-02", "C:N ratio", "tỉ lệ C:N", "Ratio of carbon to nitrogen in a medium; 10:1 recommended for SCP.", "A high C:N ratio exhausts ammonia first.")
v("APP-02", "BOD", "nhu cầu oxy sinh hóa (BOD)", "Biological oxygen demand, a measure of organic pollution.", "SCP production reduces waste BOD.", ["biological oxygen demand"])
v("APP-02", "submerged fermentation", "lên men chìm", "Cultivation in a liquid medium.", "Submerged fermentation is aerated and cooled.")
v("APP-02", "semisolid fermentation", "lên men bán rắn", "Cultivation with solid substrates in a multiphase system.", "Semisolid fermentation needs high investment.")
v("APP-02", "solid-state fermentation", "lên men rắn", "Cultivation on moist solid substrates like bran.", "Solid-state fermentation keeps 60–65% moisture.")
v("APP-02", "centrifugation", "ly tâm", "Separation by spinning at high speed.", "Bacteria are harvested by centrifugation.")
v("APP-02", "uric acid", "acid uric", "Purine breakdown product; excess causes kidney stones and gout.", "High RNA raises uric acid.")
v("APP-02", "endotoxin", "nội độc tố", "Lipid A of Gram-negative LPS released from cells.", "Bacterial SCP may contain endotoxin.", ["endotoxins"])
v("APP-02", "biomass yield", "hiệu suất sinh khối", "Biomass formed per substrate consumed (Yx/s).", "The biomass yield was 0.4 g/g.", ["Yx/s"])
v("APP-02", "mycotoxin", "độc tố nấm", "Toxic secondary metabolite of fungi.", "Aflatoxin is a mycotoxin.", ["mycotoxins", "cyanotoxins"])

fc("APP-02", "number", "Substrate share of SCP cost?", "45–75% (carbon source dominates; ammonia 7–15%).")
fc("APP-02", "fact", "C:N ratio effects?", "10:1 optimal; higher → ammonia exhausted before sugar; 1:1 → ammonia wasted.")
fc("APP-02", "fact", "Three fermentation types for SCP?", "Submerged (liquid, continuous), semisolid (high cost, U-loop), solid-state (bran, 60–65% moisture).")
fc("APP-02", "fact", "Main SCP challenge?", "High nucleic acid → uric acid → kidney stones; also indigestible walls, toxins, contamination.")
fc("APP-02", "number", "BOD reduction when wastes are used for SCP?", "About 80%.")

we("WE-14", "APP-02", "Biomass yield and recovered protein",
   "A yeast batch culture (constant volume) goes from 1.5 to 21.5 g/L dry biomass while glucose falls from 60 to 10 g/L. The harvested biomass (dry) contains 48% protein and downstream processing keeps 85% of the protein. Find Yx/s and the protein in the product per litre of culture.",
   [S("Biomass formed (g/L) = 21.5 − 1.5?", 20),
    S("Substrate consumed (g/L) = 60 − 10?", 50),
    S("Yx/s (g/g)?", 0.4),
    S("Protein in harvested biomass (g/L) = 21.5 × 0.48?", 10.32),
    S("Protein kept after processing (g/L) = 10.32 × 0.85?", 8.772)],
   "Yx/s = 0.40 g/g; ≈ 8.77 g protein per litre",
   "Hiệu suất sinh khối dùng phần **tạo thêm** chia phần **đã tiêu thụ**. Protein thu được = sinh khối khô × phần protein × hệ số thu hồi (dùng số thập phân: 48% = 0,48).")

# ---------------------------------------------------------------- APP-03
unit("APP-03", "Bioethanol production: alcoholic fermentation, yeasts and the Azolla case study", "H", 2, 25, ETH,
"""Xăng E5 và E10 ở Việt Nam chứa 5–10% **ethanol sinh học** làm từ sắn. Thế hệ nhiên liệu sinh học tiếp theo dùng nguyên liệu **không cạnh tranh lương thực** – như **bèo hoa dâu *Azolla***, mọc dày đặc trên ao cá. Nhưng *Azolla* chứa cả **glucose và xylose** sau thủy phân, và không phải nấm men nào cũng lên men được xylose.""",
("What is the theoretical maximum ethanol yield from glucose (g ethanol per g glucose)?",
 ["1.0 g/g", "0.511 g/g", "2.0 g/g", "0.25 g/g"], 1,
 "C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂: 2 × 46,07 / 180,16 = **0,511 g/g**. Phần còn lại đi ra dưới dạng CO₂."),
[
("1. Lên men rượu – cơ sở sinh hóa", """
- **Đường phân (glycolysis)**: glucose → 2 pyruvate + **2 ATP (ròng)** + 2 NADH.
- **Nhánh lên men rượu** (nấm men): pyruvate → **acetaldehyde + CO₂** (pyruvate decarboxylase) → acetaldehyde + NADH → **ethanol + NAD⁺** (alcohol dehydrogenase).
- Ý nghĩa: bước tạo ethanol **tái sinh NAD⁺** để đường phân tiếp tục; **không tạo thêm ATP**.
- Phương trình tổng: **C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂**.

> **Hiệu suất lý thuyết** = 2 × 46,07 / 180,16 = **0,511 g ethanol/g glucose** (≈ 51,1%).

- **Hiệu ứng Crabtree**: *S. cerevisiae* vẫn tạo ethanol **khi có O₂** nếu đường cao. Ethanol là **sản phẩm sơ cấp** (gắn chuyển hóa trung tâm, tạo trong pha sinh trưởng). Liên hệ FUN-02. [mở rộng]
"""),
("2. Nguyên liệu Azolla filiculoides", """
- ***Azolla*** là chi **dương xỉ thủy sinh nổi** (7 loài) – **không phải tảo**; cộng sinh với **vi khuẩn lam cố định đạm *Anabaena azollae*** → mọc tốt ở nước nghèo N; sinh khối lớn, rẻ, dễ thu hoạch.
- Thành phần (Bảng 1): **carbohydrate tổng 47,7%**; **cellulose 11,3%, hemicellulose 14,0%, lignin 28,9%**; protein ~23%.
- Là nguyên liệu **lignocellulose** → cần **tiền xử lý + đường hóa** để giải phóng đường đơn.
"""),
("3. Quy trình SHF – thủy phân và lên men tách riêng", """
1. **Thủy phân acid nhiệt (thermal acid hydrolysis)**: tối ưu **14% (w/v) Azolla**, **200 mM H₂SO₄**, **121 °C, 60 phút** → **16,7 g/L** đường đơn (hiệu quả ~25%). So sánh HCl, HNO₃, H₂SO₄: **H₂SO₄ tốt nhất**. Quá 60 phút → xylose bị phân hủy.
2. **Đường hóa bằng enzyme (enzymatic saccharification)**: so sánh Celluclast, **Viscozyme**, Cellic C-Tec2 → **Viscozyme** tốt nhất (chứa cellulase + hemicellulase); **16 U/mL**, **48 h** → **61,6 g/L** đường đơn (hiệu quả **92,2%**). Quá 16 U/mL không tăng thêm đáng kể.
3. **Lên men**: 100 mL dịch thủy phân trong bình 250 mL, **bán yếm khí**, **30 °C, 150 rpm**, 0–72 h; ethanol đo bằng **HPLC**; sinh khối nấm men theo **OD₆₀₀** + đường chuẩn.

- **SHF** (separate hydrolysis and fermentation): đường hóa trước, lên men sau – mỗi bước ở điều kiện tối ưu riêng. **SSF** (simultaneous saccharification and fermentation) làm đồng thời. [mở rộng]
"""),
("4. So sánh bốn nấm men", """
Dịch thủy phân có **glucose 27,8 g/L + xylose 33,2 g/L**.

| Nấm men | Ethanol cực đại | Y_EtOH (g/g đường ban đầu) | Dùng đường |
|---|---|---|---|
| ***Kluyveromyces marxianus*** | **26,8 g/L** | **0,43** | **dùng hết cả glucose và xylose trong 60 h** |
| *Candida lusitaniae* | 23,2 g/L | 0,37 | glucose + phần lớn xylose |
| *Pichia stipitis* | 18,2 g/L | 0,29 | glucose + một phần xylose |
| ***Saccharomyces cerevisiae*** | 13,7 g/L | 0,22 | **chỉ glucose**; **33,2 g/L xylose còn nguyên** |

- Kết luận bài báo: ***K. marxianus*** phù hợp nhất cho dịch Azolla; ***S. cerevisiae*** (chủng tự nhiên) **cho hiệu suất thấp nhất** vì **chỉ dùng glucose**, không lên men đường **pentose (xylose)**.
- Lưu ý: phần tóm tắt (abstract) bài báo đảo số của *S. cerevisiae* và *P. stipitis*; Hình 6 và kết luận cho số như bảng trên.
- **Y_EtOH = [EtOH]max / [đường đơn ban đầu (glucose + xylose)]** (phương trình 3) – tính trên **đường ban đầu**, không phải đường đã tiêu thụ.
"""),
("5. Hai cơ sở hiệu suất", """
> **Y trên đường tiêu thụ** = ethanol / (S₀ − S_f); **Y trên đường ban đầu** = ethanol / S₀ = Y_tiêu thụ × phần đường đã dùng.
> **% lý thuyết** = Y thực / 0,511 × 100%.

Ví dụ: 100 g glucose, dùng 80 g, tạo 36 g ethanol → Y tiêu thụ = 0,45 g/g (**88%** lý thuyết); Y ban đầu = 0,36 g/g (**70,4%**).
"""),
],
[
("Nhiên liệu sinh học thế hệ 1, 2, 3", """
- **Thế hệ 1**: tinh bột, đường (sắn, mía, ngô) – cạnh tranh lương thực. Việt Nam: xăng **E5 RON92**, lộ trình E10.
- **Thế hệ 2**: **lignocellulose** (rơm rạ, bã mía, Azolla) – cần tiền xử lý, enzyme cellulase; khó khăn là lên men **xylose** → dùng *K. marxianus*, *Scheffersomyces stipitis* hoặc *S. cerevisiae* biến đổi gene.
- **Thế hệ 3**: vi tảo.
- *K. marxianus* còn **chịu nhiệt** (đến 45 °C) – thích hợp **SSF** vì gần nhiệt độ tối ưu của cellulase.
"""),
],
[
("Alcoholic fermentation", "Glycolysis gives 2 pyruvate, **2 ATP net**, 2 NADH; pyruvate → acetaldehyde + CO₂ → ethanol, **regenerating NAD⁺**. C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂; theoretical yield **0.511 g/g**.", "0,511 g/g."),
("Azolla study process", "*Azolla filiculoides* = floating aquatic **fern** with N-fixing cyanobacterium *Anabaena azollae*; carbohydrate 47.7%. **SHF**: thermal acid hydrolysis (**14% w/v, 200 mM H₂SO₄, 121 °C, 60 min → 16.7 g/L**), enzymatic saccharification (**Viscozyme 16 U/mL, 48 h → 61.6 g/L**), fermentation (semianaerobic, 30 °C, 150 rpm; HPLC).", "Tiền xử lý acid → Viscozyme → lên men."),
("Yeast comparison", "*K. marxianus* **26.8 g/L (Y = 0.43)** – used glucose + xylose completely within 60 h (best); *C. lusitaniae* 23.2 g/L (0.37); *P. stipitis* 18.2 (0.29); *S. cerevisiae* 13.7 (0.22) – **used only glucose** (xylose left). Y_EtOH = max ethanol / initial monosaccharides.", "K. marxianus tốt nhất."),
],
["The ethanol step produces extra ATP", "Theoretical yield is 1 g ethanol per g glucose", "Azolla is an alga", "S. cerevisiae ferments xylose well"])

q("APP-03", "recall", 1, "Which yeast gave the highest ethanol concentration (26.8 g/L, Y = 0.43) from Azolla hydrolysate?",
  ["Saccharomyces cerevisiae", "Pichia stipitis", "Kluyveromyces marxianus", "Candida lusitaniae"], 2,
  "***K. marxianus*** – dùng hết cả glucose và xylose trong 60 h.",
  ["Thấp nhất.", "Trung bình.", "", "Thứ hai (23,2 g/L)."], ["Kluyveromyces marxianus"], src=ETH)
q("APP-03", "concept", 2, "Why did Saccharomyces cerevisiae give the lowest ethanol yield from Azolla hydrolysate?",
  ["It was killed by acid", "It utilized only glucose and left the xylose unused", "It produced lactic acid", "It needs light"], 1,
  "*S. cerevisiae* (chủng tự nhiên) **chỉ dùng glucose**; 33,2 g/L xylose còn lại.",
  ["Sai.", "", "Sai.", "Sai."], ["xylose"], "S. cerevisiae ferments xylose well", src=ETH)
q("APP-03", "calc", 2, "What is the theoretical maximum yield of ethanol from glucose (MW glucose 180.16, ethanol 46.07)?",
  ["0.256 g/g", "0.511 g/g", "1.000 g/g", "2.000 g/g"], 1,
  "2 × 46,07 / 180,16 = **0,511 g/g**.",
  ["Chỉ tính 1 mol ethanol.", "", "Quên CO₂.", "Nhầm mol với gam."], ["theoretical yield"], "Theoretical yield is 1 g ethanol per g glucose")
q("APP-03", "concept", 2, "In alcoholic fermentation, what is the main role of converting acetaldehyde to ethanol?",
  ["To produce extra ATP", "To regenerate NAD+ so glycolysis can continue", "To fix CO2", "To make pyruvate"], 1,
  "Bước acetaldehyde → ethanol dùng NADH, **tái sinh NAD⁺**; ATP (2 ròng) đến từ đường phân.",
  ["Không tạo ATP.", "", "Sai – tạo CO₂ ở bước trước.", "Sai."], ["NAD+"], "The ethanol step produces extra ATP")
q("APP-03", "recall", 1, "Azolla filiculoides, used as ethanol feedstock, is:",
  ["a brown alga", "a floating aquatic fern living in symbiosis with the nitrogen-fixing cyanobacterium Anabaena azollae", "a yeast", "a cyanobacterium"], 1,
  "*Azolla* là **dương xỉ thủy sinh nổi**, cộng sinh ***Anabaena azollae***.",
  ["Sai.", "", "Sai.", "Anabaena mới là vi khuẩn lam."], ["Azolla"], "Azolla is an alga", src=ETH)
q("APP-03", "recall", 1, "The optimal thermal acid hydrolysis conditions for Azolla in the study were:",
  ["50 mM HCl, 30 °C, 10 min", "14% (w/v) slurry, 200 mM H2SO4, 121 °C, 60 min", "250 mM HNO3, 100 °C, 5 h", "No acid, 37 °C"], 1,
  "14% w/v, **200 mM H₂SO₄**, **121 °C, 60 phút** → 16,7 g/L đường đơn.",
  ["Sai.", "", "Sai.", "Sai."], ["pretreatment"], src=ETH)
q("APP-03", "recall", 1, "Which enzyme preparation was selected for saccharification, producing 61.6 g/L monosaccharides at 16 U/mL?",
  ["Celluclast", "Viscozyme", "Cellic C-Tec2", "Amylase"], 1,
  "**Viscozyme** (cellulase + hemicellulase), 16 U/mL, 48 h.",
  ["Thấp hơn.", "", "Thấp nhất.", "Không dùng."], ["saccharification"], src=ETH)
q("APP-03", "calc", 2, "100 g glucose is supplied; 80 g is consumed and 36 g ethanol is formed. What is the ethanol yield on sugar CONSUMED, and what % of the theoretical maximum (0.511 g/g) is this?",
  ["0.36 g/g; 70%", "0.45 g/g; 88%", "0.45 g/g; 45%", "0.80 g/g; 157%"], 1,
  "36/80 = **0,45 g/g**; 0,45/0,511 = **88%**. (Trên đường ban đầu: 0,36 g/g ≈ 70%.)",
  ["Đó là trên đường ban đầu.", "", "Nhầm % lý thuyết.", "Sai."], ["ethanol yield"])
q("APP-03", "concept", 2, "In the Azolla study, the ethanol yield coefficient Y_EtOH was calculated as:",
  ["max ethanol / sugar consumed", "max ethanol / total initial monosaccharides (glucose + xylose)", "ethanol / biomass", "CO2 / glucose"], 1,
  "Phương trình 3: **[EtOH]max / [đường đơn ban đầu]**.",
  ["Không phải cơ sở của bài.", "", "Sai.", "Sai."], ["ethanol yield"], pool="mock", src=ETH)
q("APP-03", "recall", 1, "The process used in the Azolla study, where saccharification is done first and fermentation afterwards, is called:",
  ["SSF (simultaneous saccharification and fermentation)", "SHF (separate hydrolysis and fermentation)", "Solid-state fermentation", "Continuous culture"], 1,
  "Bài báo dùng **SHF**.",
  ["Đồng thời.", "", "Khác khái niệm.", "Sai."], ["SHF"], pool="mock", src=ETH)
q("APP-03", "not", 2, "Which statement about the Azolla ethanol study is NOT correct?",
  ["Fermentation was semianaerobic at 30 °C", "Ethanol was measured by HPLC", "K. marxianus consumed glucose and xylose completely within 60 h", "S. cerevisiae fermented xylose better than all other yeasts"], 3,
  "*S. cerevisiae* **không dùng xylose**.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["xylose"], pool="mock")
q("APP-03", "calc", 2, "A fermentation starts with 61 g/L total monosaccharides and reaches a maximum of 26.8 g/L ethanol. Y_EtOH on initial sugar is about:",
  ["0.22 g/g", "0.37 g/g", "0.44 g/g", "0.51 g/g"], 2,
  "26,8 / 61 ≈ **0,44 g/g** (bài báo làm tròn 0,43 với 61,6 g/L).",
  ["Sai.", "Sai.", "", "Giới hạn lý thuyết."], ["ethanol yield"], pool="mock")

v("APP-03", "bioethanol", "ethanol sinh học", "Ethanol produced by microbial fermentation of biomass.", "Bioethanol is blended into gasoline.", ["ethanol"])
v("APP-03", "alcoholic fermentation", "lên men rượu", "Conversion of sugar to ethanol and CO2, regenerating NAD+.", "Yeast performs alcoholic fermentation.")
v("APP-03", "NAD+", "NAD⁺", "Electron carrier regenerated when acetaldehyde is reduced to ethanol.", "Fermentation regenerates NAD+.", ["NADH"])
v("APP-03", "theoretical yield", "hiệu suất lý thuyết", "Maximum product per substrate from stoichiometry; 0.511 g/g for ethanol.", "The theoretical yield of ethanol is 0.511 g/g.")
v("APP-03", "ethanol yield", "hiệu suất ethanol", "Ethanol produced per sugar (initial or consumed).", "The ethanol yield was 0.43 g/g.", ["Y_EtOH"])
v("APP-03", "Azolla", "bèo hoa dâu (Azolla)", "Floating aquatic fern with symbiotic Anabaena azollae.", "Azolla filiculoides was hydrolysed for ethanol.", ["Azolla filiculoides"])
v("APP-03", "lignocellulose", "lignocellulose", "Plant material of cellulose, hemicellulose and lignin.", "Lignocellulose needs pretreatment.", ["lignocellulosic"])
v("APP-03", "pretreatment", "tiền xử lý", "Treatment opening biomass structure, e.g., dilute acid at 121 °C.", "Acid pretreatment released sugars.", ["thermal acid hydrolysis"])
v("APP-03", "saccharification", "đường hóa", "Enzymatic hydrolysis of polysaccharides to sugars.", "Viscozyme was used for saccharification.")
v("APP-03", "SHF", "thủy phân và lên men tách riêng", "Separate hydrolysis and fermentation.", "The Azolla study used SHF.", ["SSF"])
v("APP-03", "xylose", "đường xylose", "A five-carbon sugar from hemicellulose.", "S. cerevisiae cannot ferment xylose.", ["pentose"])
v("APP-03", "Kluyveromyces marxianus", "nấm men K. marxianus", "Thermotolerant yeast that ferments glucose and xylose.", "K. marxianus gave the most ethanol.")
v("APP-03", "HPLC", "sắc ký lỏng hiệu năng cao", "High-performance liquid chromatography used to measure sugars and ethanol.", "Ethanol was measured by HPLC.")
v("APP-03", "primary metabolite", "chất chuyển hóa sơ cấp", "Product of central metabolism formed during growth, e.g., ethanol.", "Ethanol is a primary metabolite.", ["primary metabolites"])

fc("APP-03", "number", "Theoretical ethanol yield from glucose?", "0.511 g/g (2 × 46.07 / 180.16).")
fc("APP-03", "fact", "Azolla study pretreatment optimum?", "14% w/v, 200 mM H2SO4, 121 °C, 60 min → 16.7 g/L; Viscozyme 16 U/mL, 48 h → 61.6 g/L (92.2%).")
fc("APP-03", "fact", "Best and worst yeasts on Azolla hydrolysate?", "Best K. marxianus 26.8 g/L (0.43), uses glucose + xylose; worst S. cerevisiae (glucose only).")
fc("APP-03", "fact", "Role of acetaldehyde → ethanol step?", "Regenerates NAD+; no extra ATP.")
fc("APP-03", "trap", "Y_EtOH in the Azolla paper uses which denominator?", "Initial total monosaccharides (glucose + xylose), not sugar consumed.")

we("WE-15", "APP-03", "Ethanol yield on two bases and % of theoretical",
   "A batch starts with 120 g/L glucose. At the end, 20 g/L glucose remains and ethanol is 45 g/L (none at the start). MW glucose 180.16, ethanol 46.07.",
   [S("Theoretical yield (g/g) = 2 × 46.07 / 180.16?", 0.5114, hint="Tính đến 4 chữ số thập phân."),
    S("Glucose consumed (g/L)?", 100),
    S("Yield on glucose consumed (g/g)?", 0.45),
    S("% of theoretical on consumed basis = 0.45/0.5114 × 100?", 88.0),
    S("Yield on initial glucose (g/g) = 45/120?", 0.375),
    S("% of theoretical on initial basis?", 73.3)],
   "Y consumed = 0.45 g/g (88% of theoretical); Y initial = 0.375 g/g (73.3%)",
   "Luôn ghi rõ mẫu số: đường **đã tiêu thụ** hay **ban đầu**. Giới hạn 0,511 g/g < 1 vì một nửa khối lượng carbon đi ra dạng CO₂.")

# ---------------------------------------------------------------- APP-04
unit("APP-04", "Penicillin: structure, biosynthesis, fed-batch fermentation, extraction and uses", "H", 2, 30, PEN,
"""Năm 1943, cả nước Mỹ chỉ có vài chục gram penicillin; một bệnh nhân được cứu nhờ thu hồi thuốc từ **nước tiểu** để dùng lại. Chỉ hai năm sau, nhờ chủng ***Penicillium chrysogenum*** phân lập từ **quả dưa lưới mốc**, dịch ngâm ngô và **lên men chìm có cấp liệu**, sản lượng tăng lên hàng tấn. Penicillin là ví dụ kinh điển của **sản phẩm chuyển hóa thứ cấp**.""",
("Penicillin is classified as a secondary metabolite. When is it mainly produced?",
 ["During rapid exponential growth (trophophase)", "After the main growth phase, when growth slows (idiophase)", "Only after all cells die", "Before inoculation"], 1,
 "Chất chuyển hóa thứ cấp được tạo mạnh ở **idiophase**, khi tăng trưởng chậm lại nhưng tế bào vẫn sống, chuyển hóa."),
[
("1. Cấu trúc penicillin", """
- Nhân của penicillin tự nhiên: **6-aminopenicillanic acid (6-APA)** = **vòng thiazolidine** gắn (ngưng tụ) với **vòng β-lactam** (4 cạnh).
- Các penicillin **khác nhau chủ yếu ở chuỗi bên R**, gắn vào nhân bằng **liên kết amide**.
- *P. notatum* của **Fleming** tạo **penicillin F** (2-pentenyl penicillin); *P. chrysogenum* tạo **penicillin K** khi không có tiền chất.
- **Penicillin G** (benzyl, chuỗi bên từ **phenylacetic acid**) và **penicillin V** (phenoxymethyl, từ **phenoxyacetic acid**) được sản xuất thương mại.
- Nếu lên men **không thêm tiền chất chuỗi bên**: tạo hỗn hợp penicillin tự nhiên, chỉ **benzylpenicillin** tách được.
"""),
("2. Sinh tổng hợp (không qua ribosome)", """
- Ba amino acid **L-α-aminoadipic acid (AAA), L-cysteine, L-valine** → **ACV synthetase** nối thành **tripeptide ACV** (δ-(L-α-aminoadipyl)-L-cysteinyl-D-valine) – **không qua ribosome**.
- **Isopenicillin N synthase** đóng vòng (cần **O₂**) → **isopenicillin N** (có vòng β-lactam + thiazolidine).
- **Acyltransferase** thay chuỗi bên aminoadipyl bằng chuỗi bên từ tiền chất (vd phenylacetyl-CoA) → **penicillin G**.
- Tài liệu ghi \"cystine\" – đúng là **L-cysteine** (hình minh họa). [hiệu chỉnh]
"""),
("3. Sinh tổng hợp định hướng vs bán tổng hợp", """
| Khái niệm | Cách làm | Ví dụ |
|---|---|---|
| **Định hướng sinh tổng hợp (precursor feeding)** | thêm **tiền chất chuỗi bên** vào môi trường lên men | **phenylacetic acid → penicillin G** (thay vì penicillin K); phenoxyacetic acid → penicillin V |
| **Bán tổng hợp (semi-synthetic)** | lấy penicillin lên men → **penicillin acylase** (thường từ *E. coli*, **cố định trên cột**) cắt chuỗi bên → **6-APA** → gắn chuỗi bên mới bằng hóa học | ampicillin, amoxicillin, methicillin |

- Penicillin bán tổng hợp cải thiện: **bền acid**, **kháng β-lactamase** (mã hóa trên plasmid hoặc NST), **phổ kháng khuẩn rộng hơn**.
- Tài liệu gọi cả penicillin nhờ tiền chất là \"semi-synthetic\"; chính xác hơn phân biệt như bảng.
"""),
("4. Cơ chế tác dụng và penicillinase", """
- Penicillin gắn **PBP (penicillin-binding proteins) / transpeptidase** → ức chế **tạo liên kết chéo peptidoglycan** → thành tế bào yếu → **ly giải** khi vi khuẩn đang sinh trưởng (liên hệ BAC-03).
- Hoạt tính chủ yếu trên **vi khuẩn Gram dương**; người không có peptidoglycan → độc tính chọn lọc; không có tác dụng với virus.
- **Penicillinase (β-lactamase)**: **thủy phân vòng β-lactam** → **penicilloic acid** mất hoạt tính (tài liệu ghi nhầm \"carboxylated\"). Vi sinh vật tạo penicillinase phân bố rộng → **nhiễm tạp là trở ngại chính** trong lên men penicillin.
"""),
("5. Chủng, giống và bảo quản", """
- Chủng năng suất cao phát triển từ ***P. chrysogenum*** hoang dại bằng **chọn lọc di truyền tuần tự** (đột biến UV, X-ray, nitrogen mustard...). *P. chrysogenum* **tốt hơn *P. notatum*** và **phù hợp lên men chìm**. (Chủng công nghiệp nay được xác định là *P. rubens*.)
- Chủng năng suất cao **không ổn định di truyền** – năng suất càng cao càng kém ổn định → bảo quản: **huyền phù bào tử đông lạnh trong nitơ lỏng**; **đông khô**; **trộn đất/cát vô trùng rồi làm khô**.
- **Nhân giống (inoculum)**: bào tử huyền phù trong nước hoặc **sodium lauryl sulfate 1:10.000** (chất thấm ướt vì bào tử **kỵ nước**) → bình → thùng giống; **24–27 °C, 2 ngày**, khuấy + sục khí để hệ sợi phát triển mạnh.
"""),
("6. Lên men sản xuất", """
- **Hiếu khí**; sục khí **0,5–1,0 vvm**; **lên men chìm fed-batch trong bồn khuấy (stirred tank)**; **25–27 °C**; bồn **40.000–200.000 L** (lớn hơn khó cấp O₂).
- **Môi trường**: phải cho (1) hệ sợi phát triển mạnh, (2) tích lũy kháng sinh tối đa, (3) chiết tách dễ, rẻ.
  - Nguồn C: **lactose** (dùng chậm – tránh kìm hãm do glucose); glucose, sucrose, glycerol, sorbitol cũng dùng được (cấp từ từ).
  - Nguồn N: amoni sulfate/acetate/nitrate; **corn steep liquor (dịch ngâm ngô)** – giàu amino acid, khoáng → hệ sợi và bào tử phát triển mạnh.
  - Khoáng: K, P (KH₂PO₄), Mg, Fe, Cu (sulfate), S, Zn.
  - **Tiền chất** phenylacetic acid (cấp dần vì độc ở nồng độ cao).
- **Động học**: **pha sinh trưởng ~10 h**, **thời gian nhân đôi 6 h** → phần lớn sinh khối; O₂ quan trọng vì **độ nhớt tăng cản truyền O₂**. Sau đó **pha sản xuất** – tăng trưởng bị hạn chế bằng **cấp liệu** → penicillin tăng **tuyến tính từ ~48 đến 96 h**; pha sản xuất kéo dài **120–180 h**.
- Năng suất cuối **3–5%** (so với carbohydrate tiêu thụ) ≈ **1500 IU/mL**.
- Lên men **liên tục khó** do chủng không ổn định → hệ **\"batch fill and draw\"**: rút **20–40%** dịch, thay môi trường mới, lặp **đến 10 lần**.

| Pha | Trophophase | Idiophase |
|---|---|---|
| Hoạt động chính | sinh trưởng hệ sợi | tạo penicillin |
| Cấp liệu | dư dinh dưỡng | **cấp hạn chế** (fed-batch) |
| O₂ | cần nhiều | vẫn cần (hô hấp + bước đóng vòng) |
"""),
("7. Chiết tách và tinh sạch", """
1. **Loại hệ sợi** (lọc chân không quay); penicillin **tiết ra môi trường**, **< 1%** gắn hệ sợi.
2. **Acid hóa dịch đến pH 2,0–2,5** (H₃PO₄ hoặc H₂SO₄) → penicillin ở **dạng acid không ion hóa** (tài liệu ghi \"anionic\" là sai) → **chiết ngay** vào **dung môi hữu cơ**: **amyl acetate, butyl acetate, methyl isobutyl ketone**; làm **nhanh** vì penicillin **kém bền ở pH thấp**; thiết bị **Podbielniak counter-current extractor** (chiết ngược dòng).
3. **Chiết ngược vào nước** bằng KOH/NaOH, **pH 7,0–7,5** (dạng muối ion hóa tan trong nước).
4. Lặp acid hóa – chiết để tinh sạch; thu **sodium penicillin**; dung môi thu hồi bằng **chưng cất**.
5. **Xử lý dịch thô**: **than hoạt tính** loại **pyrogen** (chất gây sốt); **lọc Seitz** loại vi khuẩn; **kết tinh** → bột trong lọ vô trùng, viên nén, siro.

> **Thu hồi chung = tích các hệ số thu hồi từng bước** (vd 0,90 × 0,80 × 0,95 = 68,4%).
"""),
("8. Ứng dụng", """
- Chủ yếu diệt **vi khuẩn Gram dương** (ức chế tổng hợp thành) – điều trị nhiễm khuẩn ở người (liên cầu, phế cầu, giang mai…).
- Penicillin cấp dược dùng làm nguyên liệu sản xuất **penicillin bán tổng hợp**.
"""),
],
[
("Kháng kháng sinh", """
Vi khuẩn tiết **β-lactamase** (vd *Staphylococcus aureus*), thay đổi PBP (**MRSA** – PBP2a), giảm porin (Gram âm). Giải pháp: phối hợp **chất ức chế β-lactamase** (amoxicillin + **clavulanic acid** = Augmentin), dùng kháng sinh hợp lý. Việt Nam nằm trong nhóm nước có tỉ lệ kháng kháng sinh cao – liên hệ HIS-04 (Fleming đã cảnh báo từ 1945).
"""),
],
[
("Structure and biosynthesis", "Natural penicillin nucleus **6-APA** = **thiazolidine ring fused to a β-lactam ring**; penicillins differ in the **R side chain** (amide link). Non-ribosomal: **L-α-aminoadipate + L-cysteine + L-valine → ACV tripeptide → isopenicillin N (O₂-dependent) → penicillin G** via acyltransferase. *P. notatum* → penicillin F; *P. chrysogenum* → penicillin K without precursor, **penicillin G with phenylacetic acid**.", "6-APA; tiền chất phenylacetic."),
("Fermentation", "**Aerobic, fed-batch submerged** fermentation in stirred tanks (40,000–200,000 L), **0.5–1.0 vvm**, **25–27 °C**. Medium: **lactose**, ammonium salts, **corn steep liquor**, minerals, precursor. Growth ~10 h (doubling 6 h); production phase 120–180 h (linear 48–96 h); yield 3–5% (~1500 IU/mL). High-yield strains are genetically unstable (store in liquid N₂, lyophilized, or on soil/sand). **Penicillinase** contamination is the main constraint.", "Fed-batch, lactose, CSL."),
("Recovery", "Remove mycelium (penicillin excreted; <1% bound). Acidify to **pH 2.0–2.5**, extract quickly into **amyl/butyl acetate or MIBK** (Podbielniak counter-current), back-extract into water at **pH 7.0–7.5** with KOH/NaOH; repeat; **sodium penicillin**; **charcoal removes pyrogens**, Seitz filtration, crystallization. **Penicillin acylase** (immobilized, *E. coli*) removes side chains → 6-APA → **semi-synthetic** penicillins (acid-stable, β-lactamase-resistant, broader spectrum).", "Chiết pH 2–2,5 rồi pH 7–7,5."),
],
["6-APA is the complete penicillin G molecule", "Penicillinase removes the side chain to give 6-APA", "Penicillin production is anaerobic", "Penicillin is extracted into solvent at pH 7.5"])

q("APP-04", "recall", 1, "The nucleus of natural penicillin (6-APA) consists of:",
  ["a thiazolidine ring fused to a β-lactam ring", "two β-lactam rings", "a benzene ring and a lactone", "a peptidoglycan fragment"], 0,
  "**6-APA** = vòng **thiazolidine** ngưng tụ với vòng **β-lactam**.",
  ["", "Sai.", "Sai.", "Sai."], ["6-APA", "beta-lactam ring"], src=PEN)
q("APP-04", "recall", 1, "Adding phenylacetic acid to a P. chrysogenum fermentation causes the fungus to produce:",
  ["penicillin K", "penicillin F", "penicillin G", "penicillin V"], 2,
  "Tiền chất **phenylacetic acid → penicillin G** (thay vì penicillin K). Phenoxyacetic → penicillin V.",
  ["Không có tiền chất.", "P. notatum.", "", "Phenoxyacetic acid."], ["precursor"], src=PEN)
q("APP-04", "recall", 1, "Industrial penicillin is produced by:",
  ["anaerobic batch fermentation in bottles", "aerobic fed-batch submerged fermentation in stirred tank fermenters", "solid-state fermentation on bran", "continuous chemostat culture"], 1,
  "**Hiếu khí, fed-batch, lên men chìm, bồn khuấy**.",
  ["Lịch sử, dễ nhiễm.", "", "Sai.", "Khó do chủng không ổn định."], ["fed-batch"], "Penicillin production is anaerobic", src=PEN)
q("APP-04", "concept", 2, "During penicillin recovery, the filtered broth is acidified to pH 2.0–2.5 and extracted quickly into butyl acetate. Why quickly?",
  ["Butyl acetate evaporates", "Penicillin is quite unstable at low pH", "The mycelium regrows", "Penicillin becomes insoluble in solvents"], 1,
  "Penicillin **kém bền ở pH thấp** → chiết ngay (Podbielniak ngược dòng).",
  ["Không phải lý do chính.", "", "Đã loại hệ sợi.", "Ngược: acid hóa giúp tan vào dung môi."], ["extraction"], "Penicillin is extracted into solvent at pH 7.5", src=PEN)
q("APP-04", "concept", 2, "Why is contamination such a serious problem in penicillin fermentation?",
  ["Contaminants produce too much penicillin", "Many microorganisms produce penicillinase (β-lactamase) that destroys penicillin", "Contaminants lower the temperature", "Penicillin kills the fungus"], 1,
  "**Penicillinase** thủy phân vòng β-lactam → mất hoạt tính; vi sinh vật có enzyme này phân bố rộng.",
  ["Sai.", "", "Sai.", "Sai."], ["penicillinase"], src=PEN)
q("APP-04", "recall", 1, "Which carbon source is traditionally used in penicillin production media?",
  ["Lactose", "Methanol", "Cellulose", "Starch-free paraffin"], 0,
  "**Lactose** (dùng chậm); glucose, sucrose, glycerol, sorbitol cũng có thể dùng.",
  ["", "Sai.", "Sai.", "Sai."], ["lactose"], src=PEN)
q("APP-04", "concept", 2, "What is the role of corn steep liquor in penicillin media?",
  ["It is the side-chain precursor only", "It supplies amino acids and minerals that support abundant mycelium and spore formation", "It inhibits contamination", "It lowers pH for extraction"], 1,
  "Dịch ngâm ngô chứa **amino acid** cần cho hệ sợi và **khoáng** (K, P, Mg, S, Zn, Cu).",
  ["Không chỉ vậy.", "", "Sai.", "Sai."], ["corn steep liquor"], src=PEN)
q("APP-04", "concept", 2, "How are semi-synthetic penicillins made?",
  ["By adding more lactose", "Penicillin acylase removes the natural acyl side chain to give 6-APA, to which new acyl groups are attached", "β-lactamase opens the β-lactam ring", "By UV mutation of the fungus"], 1,
  "**Penicillin acylase** (cố định, từ *E. coli*) cắt chuỗi bên → **6-APA** → gắn chuỗi bên mới.",
  ["Sai.", "", "β-lactamase làm mất hoạt tính.", "Đó là cải tiến chủng."], ["penicillin acylase", "semi-synthetic penicillin"], "Penicillinase removes the side chain to give 6-APA", src=PEN)
q("APP-04", "recall", 1, "The biosynthesis of penicillin starts from which three amino acids?",
  ["Glycine, alanine, serine", "L-α-aminoadipic acid, L-cysteine, L-valine", "Lysine, arginine, histidine", "Phenylalanine, tyrosine, tryptophan"], 1,
  "**AAA + cysteine + valine → ACV** (không qua ribosome).",
  ["Sai.", "", "Sai.", "Sai."], ["ACV tripeptide"])
q("APP-04", "recall", 1, "Charcoal treatment of crude sodium penicillin is used to remove:",
  ["water", "pyrogens (fever-causing substances)", "the β-lactam ring", "sodium ions"], 1,
  "Than hoạt tính loại **pyrogen**; lọc Seitz loại vi khuẩn.",
  ["Sai.", "", "Sẽ mất hoạt tính.", "Sai."], ["pyrogen"], src=PEN)
q("APP-04", "calc", 2, "Three sequential recovery steps retain 90%, 80% and 95% of the penicillin entering each step. What is the overall recovery?",
  ["88.3%", "68.4%", "80.0%", "265%"], 1,
  "0,90 × 0,80 × 0,95 = **0,684 = 68,4%** (nhân, không lấy trung bình).",
  ["Lấy trung bình – sai.", "", "Sai.", "Cộng – sai."], ["recovery"])
q("APP-04", "recall", 1, "High-yielding P. chrysogenum strains are genetically unstable. Which is a preservation method mentioned?",
  ["Storing spores at room temperature in broth", "Spore suspension frozen under liquid nitrogen", "Autoclaving the spores", "Storing mycelium in 70% ethanol"], 1,
  "Nitơ lỏng; đông khô; trộn đất/cát vô trùng rồi làm khô.",
  ["Sai.", "", "Diệt bào tử.", "Diệt."], ["strain preservation"], pool="mock")
q("APP-04", "not", 2, "Which statement about penicillin fermentation is NOT correct according to the reference?",
  ["It is aerobic with 0.5–1.0 vvm aeration", "Temperature is maintained around 25–27 °C", "Fermenters of 40,000–200,000 L are used", "Continuous fermentation is standard because strains are very stable"], 3,
  "Lên men liên tục **khó** vì chủng **không ổn định**; thay bằng batch fill and draw.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["fed-batch"], pool="mock")
q("APP-04", "concept", 2, "After extraction into organic solvent, penicillin is back-extracted into water by:",
  ["lowering pH to 1", "adding KOH or NaOH to raise pH to 7.0–7.5", "heating to 121 °C", "adding more butyl acetate"], 1,
  "Nâng **pH 7,0–7,5** → muối penicillin ion hóa tan vào nước.",
  ["Sai.", "", "Phá penicillin.", "Sai."], ["extraction"], pool="mock")
q("APP-04", "not", 2, "Which is NOT an improvement of semi-synthetic penicillins over natural ones mentioned in the reference?",
  ["Acid stability", "Resistance to β-lactamases", "Expanded antimicrobial effectiveness", "Activity against viruses"], 3,
  "Penicillin không có tác dụng với virus.",
  ["Có.", "Có.", "Có.", ""], ["semi-synthetic penicillin"], pool="mock")
q("APP-04", "calc", 2, "In a fed-batch, penicillin is 10 g/L in 1 L at t0 and 8 g/L in 2 L later. How much penicillin (g) is in the fermenter at each time?",
  ["10 g then 8 g (decreased)", "10 g then 16 g (increased)", "10 g then 4 g", "20 g then 16 g"], 1,
  "m = C × V: 10 × 1 = 10 g; 8 × 2 = **16 g** – tổng lượng **tăng** dù nồng độ giảm do pha loãng.",
  ["Nhầm nồng độ với khối lượng.", "", "Sai.", "Sai."], ["fed-batch"], pool="mock")

v("APP-04", "penicillin", "penicillin", "β-lactam antibiotic from Penicillium that inhibits cell-wall cross-linking.", "Penicillin kills Gram-positive bacteria.", ["penicillins", "penicillin G", "penicillin V"])
v("APP-04", "6-APA", "acid 6-aminopenicillanic (6-APA)", "Penicillin nucleus of fused thiazolidine and β-lactam rings.", "Acylase converts penicillin G into 6-APA.", ["6-aminopenicillanic acid"])
v("APP-04", "beta-lactam ring", "vòng β-lactam", "Four-membered cyclic amide essential for penicillin activity.", "β-lactamase opens the beta-lactam ring.", ["β-lactam", "thiazolidine"])
v("APP-04", "secondary metabolite", "chất chuyển hóa thứ cấp", "Specialized product formed mainly after active growth (idiophase).", "Penicillin is a secondary metabolite.", ["secondary metabolites"])
v("APP-04", "idiophase", "pha sản xuất (idiophase)", "Phase in which secondary metabolites are produced.", "Penicillin accumulates in the idiophase.", ["trophophase"])
v("APP-04", "Penicillium chrysogenum", "nấm Penicillium chrysogenum", "Industrial penicillin-producing mold suited to submerged culture.", "P. chrysogenum replaced P. notatum.", ["P. chrysogenum", "Penicillium notatum"])
v("APP-04", "precursor", "tiền chất", "A compound supplied to direct biosynthesis, e.g., phenylacetic acid.", "Phenylacetic acid is the precursor of penicillin G.", ["phenylacetic acid"])
v("APP-04", "ACV tripeptide", "tripeptide ACV", "δ-(L-α-aminoadipyl)-L-cysteinyl-D-valine made non-ribosomally.", "ACV is cyclized to isopenicillin N.", ["isopenicillin N"])
v("APP-04", "fed-batch", "nuôi cấy mẻ có bổ sung (fed-batch)", "Batch culture with controlled feeding of nutrients.", "Penicillin is made by fed-batch fermentation.")
v("APP-04", "corn steep liquor", "dịch ngâm ngô", "Nutrient-rich by-product of corn wet milling.", "Corn steep liquor boosts mycelial growth.")
v("APP-04", "penicillinase", "penicillinase (β-lactamase)", "Enzyme hydrolysing the β-lactam ring.", "Contaminants making penicillinase ruin batches.", ["beta-lactamase", "β-lactamase"])
v("APP-04", "penicillin acylase", "penicillin acylase", "Enzyme removing the side chain of penicillin to yield 6-APA.", "Immobilized penicillin acylase produces 6-APA.")
v("APP-04", "semi-synthetic penicillin", "penicillin bán tổng hợp", "Penicillin with a new side chain attached to 6-APA.", "Ampicillin is a semi-synthetic penicillin.", ["semi-synthetic penicillins"])
v("APP-04", "extraction", "chiết tách", "Transfer of a solute between immiscible phases.", "Penicillin extraction uses butyl acetate.", ["counter-current extraction", "back-extraction"])
v("APP-04", "pyrogen", "chất gây sốt (pyrogen)", "Fever-causing substance removed by charcoal.", "Charcoal removes pyrogens.", ["pyrogens"])
v("APP-04", "recovery", "hiệu suất thu hồi", "Fraction of product retained through processing steps.", "Overall recovery is the product of step recoveries.")
v("APP-04", "strain preservation", "bảo quản chủng", "Keeping production strains stable, e.g., in liquid nitrogen.", "Strain preservation limits instability.")

fc("APP-04", "fact", "Penicillin nucleus?", "6-APA: thiazolidine ring fused to β-lactam ring; R side chain via amide.")
fc("APP-04", "fact", "Precursors and products?", "No precursor: penicillin K (P. chrysogenum), F (P. notatum). Phenylacetic acid → G; phenoxyacetic → V.")
fc("APP-04", "number", "Penicillin fermentation conditions?", "Aerobic fed-batch, 0.5–1.0 vvm, 25–27 °C, 40,000–200,000 L; growth 10 h (doubling 6 h); production 120–180 h; yield 3–5% ≈ 1500 IU/mL.")
fc("APP-04", "fact", "Penicillin extraction pH steps?", "Acidify to pH 2.0–2.5 → extract into amyl/butyl acetate or MIBK (fast) → back-extract into water at pH 7.0–7.5 → repeat → sodium penicillin → charcoal (pyrogens), Seitz filter, crystallize.")
fc("APP-04", "trap", "Penicillin acylase vs penicillinase?", "Acylase removes side chain → 6-APA (useful). Penicillinase/β-lactamase opens β-lactam ring → inactive.")
fc("APP-04", "fact", "Preserving unstable high-yield strains?", "Spores in liquid N2; lyophilized; mixed with sterile soil/sand and desiccated.")

we("WE-16", "APP-04", "Fed-batch mass balance and overall recovery",
   "A fed-batch penicillin fermenter holds 50,000 L at 4 g/L at 96 h. Feeding raises the volume to 60,000 L and the titre to 6 g/L at 160 h. Recovery then runs: filtration 95%, solvent extraction 85%, back-extraction 90%, crystallization 92%.",
   [S("Penicillin at 96 h (kg) = 4 g/L × 50,000 L ÷ 1000?", 200),
    S("Penicillin at 160 h (kg)?", 360),
    S("Net increase (kg)?", 160),
    S("Overall recovery (fraction) = 0.95 × 0.85 × 0.90 × 0.92?", 0.6686, hint="Nhân các hệ số, làm tròn 4 chữ số."),
    S("Crystalline penicillin obtained (kg) from 360 kg?", 240.7)],
   "360 kg in broth; overall recovery ≈ 66.9%; ≈ 241 kg product",
   "Khi thể tích thay đổi, dùng khối lượng m = C × V chứ không so nồng độ. Thu hồi chung là **tích** các bước: 0,95 × 0,85 × 0,90 × 0,92 ≈ 0,669 → 360 × 0,669 ≈ 240,7 kg.")
