from _lib import *

SRC = "9-10.Protists.pptx"

# ---------------------------------------------------------------- PRO-01
unit("PRO-01", "Protist overview: supergroups, nutrition, reproduction; fungi vs algae vs protozoa", "H", 1, 20, SRC + ": slides 1–12, 102",
"""Một giọt nước ao dưới kính hiển vi chứa cả *Euglena* xanh bơi bằng roi, *Paramecium* phủ lông bơi, tảo silic vỏ thủy tinh và amip bò bằng chân giả. Tất cả được gọi chung là **nguyên sinh vật (protists)** – nhóm "thập cẩm" của sinh vật **nhân thực** không phải động vật, thực vật hay nấm. Làm sao sắp xếp thế giới hỗn độn này?""",
("Which statement about protists is correct?",
 ["They are all prokaryotes", "They are eukaryotes that are not animals, plants or fungi, and they show very diverse nutrition", "They are all photosynthetic", "They are all parasites"], 1,
 "Protists là **nhân thực** rất đa dạng: có loài **quang tự dưỡng**, **dị dưỡng**, và **dinh dưỡng hỗn hợp (mixotroph)**."),
[
("1. Protists là gì?", """
- **Protists** (nguyên sinh vật): nhóm **sinh vật nhân thực** rất đa dạng, **phần lớn đơn bào**, một số tập đoàn hoặc đa bào (tảo nâu khổng lồ).
- Không phải một nhánh tiến hóa duy nhất – là cách gọi "tiện dụng" cho nhân thực **không phải** động vật, thực vật, nấm.
- Theo slide 24 (bài HIS-01): protists gồm **protozoa, algae, oomycetes, slime molds**.
"""),
("2. Bốn siêu nhóm (slide 4–8)", """
| Siêu nhóm | Các nhóm trong bài |
|---|---|
| **Excavata** | **diplomonads** (*Giardia*), **parabasalids** (*Trichomonas*), **euglenozoans** (kinetoplastids *Trypanosoma*; euglenids *Euglena*), Percolozoa (*Naegleria*) |
| **SAR** (Stramenopiles – Alveolates – Rhizaria) | Stramenopiles: **diatoms, brown algae, oomycetes**; Alveolates: **dinoflagellates, apicomplexans, ciliates**; Rhizaria: **foraminiferans** |
| **Archaeplastida** | **red algae, green algae** (chlorophytes, charophytes) (+ thực vật trên cạn) |
| **Unikonta** | **slime molds** (nấm nhầy) (+ động vật, nấm) |

Mẹo nhớ: **E-S-A-U** = Excavata, SAR, Archaeplastida, Unikonta.
"""),
("3. Dinh dưỡng đa dạng (slide 9)", """
| Kiểu | Mô tả | Ví dụ |
|---|---|---|
| **Photoautotrophs** (quang tự dưỡng) | có **lục lạp**, quang hợp | tảo silic, tảo nâu, tảo đỏ, tảo lục |
| **Heterotrophs** (dị dưỡng) | hấp thụ chất hữu cơ hoặc **ăn (thực bào)** các hạt thức ăn | *Giardia, Trypanosoma, Paramecium*, oomycetes |
| **Mixotrophs** (dinh dưỡng hỗn hợp) | **vừa quang hợp vừa dị dưỡng** | *Euglena*, nhiều dinoflagellates |
"""),
("4. Sinh sản đa dạng (slide 10–11)", """
- **Vô tính (asexual)**: phân đôi (dọc ở *Euglena*, *Trichomonas*), phân nhiều (schizogony ở *Plasmodium*), nảy chồi, bào tử.
- **Hữu tính (sexual)**: qua **thụ tinh (fertilization)** và **giảm phân (meiosis)**; có nhiều kiểu vòng đời [fig]:
  - vòng đời **đơn bội trội** (hợp tử là giai đoạn 2n duy nhất – *Chlamydomonas*);
  - **luân phiên thế hệ** giữa thể bào tử 2n và thể giao tử n (tảo nâu *Laminaria*, *Ulva*);
  - **lưỡng bội trội** (oomycetes, tảo silic).
- Quy tắc đọc vòng đời: **thụ tinh: n + n → 2n**; **giảm phân: 2n → n**; **nguyên phân giữ nguyên** mức bội.
"""),
("5. Phân biệt nấm – tảo – động vật nguyên sinh (slide 102)", """
| Đặc điểm | **Fungi** (nấm) | **Algae** (tảo) | **Protozoa** (ĐV nguyên sinh) |
|---|---|---|---|
| Giới | Fungi | **Protist** | **Protist** |
| Kiểu dinh dưỡng | **hóa dị dưỡng** | **quang tự dưỡng** | **hóa dị dưỡng** |
| Đa bào | **tất cả, trừ nấm men** | **một số** | **không** |
| Sắp xếp tế bào | đơn bào; sợi; thể quả (nấm lớn) | đơn bào; tập đoàn; sợi; mô | **đơn bào** |
| Cách lấy dinh dưỡng | **hấp thụ** | hấp thụ | **hấp thụ; tiêu hóa (qua miệng tế bào)** |
| Đặc điểm khác | **bào tử** vô tính và hữu tính | **sắc tố** | **di động**; một số tạo **nang (cyst)** |
"""),
],
[
("Protists quanh ta", """
- **Tảo** tạo ra khoảng một nửa lượng O₂ trên Trái Đất và là nền tảng chuỗi thức ăn biển.
- Ký sinh trùng nguyên sinh gây bệnh lớn: **sốt rét** (*Plasmodium*), **lỵ amip** (*Entamoeba*), **tiêu chảy** (*Giardia*), **bệnh ngủ** (*Trypanosoma*).
- Công nghiệp: **agar** (tảo đỏ), **alginate** (tảo nâu – làm đặc kem, thuốc), **bột tảo Spirulina** (thực ra là vi khuẩn lam), đất tảo cát (diatomaceous earth) lọc bia.
"""),
],
[
("What protists are", "**Protists** are diverse, mostly unicellular **eukaryotes** that are not animals, plants or fungi; they include protozoa, algae, oomycetes and slime molds and do not form a single evolutionary clade.", "Nhân thực, không phải ĐV/TV/nấm."),
("Supergroups", "**Excavata** (diplomonads, parabasalids, euglenozoans), **SAR** (stramenopiles: diatoms, brown algae, oomycetes; alveolates: dinoflagellates, apicomplexans, ciliates; rhizarians: forams), **Archaeplastida** (red and green algae), **Unikonta** (slime molds).", "E-S-A-U."),
("Nutrition and reproduction", "Protists are **photoautotrophs**, **heterotrophs** or **mixotrophs**. They reproduce **asexually** and **sexually** (fertilization + meiosis) with various life cycles.", "Quang tự dưỡng, dị dưỡng, hỗn hợp."),
("Fungi vs algae vs protozoa", "Fungi: chemoheterotrophs, multicellular except yeasts, absorb nutrients, asexual/sexual spores. Algae: photoautotrophs, some multicellular, pigments. Protozoa: chemoheterotrophs, unicellular, absorb or ingest through a mouth, motile, some form cysts.", "Bảng so sánh slide cuối."),
],
["Protists are prokaryotes", "All algae are multicellular", "Protozoa are photoautotrophs"])

q("PRO-01", "recall", 1, "The four supergroups used in the lecture to classify protists are:",
  ["Bacteria, Archaea, Eukarya, Viruses", "Excavata, SAR, Archaeplastida, Unikonta", "Zygomycota, Ascomycota, Basidiomycota, Oomycota", "Algae, Fungi, Protozoa, Plants"], 1,
  "Slide 4–8: **Excavata, SAR, Archaeplastida, Unikonta**.",
  ["Ba miền sự sống + virus.", "", "Các ngành nấm.", "Không đúng."], ["Excavata", "SAR"], src=SRC + " slides 4–8")
q("PRO-01", "recall", 1, "Protists that can both photosynthesize and feed on organic matter are called:",
  ["photoautotrophs", "mixotrophs", "chemoautotrophs", "obligate heterotrophs"], 1,
  "Slide 9: **mixotrophs** – kết hợp quang hợp và dị dưỡng (vd *Euglena*).",
  ["Chỉ quang hợp.", "", "Dùng hóa chất vô cơ.", "Chỉ dị dưỡng."], ["mixotroph"], src=SRC + " slide 9")
q("PRO-01", "not", 2, "According to the comparison table, which feature is NOT typical of protozoa?",
  ["Chemoheterotrophic nutrition", "Unicellular organization", "Photosynthetic pigments", "Motility; some form cysts"], 2,
  "Slide 102: **sắc tố** là đặc điểm của **tảo**. Protozoa: hóa dị dưỡng, đơn bào, di động, một số tạo nang.",
  ["Đúng với protozoa.", "Đúng.", "", "Đúng."], ["protozoa"], "Protozoa are photoautotrophs", src=SRC + " slide 102")
q("PRO-01", "concept", 2, "How do protozoa differ from fungi in obtaining nutrients, according to the lecture table?",
  ["Protozoa photosynthesize", "Protozoa may absorb nutrients or ingest food through a mouth-like structure, while fungi only absorb", "Fungi ingest food through a mouth", "There is no difference"], 1,
  "Slide 102: protozoa **hấp thụ hoặc tiêu hóa qua miệng tế bào**; nấm **chỉ hấp thụ**.",
  ["Sai.", "", "Ngược.", "Có khác."], ["protozoa"])
q("PRO-01", "concept", 2, "In a protist life cycle diagram, which event changes a diploid (2n) nucleus into haploid (n) nuclei?",
  ["Fertilization", "Mitosis", "Meiosis", "Binary fission"], 2,
  "**Giảm phân (meiosis)**: 2n → n. Thụ tinh: n + n → 2n; nguyên phân giữ nguyên mức bội.",
  ["Tăng lên 2n.", "Giữ nguyên.", "", "Giữ nguyên."], ["meiosis"])
q("PRO-01", "recall", 1, "According to the lecture table, which group is multicellular in all members except yeasts?",
  ["Algae", "Protozoa", "Fungi", "Bacteria"], 2,
  "Slide 102: **Fungi – đa bào, trừ nấm men**. Algae: một số; protozoa: không.",
  ["Chỉ một số.", "Không đa bào.", "", "Không trong bảng."], ["fungi"], pool="mock")
q("PRO-01", "recall", 1, "Diatoms, brown algae and oomycetes belong to which supergroup?",
  ["Excavata", "SAR (Stramenopiles)", "Archaeplastida", "Unikonta"], 1,
  "Chúng thuộc **Stramenopiles** trong **SAR**.",
  ["Diplomonads, parabasalids, euglenozoans.", "", "Tảo đỏ, tảo lục.", "Nấm nhầy."], ["SAR"], pool="mock")
q("PRO-01", "not", 2, "Which is NOT a feature of algae in the lecture comparison table?",
  ["Photoautotrophic nutrition", "Some are multicellular", "Contain pigments", "Always unicellular and motile with cysts"], 3,
  "Đơn bào, di động, tạo nang là đặc điểm của **protozoa**.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["algae"], pool="mock")

v("PRO-01", "protist", "nguyên sinh vật", "A eukaryote that is not an animal, plant or fungus.", "Euglena is a protist.", ["protists"])
v("PRO-01", "protozoa", "động vật nguyên sinh", "Unicellular, chemoheterotrophic, usually motile protists.", "Paramecium belongs to the protozoa.", ["protozoan"])
v("PRO-01", "algae", "tảo", "Photoautotrophic protists with pigments; some multicellular.", "Diatoms are algae.", ["alga"])
v("PRO-01", "Excavata", "siêu nhóm Excavata", "Protist supergroup with diplomonads, parabasalids and euglenozoans.", "Giardia belongs to the Excavata.")
v("PRO-01", "SAR", "siêu nhóm SAR", "Stramenopiles, Alveolates and Rhizaria.", "Diatoms are in the SAR supergroup.", ["Stramenopiles", "Alveolates", "Rhizaria"])
v("PRO-01", "Archaeplastida", "siêu nhóm Archaeplastida", "Red algae, green algae and land plants.", "Red algae belong to Archaeplastida.")
v("PRO-01", "Unikonta", "siêu nhóm Unikonta", "Supergroup including slime molds, animals and fungi.", "Slime molds are unikonts.")
v("PRO-01", "mixotroph", "sinh vật dinh dưỡng hỗn hợp", "An organism that both photosynthesizes and feeds heterotrophically.", "Euglena is a mixotroph.", ["mixotrophs", "mixotrophic"])
v("PRO-01", "cyst", "nang (bào nang)", "A protective resting stage of some protozoa.", "Giardia survives outside the host as a cyst.", ["cysts"])

fc("PRO-01", "fact", "Four protist supergroups?", "Excavata, SAR, Archaeplastida, Unikonta.")
fc("PRO-01", "fact", "Three nutritional forms of protists?", "Photoautotrophs, heterotrophs, mixotrophs.")
fc("PRO-01", "fact", "Fungi vs algae vs protozoa nutrition?", "Fungi: chemoheterotroph (absorb). Algae: photoautotroph. Protozoa: chemoheterotroph (absorb or ingest).")
fc("PRO-01", "trap", "TRUE/FALSE: all algae are multicellular.", "FALSE – only some.")

# ---------------------------------------------------------------- PRO-02
unit("PRO-02", "Excavata: diplomonads, parabasalids and euglenozoans", "H", 2, 25, SRC + ": slides 13–33",
"""Du khách uống nước suối "trong vắt" ở vùng núi rồi bị tiêu chảy kéo dài, phân mỡ, đầy hơi – thủ phạm là *Giardia*, một sinh vật nhân thực **không có ty thể hoạt động bình thường**. Cùng siêu nhóm Excavata còn có *Trypanosoma* gây **bệnh ngủ** châu Phi và *Euglena* xanh lá vừa quang hợp vừa ăn. Họ hàng nhưng lối sống khác nhau hoàn toàn.""",
("Giardia lives in the oxygen-poor intestine. What is unusual about its mitochondria?",
 ["It has very large mitochondria", "It has reduced mitochondria (mitosomes) without a functional electron transport chain", "It has chloroplasts instead", "It has hydrogenosomes that release H2"], 1,
 "Slide 14: diplomonads có **mitosome** – ty thể tiêu giảm, **không có chuỗi truyền electron** hoạt động → lấy năng lượng bằng con đường **kỵ khí**."),
[
("1. Diplomonads – Giardia (slide 14–16)", """
- Có **ty thể tiêu giảm gọi là mitosomes**: **không có chuỗi truyền electron hoạt động** → **không dùng O₂** để khai thác năng lượng từ carbohydrate; năng lượng lấy từ **con đường sinh hóa kỵ khí**.
- Nhiều loài **ký sinh**, nổi tiếng là ***Giardia intestinalis*** (*G. lamblia*) sống trong **ruột động vật có vú**.
- Có **hai nhân bằng nhau** và **nhiều roi** (trông như "khuôn mặt").
- Vòng đời [fig]: **nang (cyst)** theo nước/thức ăn vào ruột → **thể hoạt động (trophozoite)** bám niêm mạc ruột non, nhân lên → tạo nang mới theo phân ra ngoài.
"""),
("2. Parabasalids – Trichomonas (slide 17–21)", """
- Cũng có **ty thể tiêu giảm** gọi là **hydrogenosomes**: tạo **một phần năng lượng theo kiểu kỵ khí**, **giải phóng khí H₂** là sản phẩm phụ.
- Đại diện nổi tiếng: ***Trichomonas vaginalis*** – ký sinh **lây qua đường tình dục**, nhiễm khoảng **140 triệu người mỗi năm** (slide).
- Di chuyển dọc lớp niêm mạc đường sinh dục – tiết niệu nhờ **roi** và **màng lượn sóng (undulating membrane)** (một phần màng sinh chất uốn sóng).
- Sinh sản **phân đôi dọc**; không có giai đoạn nang điển hình.

| | Mitosome (*Giardia*) | Hydrogenosome (*Trichomonas*) |
|---|---|---|
| Nguồn gốc | ty thể tiêu giảm | ty thể tiêu giảm |
| Tạo năng lượng | không trực tiếp (không ETC) | **có**, kỵ khí |
| Sản phẩm phụ đặc trưng | – | **H₂** |
"""),
("3. Euglenozoans – đặc điểm chung (slide 22–23)", """
- Nhánh đa dạng: **dị dưỡng săn mồi, quang tự dưỡng, dinh dưỡng hỗn hợp, ký sinh**.
- Đặc điểm hình thái phân biệt: **một thanh (rod) có cấu trúc xoắn hoặc tinh thể bên trong mỗi roi**.
- Hai nhóm được nghiên cứu nhiều nhất: **kinetoplastids** và **euglenids**.
"""),
("4. Kinetoplastids – Trypanosoma (slide 24–27)", """
- Có **một ty thể lớn duy nhất** chứa một **khối DNA có tổ chức gọi là kinetoplast**.
- Có loài ăn vi khuẩn trong nước ngọt, biển, đất ẩm; có loài **ký sinh** động vật, thực vật, protists khác.
- Chi ***Trypanosoma*** gây bệnh ở người:
  - ***Trypanosoma brucei*** → **bệnh ngủ châu Phi (sleeping sickness)**, truyền qua ruồi tsetse.
  - ***Trypanosoma cruzi*** → **bệnh Chagas** (Nam Mỹ), truyền qua **phân** của bọ xít hút máu.
"""),
("5. Euglenids – Euglena (slide 28–30)", """
- ***Euglena***: tế bào hình thoi, có **roi** (một roi dài nhô ra), **lục lạp** (quang hợp), **điểm mắt (eyespot/stigma)** giúp nhận biết ánh sáng, **không bào co bóp** thải nước thừa, lớp **pellicle** protein dưới màng giúp giữ hình nhưng vẫn linh hoạt.
- **Dinh dưỡng hỗn hợp**: có ánh sáng → quang hợp; thiếu ánh sáng → hấp thụ chất hữu cơ, thực bào.
- Sinh sản **phân đôi dọc (longitudinal binary fission)**.
"""),
("6. Percolozoa – Naegleria fowleri (slide 31–32)", """
- ***Naegleria fowleri*** – "amip ăn não": sống trong **nước ngọt ấm** (hồ, suối nước nóng); vào mũi khi bơi lặn → theo dây thần kinh khứu giác lên não gây **viêm não – màng não tiên phát (PAM)**, tử vong rất cao.
- Có thể chuyển đổi giữa dạng **amip**, dạng **có roi** và **nang**. [mở rộng]
"""),
],
[
("Sức khỏe cộng đồng", """
- *Giardia* – nang **kháng chlorine** tương đối tốt → nước uống cần **lọc** (màng 1 μm) hoặc **đun sôi**. Du khách nên tránh uống nước suối chưa xử lý.
- *Trichomonas* – bệnh lây qua đường tình dục phổ biến nhất không do virus; điều trị bằng metronidazole (thuốc được hoạt hóa trong điều kiện kỵ khí nhờ hydrogenosome!).
- Bệnh ngủ châu Phi từng giết hàng trăm nghìn người; nhờ kiểm soát ruồi tsetse và thuốc mới, số ca giảm mạnh.
"""),
],
[
("Diplomonads", "Have **mitosomes** (reduced mitochondria) lacking functional electron transport chains, so they cannot use O₂; energy comes from **anaerobic pathways**. Many are parasites, e.g., ***Giardia intestinalis*** in mammalian intestines. **Two equal-sized nuclei** and **multiple flagella**.", "Giardia: mitosome, 2 nhân, nhiều roi."),
("Parabasalids", "Have **hydrogenosomes** that generate some energy anaerobically, releasing **H₂**. ***Trichomonas vaginalis*** is a sexually transmitted parasite (~140 million infections/year) that moves with **flagella and an undulating membrane**.", "Trichomonas: hydrogenosome, H₂."),
("Euglenozoans", "A rod with a **spiral or crystalline structure inside each flagellum**. **Kinetoplastids**: one large mitochondrion with a **kinetoplast** (organized DNA); *Trypanosoma brucei* (**sleeping sickness**), *T. cruzi* (**Chagas disease**). **Euglenids**: *Euglena*, mixotrophic, **longitudinal binary fission**.", "Kinetoplast; Trypanosoma; Euglena."),
],
["Mitosomes release hydrogen gas", "The kinetoplast is a second nucleus", "Trypanosoma cruzi causes sleeping sickness", "Giardia has one nucleus"])

q("PRO-02", "recall", 1, "Reduced mitochondria that generate some energy anaerobically and release hydrogen gas are called:",
  ["mitosomes", "hydrogenosomes", "kinetoplasts", "chromatophores"], 1,
  "Slide 17: **hydrogenosomes** của parabasalids (*Trichomonas*) giải phóng **H₂**.",
  ["Mitosome của Giardia không tạo H₂.", "", "Khối DNA trong ty thể.", "Màng quang hợp vi khuẩn."], ["hydrogenosome"], "Mitosomes release hydrogen gas", src=SRC + " slide 17")
q("PRO-02", "recall", 1, "Giardia intestinalis has:",
  ["one nucleus and a single flagellum", "two equal-sized nuclei and multiple flagella", "chloroplasts and an eyespot", "a silica shell"], 1,
  "Slide 15: diplomonads có **hai nhân bằng nhau và nhiều roi**.",
  ["Sai.", "", "Đó là Euglena.", "Đó là tảo silic."], ["Giardia"], "Giardia has one nucleus", src=SRC + " slide 15")
q("PRO-02", "concept", 2, "Why can diplomonads not use oxygen to extract energy from carbohydrates?",
  ["They lack ribosomes", "Their mitosomes lack functional electron transport chains", "They have chloroplasts", "Oxygen is toxic to their cell wall"], 1,
  "Slide 14: mitosome **không có chuỗi truyền electron hoạt động** → dùng con đường **kỵ khí**.",
  ["Có ribosome.", "", "Không có lục lạp.", "Không có thành kiểu đó."], ["mitosome"], src=SRC + " slide 14")
q("PRO-02", "recall", 1, "Which disease is caused by Trypanosoma cruzi?",
  ["African sleeping sickness", "Chagas disease", "Malaria", "Giardiasis"], 1,
  "Slide 27: ***T. cruzi*** → **bệnh Chagas**; ***T. brucei*** → **bệnh ngủ**.",
  ["T. brucei.", "", "Plasmodium.", "Giardia."], ["Trypanosoma"], "Trypanosoma cruzi causes sleeping sickness", src=SRC + " slide 27")
q("PRO-02", "concept", 2, "The kinetoplast of kinetoplastids is:",
  ["a second nucleus", "an organized mass of DNA inside a single large mitochondrion", "a chloroplast", "a contractile vacuole"], 1,
  "Slide 24: **kinetoplast** = khối DNA có tổ chức trong **một ty thể lớn**.",
  ["Không phải nhân.", "", "Sai.", "Sai."], ["kinetoplast"], "The kinetoplast is a second nucleus", src=SRC + " slide 24")
q("PRO-02", "recall", 1, "The main morphological feature distinguishing euglenozoans is:",
  ["a silica frustule", "a rod with a spiral or crystalline structure inside each flagellum", "cilia covering the cell", "a calcium carbonate test"], 1,
  "Slide 22: **thanh có cấu trúc xoắn hoặc tinh thể bên trong mỗi roi**.",
  ["Tảo silic.", "", "Ciliates.", "Forams."], ["euglenozoans"], src=SRC + " slide 22")
q("PRO-02", "concept", 2, "Trichomonas vaginalis moves along the mucus-coated reproductive tract using:",
  ["axial filaments", "flagella and an undulating part of its plasma membrane", "pseudopodia only", "cilia"], 1,
  "Slide 17: nhờ **roi** và **màng lượn sóng** (một phần màng sinh chất uốn sóng).",
  ["Xoắn thể vi khuẩn.", "", "Amip.", "Ciliates."], ["Trichomonas", "undulating membrane"])
q("PRO-02", "recall", 1, "Euglena reproduces asexually by:",
  ["budding", "longitudinal binary fission", "schizogony", "conjugation"], 1,
  "Slide 30: **phân đôi dọc (longitudinal binary fission)**.",
  ["Nấm men.", "", "Plasmodium.", "Ciliates."], ["Euglena"], pool="mock", src=SRC + " slide 30")
q("PRO-02", "not", 2, "Which statement about euglenozoans is NOT correct?",
  ["The clade includes photosynthetic autotrophs and parasites", "Kinetoplastids have a single large mitochondrion with a kinetoplast", "Euglena can be mixotrophic", "All euglenozoans are parasites of humans"], 3,
  "Euglenozoans rất đa dạng: săn mồi, quang tự dưỡng, hỗn hợp, ký sinh.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["euglenozoans"], pool="mock")
q("PRO-02", "application", 2, "A protist from a hot freshwater spring entered a swimmer's nose and caused fatal brain infection. It is most likely:",
  ["Giardia intestinalis", "Naegleria fowleri", "Euglena gracilis", "Trypanosoma brucei"], 1,
  "***Naegleria fowleri*** (Percolozoa, Excavata) – \"amip ăn não\" trong nước ngọt ấm.",
  ["Gây tiêu chảy.", "", "Không gây bệnh.", "Truyền qua ruồi tsetse."], ["Naegleria"], pool="mock")

v("PRO-02", "diplomonads", "nhóm diplomonad", "Excavate protists with two nuclei, multiple flagella and mitosomes.", "Giardia is one of the diplomonads.", ["diplomonad"])
v("PRO-02", "mitosome", "mitosome (ty thể tiêu giảm)", "A reduced mitochondrion lacking a functional electron transport chain.", "Giardia has mitosomes.", ["mitosomes"])
v("PRO-02", "Giardia", "Giardia", "Intestinal diplomonad parasite of mammals.", "Giardia forms cysts in water.", ["Giardia intestinalis", "Giardia lamblia"])
v("PRO-02", "parabasalids", "nhóm parabasalid", "Excavates with hydrogenosomes, e.g., Trichomonas.", "Trichomonas belongs to the parabasalids.", ["parabasalid"])
v("PRO-02", "hydrogenosome", "hydrogenosome", "A reduced mitochondrion producing energy anaerobically and releasing H2.", "Trichomonas has hydrogenosomes.", ["hydrogenosomes"])
v("PRO-02", "Trichomonas", "Trichomonas", "Sexually transmitted parabasalid parasite.", "Trichomonas vaginalis has an undulating membrane.", ["Trichomonas vaginalis"])
v("PRO-02", "undulating membrane", "màng lượn sóng", "An undulating portion of the plasma membrane aiding movement.", "Trichomonas moves with an undulating membrane.")
v("PRO-02", "euglenozoans", "nhóm trùng roi euglenozoa", "Excavates with a rod inside each flagellum.", "Euglena and Trypanosoma are euglenozoans.", ["euglenozoan"])
v("PRO-02", "kinetoplast", "kinetoplast", "An organized mass of DNA in the single large mitochondrion of kinetoplastids.", "Trypanosoma has a kinetoplast.", ["kinetoplastids"])
v("PRO-02", "Trypanosoma", "Trypanosoma", "Kinetoplastid parasite causing sleeping sickness and Chagas disease.", "Trypanosoma brucei causes sleeping sickness.", ["Trypanosoma brucei", "Trypanosoma cruzi"])
v("PRO-02", "Euglena", "trùng roi xanh Euglena", "Mixotrophic euglenid with chloroplasts and an eyespot.", "Euglena divides by longitudinal fission.", ["euglenids"])
v("PRO-02", "eyespot", "điểm mắt", "A pigmented spot that helps detect light direction.", "Euglena uses its eyespot to find light.", ["stigma"])

fc("PRO-02", "fact", "Mitosome vs hydrogenosome?", "Mitosome (Giardia): no functional ETC. Hydrogenosome (Trichomonas): anaerobic energy, releases H2.")
fc("PRO-02", "fact", "Giardia features?", "Two equal nuclei, multiple flagella, mitosomes; intestinal parasite; cyst ↔ trophozoite.")
fc("PRO-02", "fact", "Trypanosoma brucei vs T. cruzi?", "Sleeping sickness vs Chagas disease.")
fc("PRO-02", "number", "Trichomonas vaginalis infections per year (lecture)?", "About 140 million.")
fc("PRO-02", "trap", "TRUE/FALSE: the kinetoplast is a nucleus.", "FALSE – it is DNA inside a large mitochondrion.")

# ---------------------------------------------------------------- PRO-03
unit("PRO-03", "Stramenopiles: diatoms, brown algae and oomycetes", "M", 2, 20, SRC + ": slides 34–51",
"""Nạn đói khoai tây Ireland (1845–1849) làm **1 triệu người chết**. Thủ phạm *Phytophthora infestans* trông **giống nấm** – có sợi, bào tử – nhưng thực ra là **oomycete**, họ hàng gần của **tảo nâu** và **tảo silic**. Thành tế bào của nó là **cellulose**, không phải chitin. Ngoại hình có thể đánh lừa phân loại.""",
("Phytophthora infestans (potato blight) looks like a fungus but is an oomycete. Which feature shows it is not a true fungus?",
 ["It forms hyphae", "Its cell walls are made of cellulose rather than chitin", "It absorbs nutrients", "It produces spores"], 1,
 "Oomycetes có **thành cellulose** và **zoospore 2 roi**, thuộc **Stramenopiles** – khác nấm thật (thành **chitin**)."),
[
("1. Stramenopiles trong SAR", """
- **SAR** là nhóm **rất đa dạng** được định nghĩa bằng **sự tương đồng DNA** (slide 34).
- **Stramenopiles**: nhiều loài có **2 roi khác nhau** – một roi có **lông dạng ống (hairy)** và một roi **nhẵn** (ở giai đoạn có roi).
- Trong bài: **diatoms (tảo silic), brown algae (tảo nâu), oomycetes**.
"""),
("2. Diatoms – tảo silic (slide 35–36)", """
- Tảo **đơn bào**, **quang hợp**, cực kỳ phong phú ở biển và nước ngọt (**thực vật phù du**).
- Có **vỏ (frustule)** bằng **silica (SiO₂)** gồm **hai nửa lồng vào nhau** như hộp và nắp. [fig]
- Sinh sản vô tính: mỗi tế bào con nhận **một nửa vỏ cũ** và tạo **nửa mới nhỏ hơn bên trong** → kích thước trung bình **giảm dần** qua các thế hệ; kích thước được phục hồi nhờ **sinh sản hữu tính** tạo **auxospore**. [mở rộng]
- Xác tảo silic tích tụ → **đất tảo cát (diatomaceous earth)**: chất lọc, chất đánh bóng, thuốc trừ sâu tự nhiên.
"""),
("3. Brown algae – tảo nâu (slide 37–45)", """
- **Đa bào**, có loài rất lớn (tảo bẹ **kelp** dài hàng chục mét – *Laminaria, Macrocystis*); dạng sợi nhỏ như ***Ectocarpus*** (sinh vật mô hình, *Ectocarpus sp.* Ec32).
- Cơ thể (thallus) gồm **phiến (blade)**, **cuống (stipe)**, **bộ phận bám (holdfast)** – không phải lá, thân, rễ thật.
- **Thành phần sắc tố** (slide 41):
  - **Fucoxanthin**: **sắc tố chính tạo màu nâu**; hấp thụ hiệu quả ánh sáng **lam-lục đến lục** → quang hợp được ở **vùng nước sâu hoặc bị che bóng**; **che lấp** chlorophyll a và c.
  - **Chlorophyll a & c**: có nhưng màu xanh bị fucoxanthin át.
  - Carotenoid phụ: violaxanthin, β-carotene – góp phần hấp thụ ánh sáng, không ảnh hưởng nhiều tới màu.
- **Vòng đời luân phiên thế hệ** (*Laminaria*, *Ectocarpus*): **thể bào tử 2n** → giảm phân → **bào tử động (zoospore) n** → **thể giao tử n** (nhỏ) → giao tử → thụ tinh → **hợp tử 2n** → thể bào tử. [fig]
- Polysaccharide: **alginate**, **fucoidan** (khác fucoxanthin là sắc tố). [mở rộng]
"""),
("4. Oomycetes – nấm noãn (slide 46–51)", """
- Gồm **nấm nước (water molds)**, **mốc trắng**, **mốc sương (downy mildews)**; ví dụ ***Phytophthora***.
- **Giống nấm** về hình thái (**sợi**, hấp thụ dinh dưỡng) nhưng **khác**:
  - thành tế bào bằng **cellulose** (nấm: chitin);
  - **giai đoạn lưỡng bội** chiếm ưu thế;
  - **zoospore có 2 roi** (đặc trưng Stramenopiles) – slide 48–49: cấu trúc và đặc tính bơi của zoospore *Phytophthora*, tiếp nhận tín hiệu hóa học từ rễ cây chủ.
- Sinh sản hữu tính tạo **oospore (noãn bào tử)** vách dày, sống sót lâu trong đất.
- *Phytophthora infestans* – bệnh **mốc sương khoai tây/cà chua** (nạn đói Ireland); *Plasmopara viticola* – mốc sương nho.
"""),
],
[
("Tảo trong công nghiệp và đời sống", """
- **Alginate** từ tảo nâu: chất làm đặc trong kem, sữa chua, băng gạc cầm máu, cố định tế bào (tế bào nấm men bọc alginate trong lên men liên tục – liên hệ công nghệ sinh học).
- **Fucoxanthin** được nghiên cứu làm thực phẩm chức năng chống oxy hóa.
- Tảo silic là **chỉ thị chất lượng nước** và nguồn O₂ lớn của đại dương.
"""),
("Nông nghiệp: bệnh do oomycetes ở Việt Nam", """
*Phytophthora* gây **bệnh chết nhanh cây hồ tiêu**, thối rễ sầu riêng, mốc sương cà chua – thiệt hại lớn ở Tây Nguyên, miền Tây. Thuốc trừ nấm thông thường nhắm chitin/ergosterol **kém hiệu quả** vì oomycetes không phải nấm thật → phải dùng thuốc đặc hiệu (metalaxyl).
"""),
],
[
("Stramenopiles", "SAR is defined by **DNA similarities**. Stramenopiles typically have a **hairy flagellum and a smooth flagellum**. Examples: **diatoms, brown algae, oomycetes**.", "Hai roi khác nhau."),
("Diatoms and brown algae", "**Diatoms**: unicellular photosynthetic algae with a two-part **silica** shell (frustule). **Brown algae**: multicellular (e.g., *Ectocarpus*, kelps); **fucoxanthin** gives the brown color, absorbs **blue-green to green** light (deeper or shaded water) and **masks chlorophyll a and c**; alternation of generations.", "Tảo silic vỏ silica; tảo nâu fucoxanthin."),
("Oomycetes", "Water molds, white rusts, downy mildews (***Phytophthora***). Fungus-like hyphae, but **cellulose walls**, dominant diploid stage and **biflagellated zoospores**; sexual **oospores**.", "Giống nấm nhưng thành cellulose."),
],
["Oomycetes are true fungi", "Chlorophyll gives brown algae their color", "Diatom walls are cellulose"])

q("PRO-03", "recall", 1, "The main pigment giving brown algae their color is:",
  ["chlorophyll b", "phycoerythrin", "fucoxanthin", "bacteriochlorophyll"], 2,
  "Slide 41: **fucoxanthin** là sắc tố chính tạo màu nâu, che lấp chlorophyll a và c.",
  ["Tảo lục, thực vật.", "Tảo đỏ.", "", "Vi khuẩn quang hợp."], ["fucoxanthin"], "Chlorophyll gives brown algae their color", src=SRC + " slide 41")
q("PRO-03", "concept", 2, "Why does fucoxanthin help brown algae photosynthesize in deeper or shaded water?",
  ["It absorbs red light efficiently", "It absorbs blue-green to green light efficiently", "It reflects all light", "It fixes nitrogen"], 1,
  "Slide 41: fucoxanthin **hấp thụ hiệu quả ánh sáng lam-lục đến lục** – loại ánh sáng xuyên sâu hơn trong nước.",
  ["Ánh sáng đỏ bị nước hấp thụ nhanh.", "", "Sai.", "Sai."], ["fucoxanthin"], src=SRC + " slide 41")
q("PRO-03", "recall", 1, "Diatoms have cell walls (frustules) made of:",
  ["chitin", "cellulose plates in alveoli", "silica", "calcium carbonate"], 2,
  "Tảo silic có vỏ **silica** hai nửa lồng nhau.",
  ["Nấm.", "Dinoflagellates.", "", "Forams."], ["diatom", "frustule"], "Diatom walls are cellulose")
q("PRO-03", "concept", 2, "Which feature distinguishes oomycetes from true fungi?",
  ["Oomycetes form hyphae", "Oomycetes have cellulose cell walls and biflagellated zoospores", "Oomycetes absorb nutrients", "Oomycetes produce spores"], 1,
  "Oomycetes: **thành cellulose**, zoospore **2 roi** (Stramenopiles). Sợi, hấp thụ, bào tử thì nấm cũng có.",
  ["Nấm cũng có sợi.", "", "Nấm cũng hấp thụ.", "Nấm cũng có bào tử."], ["oomycetes"], "Oomycetes are true fungi")
q("PRO-03", "recall", 1, "Phytophthora, whose zoospores are shown in the lecture, belongs to:",
  ["Ascomycota", "Oomycetes", "Red algae", "Apicomplexans"], 1,
  "Slide 48–49: zoospore của ***Phytophthora*** – một **oomycete**.",
  ["Sai.", "", "Sai.", "Sai."], ["Phytophthora"], src=SRC + " slides 48–49")
q("PRO-03", "not", 2, "Which statement about brown algae is NOT correct?",
  ["They contain chlorophyll a and c", "Fucoxanthin masks the green color of chlorophyll", "They are prokaryotic cyanobacteria", "Ectocarpus is an example"], 2,
  "Tảo nâu là **nhân thực đa bào** (Stramenopiles), không phải vi khuẩn lam.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["brown algae"])
q("PRO-03", "concept", 2, "In the brown alga life cycle (alternation of generations), the large kelp body is:",
  ["the haploid gametophyte", "the diploid sporophyte", "a zygote", "a gamete"], 1,
  "Ở *Laminaria*, cơ thể lớn là **thể bào tử 2n**; thể giao tử n nhỏ.",
  ["Thể giao tử nhỏ.", "", "Sai.", "Sai."], ["alternation of generations"], pool="mock")
q("PRO-03", "recall", 1, "The SAR supergroup is defined mainly by:",
  ["silica shells", "DNA similarities", "cellulose walls", "parasitism"], 1,
  "Slide 34: SAR là nhóm rất đa dạng được định nghĩa bởi **tương đồng DNA**.",
  ["Chỉ tảo silic.", "", "Sai.", "Sai."], ["SAR"], pool="mock", src=SRC + " slide 34")
q("PRO-03", "not", 2, "Which pigment statement for brown algae is NOT correct?",
  ["Fucoxanthin is the main brown pigment", "Chlorophyll a and c are present", "Violaxanthin and β-carotene are minor pigments", "Chlorophyll b is the dominant pigment giving the brown color"], 3,
  "Tảo nâu có **chlorophyll a và c**, không phải b; màu nâu do **fucoxanthin**.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["fucoxanthin"], pool="mock")

v("PRO-03", "diatom", "tảo silic (tảo cát)", "A unicellular alga with a two-part silica shell.", "Diatoms are major marine producers.", ["diatoms"])
v("PRO-03", "frustule", "vỏ silic", "The two-part silica wall of a diatom.", "The frustule fits together like a box and lid.")
v("PRO-03", "brown algae", "tảo nâu", "Multicellular stramenopile algae colored by fucoxanthin.", "Kelps are brown algae.", ["kelp"])
v("PRO-03", "fucoxanthin", "fucoxanthin", "The brown carotenoid pigment of brown algae that absorbs blue-green light.", "Fucoxanthin masks chlorophyll.")
v("PRO-03", "oomycetes", "nấm noãn (oomycete)", "Fungus-like stramenopiles with cellulose walls and biflagellated zoospores.", "Phytophthora is one of the oomycetes.", ["oomycete", "water molds"])
v("PRO-03", "Phytophthora", "Phytophthora", "Oomycete genus causing potato late blight and root rots.", "Phytophthora infestans caused the Irish famine.")
v("PRO-03", "alternation of generations", "luân phiên thế hệ", "A life cycle alternating between multicellular diploid and haploid stages.", "Brown algae show alternation of generations.", ["sporophyte", "gametophyte"])
v("PRO-03", "oospore", "noãn bào tử", "A thick-walled sexual spore of oomycetes.", "Oospores survive in soil.", ["oospores"])

fc("PRO-03", "fact", "Brown algae pigments (lecture)?", "Fucoxanthin (main, brown, absorbs blue-green/green, masks chlorophyll), chlorophyll a & c, minor violaxanthin, β-carotene.")
fc("PRO-03", "fact", "Oomycetes vs true fungi?", "Oomycetes: cellulose walls, diploid dominant, biflagellated zoospores. Fungi: chitin walls.")
fc("PRO-03", "fact", "Diatom shell material?", "Silica (two overlapping halves).")
fc("PRO-03", "trap", "TRUE/FALSE: Phytophthora is a true fungus.", "FALSE – it is an oomycete (stramenopile).")

# ---------------------------------------------------------------- PRO-04
unit("PRO-04", "Alveolates and Rhizaria: dinoflagellates, apicomplexans, ciliates and forams", "H", 2, 25, SRC + ": slides 52–71",
"""Mỗi năm vẫn có hàng trăm triệu ca **sốt rét**. Ký sinh trùng *Plasmodium* luân phiên sống trong **muỗi** và **người**, lúc ở gan, lúc ở hồng cầu, mỗi giai đoạn một tên. Nó là họ hàng của *Paramecium* và của tảo hai roi gây **thủy triều đỏ** – cả ba cùng thuộc nhóm **Alveolates** có túi màng (alveoli) dưới màng tế bào.""",
("In the malaria life cycle, which stage is injected into humans by the mosquito?",
 ["Merozoites", "Sporozoites", "Gametocytes", "Oospores"], 1,
 "Slide 59: dạng truyền giữa các vật chủ là tế bào nhỏ gọi là **sporozoites**, được muỗi tiêm vào máu người."),
[
("1. Alveolates – đặc điểm chung", """
- Có các **túi màng (alveoli)** nằm ngay **dưới màng sinh chất**.
- Gồm **dinoflagellates, apicomplexans, ciliates**.
"""),
("2. Dinoflagellates – tảo hai roi (slide 52–58)", """
- **Vỏ ngoài (theca)** gồm các **tấm cellulose** nằm **trong các alveoli** màng → tạo lớp giáp cứng liên tục ngay dưới màng sinh chất (ví dụ *Pfiesteria shumwayae*).
- Có **2 roi**: một roi nằm trong **rãnh ngang**, một roi **dọc** → chuyển động xoay tròn. [fig]
- **Dinh dưỡng hỗn hợp (mixotrophic)**: **dị dưỡng**, và trong một số điều kiện **quang hợp**; ăn hạt hữu cơ hoặc con mồi bằng **thực bào**.
- Sinh sản phổ biến bằng **phân đôi vô tính**.
- Một số loài bùng phát gây **thủy triều đỏ (red tide)**, tiết độc tố tích lũy trong nghêu sò. [mở rộng]
"""),
("3. Apicomplexans – Plasmodium (slide 59–62)", """
- **Ký sinh động vật**; có **phức hợp đỉnh (apical complex)** giúp xâm nhập tế bào chủ.
- Dạng truyền giữa các vật chủ là tế bào nhỏ gọi là **sporozoites**.
- Vòng đời phức tạp với **cả giai đoạn vô tính và hữu tính**, thường cần **hai hoặc nhiều vật chủ**.
- ***Plasmodium*** gây **sốt rét (malaria)**, sống ở **muỗi và người**; slide: nhiễm **~300 triệu người** ở vùng nhiệt đới, **~2 triệu ca tử vong/năm** (số liệu cũ).

**Vòng đời *Plasmodium falciparum*** [fig]:
1. Muỗi *Anopheles* cái đốt → tiêm **sporozoites** vào máu.
2. Sporozoites vào **tế bào gan (hepatocyte)**; trong **không bào ký sinh (parasitophorous vacuole)**, mỗi trophozoite thực hiện **schizogony** – **nhiều vòng nguyên phân** tạo tế bào hợp bào (**coenocyte**) gọi là **schizont** → giải phóng **merozoites**.
3. Merozoites xâm nhập **hồng cầu**; nhân lên (**schizogony hồng cầu – erythrocytic schizogony**), phá vỡ hồng cầu → **cơn sốt**. Ở giai đoạn schizont, ký sinh trùng **nhân đôi DNA nhiều lần** và các lần nguyên phân diễn ra **không đồng bộ**.
4. Một số merozoites biệt hóa thành **gametocytes** (giao tử bào).
5. Muỗi hút máu nhận gametocytes → trong ruột muỗi tạo **giao tử, thụ tinh** → hợp tử → noãn nang → tạo sporozoites mới về tuyến nước bọt.
- **Muỗi**: vật chủ **chính** (sinh sản hữu tính); **người**: vật chủ **trung gian** (sinh sản vô tính).
"""),
("4. Ciliates – trùng lông (slide 63–65)", """
- Dùng **lông (cilia)** để **di chuyển và kiếm ăn**; ví dụ ***Paramecium***.
- Có **2 loại nhân**: **nhân lớn (macronucleus)** – điều khiển hoạt động hằng ngày; **nhân nhỏ (micronucleus)** – vai trò trong sinh sản hữu tính.
- **Rãnh miệng (oral groove)** → **không bào tiêu hóa (food vacuole)**; **không bào co bóp (contractile vacuole)** thải nước thừa.
- Sinh sản: **vô tính – phân đôi ngang**; **hữu tính – tiếp hợp (conjugation)**: hai tế bào trao đổi nhân nhỏ → tái tổ hợp di truyền (không tăng số lượng). [fig]
"""),
("5. Foraminiferans – trùng lỗ (Rhizaria) (slide 66–71)", """
- **Forams** có **vỏ (test) xốp nhiều lỗ**, là **một mảnh chất hữu cơ** thường **được cứng hóa bằng calcium carbonate (CaCO₃)**.
- **Chân giả (pseudopodia)** thò qua các lỗ → dùng để **bơi, tạo vỏ và kiếm ăn**.
- Có loài lấy dinh dưỡng từ **quang hợp của tảo cộng sinh** sống trong vỏ.
- **Hóa thạch foram** là **chỉ thị tuyệt vời để đối chiếu tuổi đá trầm tích** ở các nơi khác nhau trên thế giới (dùng trong thăm dò dầu khí). Vỏ nhiều buồng nhưng vẫn là **đơn bào**.
"""),
],
[
("Sốt rét và thuốc artemisinin", """
**Artemisinin** chiết từ cây thanh hao hoa vàng (*Artemisia annua*) – công trình đoạt Nobel 2015 của Tu Youyou – diệt nhanh thể trong hồng cầu. Việt Nam từng là điểm nóng sốt rét và đã giảm mạnh số ca nhờ màn tẩm hóa chất, phun thuốc diệt muỗi, điều trị phối hợp artemisinin. Kháng artemisinin đang xuất hiện ở Tiểu vùng sông Mekong.
"""),
("Thủy triều đỏ và an toàn hải sản", """
Một số dinoflagellates (*Alexandrium, Karenia*) tiết **saxitoxin, brevetoxin** tích lũy trong nghêu, sò → ngộ độc liệt cơ, có thể tử vong. Nấu chín **không phá** độc tố. Cơ quan thú y thủy sản giám sát mật độ tảo độc ở vùng nuôi nhuyễn thể.
"""),
],
[
("Dinoflagellates", "External covering (**theca**) of **cellulose plates inside membranous alveoli**, just beneath the plasma membrane (e.g., *Pfiesteria shumwayae*). Two flagella. **Mixotrophic**: heterotrophic and, under some conditions, photosynthetic; ingest prey by **phagocytosis**. Commonly reproduce by **asexual binary fission**.", "Giáp cellulose trong alveoli; hỗn hợp."),
("Apicomplexans", "Animal **parasites**; the stage transmitted between hosts is the **sporozoite**. Complex cycle with **asexual and sexual stages**, often **two or more hosts**. *Plasmodium* causes **malaria**, lives in **mosquitoes and humans** (~300 million infected, ~2 million deaths/year per lecture). In liver cells, trophozoites undergo **schizogony** → **schizont** (coenocyte) → merozoites; **erythrocytic schizogony** in red blood cells.", "Sporozoite → gan → hồng cầu → gametocyte."),
("Ciliates and forams", "**Ciliates** (*Paramecium*) use cilia to move and feed; **macronucleus** and **micronucleus**; conjugation. **Forams**: porous **tests** of organic material hardened with **CaCO₃**; pseudopodia for swimming, test formation and feeding; some host symbiotic algae; fossils **date sedimentary rocks**.", "Ciliates 2 loại nhân; forams vỏ CaCO₃."),
],
["Merozoites are injected by mosquitoes", "Forams are multicellular because of many chambers", "Dinoflagellate theca is silica", "Humans are the definitive host of Plasmodium"])

q("PRO-04", "recall", 1, "The theca of dinoflagellates such as Pfiesteria is made of:",
  ["silica", "cellulose plates located within membranous alveoli", "calcium carbonate", "chitin"], 1,
  "Slide 55–57: theca = **tấm cellulose nằm trong alveoli** ngay dưới màng sinh chất.",
  ["Tảo silic.", "", "Forams.", "Nấm."], ["theca", "dinoflagellates"], "Dinoflagellate theca is silica", src=SRC + " slides 55–57")
q("PRO-04", "recall", 1, "Plasmodium, the malaria parasite, belongs to the:",
  ["ciliates", "apicomplexans", "diplomonads", "oomycetes"], 1,
  "Slide 59: *Plasmodium* thuộc **Apicomplexans** – ký sinh động vật, truyền bằng sporozoites.",
  ["Paramecium.", "", "Giardia.", "Phytophthora."], ["apicomplexans"], src=SRC + " slide 59")
q("PRO-04", "concept", 2, "In the liver stage of Plasmodium, each trophozoite undergoes schizogony. What does this mean?",
  ["Two cells fuse to form a zygote", "Many rounds of mitosis produce a multinucleate schizont that releases many merozoites", "The cell forms a spore coat", "Meiosis produces gametes"], 1,
  "Slide 61: schizogony = **nhiều vòng nguyên phân** tạo **schizont** hợp bào (coenocyte) → giải phóng nhiều merozoite.",
  ["Đó là thụ tinh.", "", "Sai.", "Sai."], ["schizogony", "schizont"], src=SRC + " slide 61")
q("PRO-04", "concept", 2, "Which statement about Plasmodium hosts is correct?",
  ["It needs only one host", "It lives in both mosquitoes and humans; sexual reproduction occurs in the mosquito", "Humans are where fertilization occurs", "It is transmitted by fecal-oral route"], 1,
  "Slide 59: sống ở **muỗi và người**; hữu tính trong **muỗi** (vật chủ chính), vô tính trong người.",
  ["Cần hai vật chủ.", "", "Ngược lại.", "Truyền qua muỗi."], ["Plasmodium"], "Humans are the definitive host of Plasmodium")
q("PRO-04", "recall", 1, "Foraminiferan tests are made of:",
  ["silica only", "organic material typically hardened with calcium carbonate", "cellulose plates", "peptidoglycan"], 1,
  "Slide 66: test là một mảnh chất hữu cơ **cứng hóa bằng CaCO₃**.",
  ["Tảo silic.", "", "Dinoflagellates.", "Vi khuẩn."], ["foraminiferans", "test"], src=SRC + " slide 66")
q("PRO-04", "concept", 2, "Why are foram fossils useful to geologists?",
  ["They glow under UV", "They are excellent markers for correlating the ages of sedimentary rocks", "They contain DNA", "They produce oil directly"], 1,
  "Slide 66: hóa thạch foram là **chỉ thị đối chiếu tuổi đá trầm tích** trên thế giới.",
  ["Sai.", "", "Sai.", "Sai."], ["foraminiferans"])
q("PRO-04", "concept", 2, "Paramecium has two types of nuclei. The micronucleus functions mainly in:",
  ["daily metabolism", "sexual reproduction (genetic exchange during conjugation)", "photosynthesis", "excretion"], 1,
  "**Micronucleus**: vai trò di truyền trong **sinh sản hữu tính (tiếp hợp)**; **macronucleus** điều khiển hoạt động hằng ngày.",
  ["Macronucleus.", "", "Sai.", "Không bào co bóp."], ["ciliates", "micronucleus"])
q("PRO-04", "recall", 1, "Dinoflagellates are described in the lecture as mixotrophic. This means they:",
  ["are only photosynthetic", "are heterotrophic and, under some conditions, photosynthetic", "absorb nutrients like fungi only", "are chemoautotrophs"], 1,
  "Slide 58: **dị dưỡng, và trong một số điều kiện quang hợp**; ăn con mồi bằng thực bào.",
  ["Sai.", "", "Sai.", "Sai."], ["mixotroph"], pool="mock")
q("PRO-04", "not", 2, "Which statement about the Plasmodium life cycle is NOT correct?",
  ["Sporozoites are transmitted between hosts", "Schizogony occurs in hepatocytes", "Erythrocytic schizogony occurs in red blood cells", "Merozoites are injected by the mosquito into human blood"], 3,
  "Muỗi tiêm **sporozoites**; merozoites được tạo ra trong gan/hồng cầu.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["Plasmodium", "sporozoite"], "Merozoites are injected by mosquitoes", pool="mock")
q("PRO-04", "concept", 2, "The pseudopodia of forams extend through the pores of the test and function in:",
  ["photosynthesis only", "swimming, test formation and feeding", "DNA exchange", "producing silica"], 1,
  "Slide 66: chân giả dùng để **bơi, tạo vỏ, kiếm ăn**.",
  ["Sai.", "", "Sai.", "Sai."], ["pseudopodia"], pool="mock")
q("PRO-04", "not", 2, "Which statement about foraminiferans is NOT correct?",
  ["They have porous tests", "Some derive nourishment from symbiotic algae", "A multichambered test means the organism is multicellular", "Their fossils help date sedimentary rocks"], 2,
  "Vỏ nhiều buồng nhưng foram vẫn là **đơn bào**.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["foraminiferans"], "Forams are multicellular because of many chambers", pool="mock")

v("PRO-04", "alveoli", "túi màng alveoli", "Membrane-bound sacs beneath the plasma membrane of alveolates.", "Dinoflagellate plates lie in alveoli.")
v("PRO-04", "dinoflagellates", "tảo hai roi (giáp tảo)", "Alveolates with two flagella and often a cellulose theca.", "Some dinoflagellates cause red tides.", ["dinoflagellate"])
v("PRO-04", "theca", "vỏ giáp (theca)", "The armor of cellulose plates in alveoli of dinoflagellates.", "The theca protects Pfiesteria.")
v("PRO-04", "apicomplexans", "ngành bào tử trùng (apicomplexa)", "Parasitic alveolates transmitted as sporozoites.", "Plasmodium belongs to the apicomplexans.", ["apicomplexan"])
v("PRO-04", "Plasmodium", "Plasmodium (ký sinh trùng sốt rét)", "Apicomplexan genus causing malaria.", "Plasmodium falciparum causes severe malaria.", ["Plasmodium falciparum", "malaria"])
v("PRO-04", "sporozoite", "thoa trùng (sporozoite)", "The infective stage transmitted from mosquito to human.", "Sporozoites travel to the liver.", ["sporozoites"])
v("PRO-04", "merozoite", "mảnh trùng (merozoite)", "Stage released by schizonts that infects red blood cells.", "Merozoites invade erythrocytes.", ["merozoites"])
v("PRO-04", "schizogony", "sinh sản phân liệt (schizogony)", "Multiple rounds of mitosis forming a multinucleate schizont before splitting.", "Schizogony occurs in liver cells.", ["schizont", "erythrocytic schizogony"])
v("PRO-04", "gametocyte", "giao tử bào", "Plasmodium stage that forms gametes in the mosquito.", "Mosquitoes ingest gametocytes.", ["gametocytes"])
v("PRO-04", "ciliates", "trùng lông", "Alveolates using cilia for movement and feeding.", "Paramecium is one of the ciliates.", ["ciliate", "cilia", "Paramecium"])
v("PRO-04", "macronucleus", "nhân lớn", "The large nucleus controlling daily functions in ciliates.", "The macronucleus controls metabolism.", ["micronucleus"])
v("PRO-04", "foraminiferans", "trùng lỗ (foram)", "Rhizarians with porous CaCO3-hardened tests.", "Foram fossils date rocks.", ["forams", "foraminiferan"])
v("PRO-04", "test", "vỏ (của trùng lỗ)", "The porous shell of a foraminiferan.", "The test is hardened with calcium carbonate.", ["tests"])
v("PRO-04", "pseudopodia", "chân giả", "Cytoplasmic extensions used for movement and feeding.", "Forams extend pseudopodia through pores.", ["pseudopodium"])

fc("PRO-04", "fact", "Dinoflagellate theca?", "Cellulose plates inside membranous alveoli beneath the plasma membrane.")
fc("PRO-04", "fact", "Plasmodium life cycle stages?", "Sporozoites (mosquito → blood) → liver schizogony → merozoites → red-cell schizogony → gametocytes → mosquito (sexual).")
fc("PRO-04", "number", "Malaria figures in the lecture?", "~300 million infected, ~2 million deaths per year.")
fc("PRO-04", "fact", "Foram test and uses?", "Organic material hardened with CaCO3; pseudopodia through pores; fossils date sedimentary rocks.")
fc("PRO-04", "fact", "Two nuclei of ciliates?", "Macronucleus (daily functions) and micronucleus (sexual/genetic exchange).")

# ---------------------------------------------------------------- PRO-05
unit("PRO-05", "Archaeplastida (red and green algae) and slime molds", "M", 2, 20, SRC + ": slides 72–101",
"""Đĩa thạch bạn dùng trong lab làm từ **agar** chiết từ **tảo đỏ** *Gracilaria*; rong biển cuộn sushi (nori) cũng là tảo đỏ. Còn **tảo lục** *Chara* được xem là họ hàng gần nhất của **thực vật trên cạn**. Và trên khúc gỗ mục trong rừng ẩm, một khối **nhầy vàng cam bò chậm** – nấm nhầy – từng bị xếp nhầm vào nấm.""",
("Agar used in microbiology media is extracted from:",
 ["brown algae", "red algae such as Gracilaria", "green algae", "diatoms"], 1,
 "Slide 77: **tảo đỏ *Gracilaria dura*** dùng chiết **agarose/agar**."),
[
("1. Tảo đỏ – red algae (slide 72–78)", """
- Thuộc **Archaeplastida**; đa số **đa bào**, sống ở biển, một số ở **vùng nước sâu** (sắc tố **phycoerythrin** hấp thụ ánh sáng lam, tạo màu đỏ) [mở rộng].
- **Không có giai đoạn mang roi** trong vòng đời.
- Ứng dụng: **agar/agarose** (*Gracilaria dura* – slide 77, Gupta et al. 2011 nghiên cứu sinh trưởng và đặc tính agarose của thể giao tử đực, cái và thể bào tử), **carrageenan**, **nori** (*Porphyra/Pyropia*).
- Vòng đời *Gracilaria* **ba pha**: **thể giao tử (n)** → thụ tinh → **thể quả bào tử (carposporophyte, 2n)** trên thể cái → **quả bào tử 2n** → **thể tứ bào tử (tetrasporophyte, 2n)** → giảm phân → **tứ bào tử n** → thể giao tử. [fig] (Ba pha nhưng chỉ **hai mức bội**.)
"""),
("2. Tảo lục – chlorophytes (slide 79–85)", """
- Có **chlorophyll a và b** (giống thực vật), dự trữ tinh bột, thành cellulose. [mở rộng]
- Đa dạng hình thức tổ chức:
  - **đơn bào**: *Chlamydomonas* (2 roi; vòng đời **đơn bội trội**, hợp tử 2n là giai đoạn lưỡng bội duy nhất);
  - **tập đoàn**: *Volvox, Pediastrum*;
  - **đa bào**: *Ulva* (rau diếp biển – luân phiên thế hệ, hai thế hệ giống nhau về hình dạng);
  - **hợp bào nhiều nhân**: *Caulerpa*.
"""),
("3. Tảo lục – charophytes (slide 86–91)", """
**Charophytes** (*Chara, Coleochaete*) là **tảo duy nhất chia sẻ 4 đặc điểm với thực vật trên cạn**:
1. **Phức hợp tổng hợp cellulose dạng hoa thị (rosette-shaped cellulose synthase complexes)** trên màng sinh chất → tổng hợp **vi sợi cellulose** cho thành tế bào.
2. **Enzyme peroxisome** giúp **hạn chế mất chất hữu cơ do quang hô hấp (photorespiration)**:
   - Phản ứng đầu tiên chu trình Calvin: **ribulose-1,5-bisphosphate + CO₂ → 2 3-phosphoglycerate**.
   - Nếu RuBisCO phản ứng với **O₂** thay vì CO₂: ribulose-1,5-bisphosphate + O₂ → 3-phosphoglycerate + **phosphoglycolate** → glycolate → vào **peroxisome**: glycine → vào **ty thể**: serine → về **peroxisome**: glycerate → về **lục lạp** tham gia chu trình Calvin.
   - **Peroxisome của các tảo khác không có** các enzyme này.
   - (Chu trình Calvin dùng **ATP và NADPH** để biến CO₂ thành đường.)
3. **Cấu trúc tinh trùng (có roi)** tương tự.
4. Ở chi *Chara* và *Coleochaete*, **phragmoplast** (hệ **vi ống**) hình thành giữa hai nhân của hai tế bào mới sau phân chia.
"""),
("4. Nấm nhầy – slime molds (Unikonta) (slide 92–101)", """
- **Mycetozoans ("fungus animals")**; **trước đây bị xem là nấm sợi**. Chia 2 nhánh phân biệt bằng **chu trình sinh sản**:

**a) Plasmodial slime molds (nấm nhầy hợp bào)**:
- Màu **sáng** (thường **vàng hoặc cam**).
- **Không phải đa bào**: là **một khối tế bào chất không ngăn bởi màng sinh chất**, chứa **nhiều nhân lưỡng bội** – sản phẩm của **nguyên phân không kèm phân chia tế bào chất** (plasmodium).
- Gặp **điều kiện khắc nghiệt** → biệt hóa thành **thể quả (fruiting bodies)** phục vụ **sinh sản hữu tính** (giảm phân → bào tử n).
- Phần lớn nhỏ, nhưng nhóm **Myxogastria** tạo plasmodium lớn **nhìn thấy bằng mắt thường**.

**b) Cellular slime molds (nấm nhầy tế bào)** – vd *Dictyostelium*:
- **Giai đoạn kiếm ăn**: các tế bào (amip đơn bội) **hoạt động riêng lẻ**.
- **Khi cạn thức ăn**: tế bào **kết tụ thành khối giống con sên (slug)** hoạt động như một đơn vị.
- **Khác** plasmodium: các tế bào kết tụ **vẫn tách biệt bởi màng sinh chất riêng**.
- Cuối cùng khối kết tụ tạo **thể quả vô tính (asexual fruiting body)** → bào tử.

| | Hợp bào (plasmodial) | Tế bào (cellular) |
|---|---|---|
| Dạng kiếm ăn | **plasmodium** 1 khối nhiều nhân **2n** | **amip đơn bội riêng lẻ** |
| Màng giữa các nhân | **không** | **có** (mỗi tế bào) |
| Khi đói | thể quả **hữu tính** | kết tụ "slug" → thể quả **vô tính** |
"""),
],
[
("Agar – từ biển vào phòng thí nghiệm", """
Việt Nam trồng rong câu *Gracilaria* ở đầm phá (Thừa Thiên Huế, Ninh Thuận) để chiết **agar** – dùng trong thạch rau câu, mỹ phẩm và môi trường vi sinh. Agarose tinh khiết dùng cho **điện di DNA** (IDT-02).
"""),
("Nấm nhầy \"thông minh\"", """
*Physarum polycephalum* (nấm nhầy hợp bào) có thể tìm đường ngắn nhất qua mê cung và \"thiết kế\" mạng lưới giống hệ thống đường sắt Tokyo (Nobel Ig 2010). *Dictyostelium* là sinh vật mô hình nghiên cứu **tín hiệu tế bào (cAMP)** và sự biệt hóa.
"""),
],
[
("Red algae", "Mostly multicellular marine algae; no flagellated stages. ***Gracilaria dura*** is used for **agarose** extraction. Life cycle has three phases: gametophyte (n), carposporophyte (2n), tetrasporophyte (2n).", "Tảo đỏ → agar."),
("Green algae", "**Chlorophytes**: *Chlamydomonas* (unicellular), *Volvox* (colonial), *Ulva* (multicellular). **Charophytes** share 4 features with land plants: **rosette cellulose-synthase complexes**; **peroxisome enzymes** limiting photorespiration losses; similar **flagellated sperm**; **phragmoplast** (microtubules) between daughter nuclei in *Chara* and *Coleochaete*.", "Charophytes: 4 điểm giống thực vật."),
("Slime molds", "Mycetozoans, once thought to be fungi. **Plasmodial**: bright yellow/orange **plasmodium** = one mass of cytoplasm with **many diploid nuclei**, no membranes between them (mitosis without cytokinesis); forms fruiting bodies for **sexual** reproduction. **Cellular**: individual cells feed; when food runs out they **aggregate into a slug** whose cells keep their **own membranes**; form an **asexual** fruiting body.", "Hợp bào vs tế bào."),
],
["Plasmodial slime molds are multicellular", "Cellular slime mold cells fuse into one cytoplasm", "Slime molds are true fungi", "All algae peroxisomes limit photorespiration"])

q("PRO-05", "recall", 1, "Which red alga is shown in the lecture as a source of agarose?",
  ["Laminaria", "Gracilaria dura", "Chlamydomonas", "Ectocarpus"], 1,
  "Slide 77: ***Gracilaria dura*** dùng chiết **agarose**.",
  ["Tảo nâu.", "", "Tảo lục.", "Tảo nâu."], ["red algae", "agarose"], src=SRC + " slide 77")
q("PRO-05", "concept", 2, "A plasmodial slime mold is described as NOT multicellular because it is:",
  ["a single cell with one nucleus", "a mass of cytoplasm containing many diploid nuclei not separated by plasma membranes", "a colony of separate amoebae", "a bacterium"], 1,
  "Slide 93: plasmodium = **một khối tế bào chất không ngăn bởi màng**, nhiều **nhân 2n** – do nguyên phân không phân chia tế bào chất.",
  ["Có nhiều nhân.", "", "Đó là nấm nhầy tế bào.", "Sai."], ["plasmodial slime mold", "plasmodium"], "Plasmodial slime molds are multicellular", src=SRC + " slide 93")
q("PRO-05", "concept", 2, "How does the slug of a cellular slime mold differ from the plasmodium of a plasmodial slime mold?",
  ["The slug has no nuclei", "Cells in the slug remain separated by their own plasma membranes", "The slug is photosynthetic", "The slug forms sexual fruiting bodies only"], 1,
  "Slide 99: các tế bào kết tụ **vẫn tách biệt bởi màng sinh chất riêng**, khác plasmodium.",
  ["Sai.", "", "Sai.", "Tạo thể quả vô tính."], ["cellular slime mold"], "Cellular slime mold cells fuse into one cytoplasm", src=SRC + " slide 99")
q("PRO-05", "not", 2, "Which is NOT one of the four features that charophytes share with land plants?",
  ["Rosette-shaped cellulose-synthase complexes", "Peroxisome enzymes that limit losses from photorespiration", "Similar flagellated sperm", "Silica frustules"], 3,
  "Slide 88–91: 4 đặc điểm: phức hợp cellulose hoa thị, enzyme peroxisome (quang hô hấp), tinh trùng có roi, phragmoplast. **Vỏ silica** là của tảo silic.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["charophytes"], src=SRC + " slides 88–91")
q("PRO-05", "recall", 1, "In Chara and Coleochaete, which structure forms between the nuclei of two new cells after division?",
  ["Septum", "Phragmoplast (microtubules)", "Cell plate of chitin", "Frustule"], 1,
  "Slide 91: **phragmoplast** (vi ống) hình thành giữa hai nhân con.",
  ["Nấm.", "", "Sai.", "Tảo silic."], ["phragmoplast"])
q("PRO-05", "concept", 2, "In photorespiration, RuBisCO reacts with O2 instead of CO2. What does this first reaction produce?",
  ["Two 3-phosphoglycerate", "3-phosphoglycerate + phosphoglycolate", "Glucose", "Pyruvate + CO2"], 1,
  "Slide 89: RuBP + O₂ → **3-phosphoglycerate + phosphoglycolate**. (Với CO₂: RuBP + CO₂ → 2 3-PGA.)",
  ["Đó là phản ứng với CO₂.", "", "Sai.", "Sai."], ["photorespiration"], "All algae peroxisomes limit photorespiration", src=SRC + " slide 89")
q("PRO-05", "recall", 1, "What happens when a cellular slime mold runs out of food?",
  ["It forms a plasmodium with diploid nuclei", "Cells aggregate into a slug-like mass that functions as a unit and forms an asexual fruiting body", "It photosynthesizes", "It forms endospores"], 1,
  "Slide 99: **kết tụ thành slug** → **thể quả vô tính**.",
  ["Đó là nấm nhầy hợp bào.", "", "Sai.", "Sai."], ["cellular slime mold"])
q("PRO-05", "recall", 1, "Slime molds (mycetozoans) were previously thought to be:",
  ["bacteria", "filamentous fungi", "red algae", "viruses"], 1,
  "Slide 92: trước đây bị xem là **nấm sợi**.",
  ["Sai.", "", "Sai.", "Sai."], ["slime mold"], "Slime molds are true fungi", pool="mock", src=SRC + " slide 92")
q("PRO-05", "concept", 2, "Under harsh conditions, plasmodial slime molds:",
  ["form endospores", "differentiate into fruiting bodies that function in sexual reproduction", "aggregate into a slug", "become photosynthetic"], 1,
  "Slide 93: điều kiện khắc nghiệt → **thể quả** phục vụ **sinh sản hữu tính**.",
  ["Vi khuẩn.", "", "Nấm nhầy tế bào.", "Sai."], ["plasmodial slime mold"], pool="mock")
q("PRO-05", "concept", 2, "Which statement about the Gracilaria life cycle is correct?",
  ["It has three phases but only two ploidy levels (n and 2n)", "It has n, 2n and 3n phases", "It has flagellated gametes", "It has only a haploid phase"], 0,
  "Ba pha: thể giao tử n, thể quả bào tử 2n, thể tứ bào tử 2n → **chỉ 2 mức bội**. Tảo đỏ **không có giai đoạn có roi**.",
  ["", "Không có 3n.", "Tảo đỏ không có roi.", "Sai."], ["red algae"], pool="mock")
q("PRO-05", "not", 2, "Which statement about plasmodial slime molds is NOT correct?",
  ["They are often yellow or orange", "Their nuclei are diploid", "Their feeding stage consists of separate amoeboid cells with individual membranes", "Some Myxogastria are visible to the naked eye"], 2,
  "Tế bào riêng lẻ có màng là giai đoạn kiếm ăn của **nấm nhầy tế bào**.",
  ["Đúng.", "Đúng.", "", "Đúng."], ["plasmodial slime mold"], pool="mock")

v("PRO-05", "red algae", "tảo đỏ", "Mostly multicellular marine algae without flagellated stages; source of agar.", "Gracilaria is one of the red algae.", ["red alga", "Gracilaria"])
v("PRO-05", "agarose", "agarose", "The gelling polysaccharide fraction of agar from red algae.", "Agarose gels separate DNA.")
v("PRO-05", "green algae", "tảo lục", "Algae with chlorophyll a and b: chlorophytes and charophytes.", "Chlamydomonas is one of the green algae.", ["chlorophytes", "Chlamydomonas", "Volvox", "Ulva"])
v("PRO-05", "charophytes", "tảo vòng (charophyte)", "Green algae most closely related to land plants.", "Chara is one of the charophytes.", ["charophyte", "Chara", "Coleochaete"])
v("PRO-05", "photorespiration", "quang hô hấp", "Reaction of RuBisCO with O2 that wastes fixed carbon.", "Peroxisomes help recover carbon lost in photorespiration.")
v("PRO-05", "Calvin cycle", "chu trình Calvin", "Pathway using ATP and NADPH to convert CO2 into sugar.", "The first step of the Calvin cycle fixes CO2 to RuBP.")
v("PRO-05", "phragmoplast", "phragmoplast", "A microtubule array forming between daughter nuclei during plant-type cytokinesis.", "Chara forms a phragmoplast.")
v("PRO-05", "slime mold", "nấm nhầy", "Mycetozoan protist once classified as a fungus.", "Slime molds form fruiting bodies.", ["slime molds", "mycetozoans"])
v("PRO-05", "plasmodial slime mold", "nấm nhầy hợp bào", "Slime mold whose feeding stage is a plasmodium: a multinucleate mass of cytoplasm without internal membranes.", "The plasmodium of Physarum is yellow.", ["plasmodial slime molds"])
v("PRO-05", "cellular slime mold", "nấm nhầy tế bào", "Slime mold whose separate amoebae aggregate into a slug when food runs out.", "Dictyostelium is a cellular slime mold.", ["cellular slime molds", "Dictyostelium", "slug"])
v("PRO-05", "fruiting body", "thể quả", "A spore-producing structure.", "Slime molds form fruiting bodies.", ["fruiting bodies"])

fc("PRO-05", "fact", "Red alga used for agarose?", "Gracilaria dura.")
fc("PRO-05", "fact", "Four charophyte features shared with land plants?", "Rosette cellulose-synthase complexes; peroxisome enzymes limiting photorespiration loss; similar flagellated sperm; phragmoplast (Chara, Coleochaete).")
fc("PRO-05", "fact", "Plasmodial vs cellular slime molds?", "Plasmodial: multinucleate diploid mass, no membranes, sexual fruiting bodies. Cellular: separate cells aggregate into a slug, keep membranes, asexual fruiting body.")
fc("PRO-05", "fact", "Photorespiration path (lecture)?", "Phosphoglycolate → glycolate → peroxisome (glycine) → mitochondrion (serine) → peroxisome (glycerate) → chloroplast (Calvin cycle).")
