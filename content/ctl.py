from _lib import *

SRC = "4.The Control of Microbial Growth.pptx"

# ---------------------------------------------------------------- CTL-01
unit("CTL-01", "Sterilization vs disinfection; microbial death rate; D-value; efficacy factors", "H", 3, 25, SRC + ": slides 1–8",
"""Một nhà máy đồ hộp phải đảm bảo xác suất còn sót một bào tử *Clostridium botulinum* trong hộp **nhỏ hơn 1 phần tỉ tỉ**. Họ không "diệt sạch" theo cảm tính mà **tính toán**: vi khuẩn chết theo **tỉ lệ cố định** mỗi phút – cứ mỗi **D phút** số sống giảm **10 lần**. Biết D, bạn tính được phải đun bao lâu.""",
("A population of 10^6 bacteria is heated; 90% die every minute. How many survivors remain after 3 minutes?",
 ["0", "10^3", "10^5", "7 × 10^5"], 1,
 "Mỗi phút giảm **1 log** (còn 10 %): 10⁶ → 10⁵ → 10⁴ → **10³**. Vi khuẩn chết theo **tỉ lệ**, không theo số lượng cố định."),
[
("1. Các thuật ngữ (slide 3–4)", """
| Thuật ngữ | Định nghĩa | Ghi chú |
|---|---|---|
| **Sterilization** (tiệt trùng) | **tiêu diệt tất cả** vi sinh vật: **tế bào sinh dưỡng + bào tử** | thường dùng **nhiệt độ cao** (autoclave) |
| **Disinfection** (khử trùng) | **tiêu diệt vi khuẩn gây bệnh** (tế bào sinh dưỡng không tạo bào tử) trên **vật vô tri** | dùng **hóa chất, UV, nước sôi, hơi nước…** |
| **Antisepsis** (sát khuẩn) | khử trùng khi áp dụng **trực tiếp lên mô sống**; hóa chất là **antiseptic** | cồn, iodine lên da |
| Commercial sterilization | xử lý nhiệt đủ diệt bào tử *C. botulinum* trong đồ hộp | [mở rộng] |
| Sanitization | giảm vi sinh vật trên dụng cụ ăn uống tới mức an toàn | [mở rộng] |
| Degerming | loại vi sinh vật cơ học (rửa tay, lau cồn) | [mở rộng] |

Hậu tố: **-cide** = giết (**bactericide, fungicide, virucide, germicide**); **-stasis/-static** = **ức chế** sinh trưởng (bacteriostatic) – bỏ tác nhân thì vi sinh vật mọc lại.
"""),
("2. Tốc độ chết của vi sinh vật (slide 5)", """
- Khi xử lý nhiệt, vi khuẩn thường **chết với tốc độ không đổi (constant rate)** – tức **tỉ lệ chết cố định** mỗi đơn vị thời gian.
- Ví dụ bảng slide (chết 90 %/phút):
| Thời gian (phút) | Số tế bào sống | Số chết trong phút đó | log₁₀ sống |
|---|---|---|---|
| 0 | 1 000 000 | – | 6 |
| 1 | 100 000 | 900 000 | 5 |
| 2 | 10 000 | 90 000 | 4 |
| 3 | 1 000 | 9 000 | 3 |
| 4 | 100 | 900 | 2 |
| 5 | 10 | 90 | 1 |
| 6 | 1 | 9 | 0 |
- Vẽ **log(số sống)** theo thời gian → **đường thẳng** (logarithmic death curve).
"""),
("3. D-value – thời gian giảm thập phân", """
- **D-value (decimal reduction time, DRT)**: **thời gian (phút) ở một nhiệt độ xác định** để **giết 90 %** quần thể (giảm **1 log**).
- Công thức: **t = D × (log N₀ − log N)** hay **log N = log N₀ − t/D**.
- Ví dụ: D₁₂₁ của bào tử *C. botulinum* ≈ **0,2 phút**. Quy tắc **12D** trong đồ hộp: t = 12 × 0,2 = **2,4 phút** ở 121 °C → giảm 10¹² lần.
- Thuật ngữ khác [mở rộng]: **thermal death point (TDP)** – nhiệt độ thấp nhất giết hết trong 10 phút; **thermal death time (TDT)** – thời gian ngắn nhất để giết hết ở một nhiệt độ.
- Mô hình log **không bao giờ đạt đúng 0** → tiệt trùng được định nghĩa bằng **xác suất sống sót** rất nhỏ (ví dụ < 10⁻⁶).
"""),
("4. Các yếu tố ảnh hưởng hiệu quả diệt khuẩn (slide 6–7)", """
1. **Số lượng vi sinh vật**: **càng nhiều** vi sinh vật ban đầu → **càng lâu** mới loại bỏ hết.
2. **Đặc điểm vi sinh vật**:
   - **Bào tử khó diệt hơn** tế bào sinh dưỡng;
   - các tế bào sinh dưỡng khác nhau có **độ nhạy khác nhau** với cùng tác nhân (vd vi khuẩn lao, *Pseudomonas* bền hơn).
3. **Ảnh hưởng của môi trường**:
   - **Chất béo và protein** trong dung dịch có xu hướng **bảo vệ** vi khuẩn (máu, mủ, sữa làm giảm hiệu quả);
   - **pH càng thấp → càng dễ diệt** vi khuẩn (acid tăng hiệu quả nhiệt – thực phẩm chua cần xử lý nhiệt nhẹ hơn).
4. **Thời gian tiếp xúc (time of exposure)**:
   - **Nhiệt độ càng thấp → thời gian tiếp xúc càng dài**;
   - **diệt bào tử cần lâu hơn** tế bào sinh dưỡng.
"""),
("5. Cơ chế tác động của tác nhân (slide 8)", """
| Đích | Cơ chế | Ví dụ tác nhân |
|---|---|---|
| **Màng tế bào** | thay đổi **tính thấm** – phá cấu trúc lipid, protein của màng → rò rỉ chất trong tế bào | cồn, phenol, quats, chlorhexidine |
| **Protein và acid nucleic** | **phá liên kết hóa học** (liên kết H, cộng hóa trị) → biến tính protein, hỏng DNA/RNA | nhiệt, bức xạ, aldehyde, kim loại nặng |
"""),
],
[
("Thực tế: vì sao bệnh viện dặn \"rửa sạch trước khi khử trùng\"", """
Máu, mủ, dịch tiết (**protein, lipid**) **bảo vệ** vi khuẩn và **tiêu hao** hóa chất (chlorine, iodine phản ứng với chất hữu cơ). Rửa sạch trước giúp giảm **tải lượng ban đầu (N₀)** và loại chất bảo vệ → cùng thời gian xử lý đạt nhiều log hơn.
"""),
("Thực phẩm chua cần ít nhiệt hơn", """
Đồ hộp **pH < 4,6** (dưa chua, nước ép cà chua, trái cây) chỉ cần xử lý ~100 °C, vì bào tử *C. botulinum* **không nảy mầm** và vi khuẩn **dễ chết hơn** ở pH thấp. Đồ hộp ít acid (thịt, cá, rau) bắt buộc **121 °C** với 12D.
"""),
],
[
("Key terms", "**Sterilization**: kills **all** microbes including **spores** (usually high heat). **Disinfection**: kills pathogenic vegetative cells on objects (chemicals, UV, boiling water, steam). **Antisepsis**: disinfection of **living tissue**; agent = **antiseptic**. -cide kills; -static inhibits.", "Tiệt trùng diệt cả bào tử; khử trùng thì không."),
("Microbial death rate", "Heated bacteria die at a **constant rate** (a constant fraction per unit time), e.g., 90 % per minute: 10⁶ → 10⁵ → 10⁴… A plot of **log survivors vs time is a straight line**.", "Chết theo tỉ lệ → đường thẳng trên trục log."),
("D-value", "**D** = time at a given temperature to kill **90 %** (1 log). **t = D × (log N₀ − log N)**. 12D for *C. botulinum* spores (D₁₂₁ ≈ 0.2 min) = 2.4 min.", "D = thời gian giảm 1 log."),
("Factors and mechanisms", "More microbes → longer time. **Spores** are harder to kill. **Fats and proteins protect** bacteria; **lower pH** kills more easily. **Lower temperature → longer exposure**. Agents act by **altering membrane permeability** or **damaging proteins and nucleic acids**.", "N₀, loại vi sinh vật, môi trường, thời gian."),
],
["Disinfection kills spores", "Microbes die at a constant number per minute", "Organic matter increases killing", "Log survivors reaches zero"])

q("CTL-01", "recall", 1, "Sterilization is defined as:",
  ["killing pathogenic vegetative cells on objects", "killing all microorganisms, including endospores", "reducing microbes on living tissue", "inhibiting microbial growth without killing"], 1,
  "Slide 3: **tiệt trùng** = giết **tất cả** vi khuẩn (**tế bào sinh dưỡng + bào tử**).",
  ["Đó là disinfection.", "", "Đó là antisepsis.", "Đó là -stasis."], ["sterilization"], "Disinfection kills spores", src=SRC + " slide 3")
q("CTL-01", "recall", 1, "When disinfection is applied directly to living tissue, it is called:",
  ["sterilization", "antisepsis", "pasteurization", "sanitization"], 1,
  "Slide 4: khử trùng trên **mô sống** = **antisepsis**; hóa chất gọi là **antiseptic**.",
  ["Sai.", "", "Xử lý nhiệt thực phẩm.", "Không đúng định nghĩa slide."], ["antisepsis"], src=SRC + " slide 4")
q("CTL-01", "calc", 2, "A suspension contains 10⁸ spores/mL. At 121 °C the D-value is 1.5 min. How long must it be heated to reduce the count to 10² spores/mL?",
  ["6 min", "9 min", "4.5 min", "12 min"], 1,
  "Số log cần giảm = 8 − 2 = **6**. t = D × 6 = 1,5 × 6 = **9 phút**.",
  ["Lấy 6 log × 1 phút.", "", "Tính 3 log.", "Tính 8 log."], ["D-value"],
  steps=["Số log giảm = log N₀ − log N = 8 − 2 = 6", "t = D × số log = 1,5 × 6", "t = 9 phút"])
q("CTL-01", "concept", 2, "Why does a plot of log(number of survivors) versus heating time give a straight line?",
  ["Because a constant number of cells dies each minute", "Because a constant fraction of the surviving cells dies each minute", "Because all cells die at the same moment", "Because spores germinate during heating"], 1,
  "Slide 5: chết theo **tỉ lệ không đổi** → log(sống) giảm tuyến tính theo thời gian.",
  ["Nếu vậy thì đường số tuyệt đối mới thẳng, không phải log.", "", "Sai.", "Không liên quan."], ["microbial death rate"], "Microbes die at a constant number per minute", src=SRC + " slide 5")
q("CTL-01", "not", 2, "Which factor does NOT make microbial killing more difficult or slower?",
  ["A larger initial number of microbes", "The presence of fats and proteins", "The presence of endospores", "A lower pH"], 3,
  "Slide 7: **pH càng thấp → càng dễ diệt**. Nhiều vi sinh vật, chất béo/protein, bào tử đều làm việc diệt khó hơn.",
  ["Làm khó hơn.", "Làm khó hơn.", "Làm khó hơn.", ""], ["pH"], "Organic matter increases killing", src=SRC + " slides 6–7")
q("CTL-01", "concept", 2, "According to the lecture, what happens to the required exposure time when the treatment temperature is lowered?",
  ["It becomes shorter", "It becomes longer", "It does not change", "Spores are killed faster"], 1,
  "Slide 7: **nhiệt độ càng thấp → thời gian tiếp xúc càng dài**.",
  ["Ngược lại.", "", "Sai.", "Sai."], ["time of exposure"])
q("CTL-01", "calc", 3, "The D121 of Clostridium botulinum spores is 0.21 min. How long at 121 °C is a 12D process?",
  ["1.75 min", "2.52 min", "12.21 min", "0.21 min"], 1,
  "12D: t = 12 × 0,21 = **2,52 phút**.",
  ["Chia thay vì nhân.", "", "Cộng thay vì nhân.", "Chỉ 1D."], ["D-value", "12D"],
  steps=["12D = 12 × D", "12 × 0,21 = 2,52 phút"])
q("CTL-01", "recall", 1, "The two major mechanisms by which microbial control agents act are:",
  ["alteration of membrane permeability and damage to proteins and nucleic acids", "stimulating growth and sporulation", "blocking flagella and pili", "increasing osmotic pressure and pH"], 0,
  "Slide 8: **thay đổi tính thấm màng** và **phá protein, acid nucleic** (phá liên kết hóa học).",
  ["", "Sai.", "Sai.", "Chỉ là một vài tác nhân vật lý."], ["mechanism"], pool="mock", src=SRC + " slide 8")
q("CTL-01", "calc", 2, "A product initially contains 10⁵ CFU. Heating at 72 °C (D = 0.5 min) is applied for 2 min. How many CFU are expected to survive?",
  ["10⁴", "10", "10³", "1"], 1,
  "Số log giảm = t/D = 2/0,5 = **4** → 10⁵⁻⁴ = **10 CFU**.",
  ["Chỉ giảm 1 log.", "", "Giảm 2 log.", "Giảm 5 log."], ["D-value"], pool="mock",
  steps=["Số log giảm = t / D = 2 / 0,5 = 4", "log N = 5 − 4 = 1", "N = 10 CFU"])
q("CTL-01", "concept", 2, "Why do hospitals clean instruments to remove blood and tissue before disinfecting them?",
  ["Blood contains antibiotics", "Organic matter such as fats and proteins protects microbes and reduces the agent's effectiveness", "Cleaning sterilizes the instruments", "Disinfectants only work on dry surfaces"], 1,
  "Slide 7: **chất béo và protein bảo vệ vi khuẩn**; rửa còn giảm số lượng ban đầu.",
  ["Sai.", "", "Rửa không phải tiệt trùng.", "Sai."], ["disinfection"], pool="mock")
q("CTL-01", "not", 2, "Which statement about a bacteriostatic agent is NOT correct?",
  ["It inhibits growth", "Growth may resume when the agent is removed", "It kills all spores", "It is different from a bactericide"], 2,
  "-static chỉ **ức chế**; không diệt được bào tử (thậm chí không diệt tế bào sinh dưỡng).",
  ["Đúng.", "Đúng.", "", "Đúng."], ["bacteriostatic"], pool="mock")
q("CTL-01", "data", 2, "A heating experiment gives these survivor counts:\n\nTime (min) | 0     | 2     | 4\nCFU/mL     | 10^7  | 10^5  | 10^3\n\nWhat is the D-value?",
  ["2 min", "1 min", "0.5 min", "4 min"], 1,
  "Mỗi 2 phút giảm 2 log → giảm 1 log mất **1 phút** → D = 1 phút.",
  ["Đó là thời gian giảm 2 log.", "", "Sai.", "Sai."], ["D-value"], pool="mock",
  steps=["Từ 0 → 2 phút: log giảm 7 → 5 = 2 log", "D = 2 phút / 2 log = 1 phút"])

we("WE-01", "CTL-01", "D-value and survivors after heating",
"""A milk sample contains 2 × 10⁶ CFU/mL of a heat-resistant vegetative bacterium. At 65 °C its D-value is 3 min.
(a) How many log reductions are achieved by holding for 15 min?
(b) How many CFU/mL survive?
(c) How long would be needed to reach 1 CFU/mL?""",
[S("Log reductions = t / D = 15 / 3 = ?", 5, hint="Chia thời gian cho D"),
 S("log N₀ = log(2 × 10⁶) = ? (2 decimals)", 6.30, hint="log 2 = 0,30"),
 S("log N = log N₀ − 5 = ?", 1.30),
 S("N = 10^1.30 ≈ ? CFU/mL", 20, hint="10^1,3 ≈ 20"),
 S("Time to reach log N = 0: t = D × (log N₀ − 0) = 3 × 6.30 = ? min", 18.9)],
"(a) 5 log; (b) ≈ 20 CFU/mL; (c) ≈ 18.9 min.",
"Luôn làm việc với **log**: số log giảm = t/D. Nhớ log(2 × 10⁶) = 6,30 chứ không phải 6.")

we("WE-02", "CTL-01", "Designing a 12D canning process",
"""Spores of Clostridium botulinum have D₁₂₁ = 0.25 min. A cannery wants a 12D process.
(a) What holding time at 121 °C is required?
(b) If one can initially contains 10³ spores, what is the expected number of survivors per can after the 12D process?
(c) Out of how many cans would you expect one to contain a surviving spore?""",
[S("Holding time = 12 × D = ? min", 3.0),
 S("log survivors per can = 3 − 12 = ?", -9),
 S("Survivors per can = 10^−9. Expected cans per survivor = 10^? ", 9)],
"(a) 3.0 min; (b) 10⁻⁹ spores per can; (c) about 1 can in 10⁹ (one billion).",
"Mô hình log không đạt 0 → tiệt trùng được hiểu là **xác suất sống sót rất nhỏ**. 10⁻⁹ bào tử/hộp nghĩa là trung bình 1 tỉ hộp có 1 hộp còn bào tử.")

v("CTL-01", "sterilization", "tiệt trùng", "Killing all microorganisms, including endospores.", "Autoclaving is a sterilization method.", ["sterilize", "sterile"])
v("CTL-01", "disinfection", "khử trùng", "Killing pathogenic vegetative microbes on inanimate objects.", "Bleach is used for disinfection.", ["disinfectant", "disinfect"])
v("CTL-01", "antisepsis", "sát khuẩn", "Disinfection of living tissue; the agent is an antiseptic.", "Iodine is used for antisepsis of skin.", ["antiseptic"])
v("CTL-01", "bactericidal", "diệt khuẩn", "Killing bacteria (-cide).", "Alcohol is bactericidal.", ["bactericide", "germicide"])
v("CTL-01", "bacteriostatic", "kìm khuẩn", "Inhibiting bacterial growth without killing (-static).", "Refrigeration is bacteriostatic.", ["bacteriostasis"])
v("CTL-01", "D-value", "giá trị D (thời gian giảm thập phân)", "Time at a given temperature to kill 90% of a population.", "The D-value of spores is longer than that of vegetative cells.", ["decimal reduction time", "D value"])
v("CTL-01", "microbial death rate", "tốc độ chết của vi sinh vật", "The constant fraction of a population killed per unit time.", "The microbial death rate appears as a straight line on a log plot.", ["death curve"])
v("CTL-01", "12D", "quy tắc 12D", "A heat process giving 12 log reductions of C. botulinum spores.", "Low-acid canned foods receive a 12D process.")
v("CTL-01", "time of exposure", "thời gian tiếp xúc", "How long microbes are exposed to a control agent.", "Lower temperatures need a longer time of exposure.")

fc("CTL-01", "fact", "Sterilization vs disinfection vs antisepsis?", "Sterilization: all microbes incl. spores. Disinfection: pathogenic vegetative cells on objects. Antisepsis: disinfection of living tissue.")
fc("CTL-01", "fact", "Four factors affecting killing?", "Number of microbes; microbial characteristics (spores); environment (fats/proteins protect, low pH helps); time of exposure.")
fc("CTL-01", "fact", "Formula linking time, D and logs?", "t = D × (log N₀ − log N).")
fc("CTL-01", "number", "12D time if D121 = 0.2 min?", "2.4 min.")
fc("CTL-01", "trap", "TRUE/FALSE: 90% kill per minute means 900,000 die every minute.", "FALSE – a constant fraction dies; the number killed falls each minute.")

# ---------------------------------------------------------------- CTL-02
unit("CTL-02", "Heat: moist heat, autoclaving, pasteurization and dry heat", "H", 2, 25, SRC + ": slides 9–13",
"""Nồi luộc sữa bình của mẹ đun **100 °C** – đủ an toàn cho em bé. Nhưng phòng thí nghiệm vi sinh bắt buộc dùng **nồi hấp (autoclave) 121 °C**, còn que cấy thì hơ **đỏ rực** trên ngọn lửa. Vì sao 100 °C "chưa đủ", và vì sao **hơi nước** diệt khuẩn tốt hơn **khí nóng khô** ở cùng nhiệt độ?""",
("Why is boiling at 100 °C not a sterilization method?",
 ["It does not kill vegetative bacteria", "Some endospores survive boiling", "Water blocks heat transfer", "Boiling only works for dry objects"], 1,
 "Đun sôi 100 °C diệt tế bào sinh dưỡng, nhiều virus và nấm, nhưng **một số nội bào tử sống sót** → không phải tiệt trùng. Autoclave 121 °C mới diệt được bào tử."),
[
("1. Nhiệt ẩm (moist heat) – slide 9–10", """
**Cơ chế**: phá **liên kết hydro giữa các chuỗi protein** → **đông tụ (coagulate) protein** vi khuẩn. Nước giúp protein đông tụ nhanh → nhiệt ẩm hiệu quả hơn nhiệt khô.

| Phương pháp | Điều kiện | Hiệu quả |
|---|---|---|
| **Boiling** (đun sôi) | 100 °C, 1 atm | diệt tế bào sinh dưỡng, phần lớn virus, nấm; **không diệt chắc chắn bào tử** |
| **Free-flowing steam** (hơi nước không nén) | 100 °C | tương tự đun sôi |
| **Autoclave** (nồi hấp áp lực) | **121 °C**, áp suất dư **~1 atm (15 psi)**, thường **15 phút** | **diệt tế bào sinh dưỡng và bào tử** → **tiệt trùng** |

**Lưu ý autoclave**:
- Hơi nước phải **tiếp xúc trực tiếp với bề mặt** dụng cụ (slide 9) → không nút kín bình, không bọc giấy bạc kín khí, đuổi hết không khí.
- Áp suất chỉ để **nâng nhiệt độ sôi** của nước lên 121 °C; **nhiệt độ** mới là yếu tố diệt khuẩn.
- Bình dung tích lớn cần **thời gian lâu hơn** để tâm dung dịch đạt 121 °C (slide 11 [fig]).
- Kiểm tra bằng **băng chỉ thị nhiệt** hoặc **chỉ thị sinh học** (bào tử *Geobacillus stearothermophilus*). [mở rộng]
"""),
("2. Thanh trùng – pasteurization (slide 12)", """
- **Đun nóng nhẹ**, **đủ để diệt vi sinh vật gây hỏng** (và gây bệnh) mà **không làm ảnh hưởng nghiêm trọng hương vị** sản phẩm.
- **Thanh trùng sữa**:
| Kiểu | Nhiệt độ | Thời gian |
|---|---|---|
| **Truyền thống (LTLT – batch)** | **63 °C** | **30 phút** |
| **HTST** (high temperature short time) | **72 °C** | **15 giây** |
| **UHT** (ultra-high temperature) | **140 °C** | **< 1 giây** (slide); thực tế ~135–150 °C vài giây |

- Các cặp nhiệt độ – thời gian này là **xử lý tương đương (equivalent treatments)**: nhiệt càng cao, thời gian càng ngắn.
- Thanh trùng **không phải tiệt trùng**; riêng UHT + đóng gói vô trùng cho sữa bảo quản nhiệt độ phòng nhiều tháng.
"""),
("3. Nhiệt khô (dry heat) – slide 13", """
**Cơ chế**: **oxy hóa (oxidation)** thành phần tế bào → cần nhiệt độ cao hơn/lâu hơn nhiệt ẩm.
| Phương pháp | Ứng dụng |
|---|---|
| **Direct flaming** (hơ lửa trực tiếp) | tiệt trùng **que cấy (inoculating loop)** – hơ đến đỏ |
| **Incineration** (thiêu đốt) | tiệt trùng và **tiêu hủy** cốc giấy, túi, băng gạc nhiễm bẩn |
| **Hot-air sterilization** (tủ sấy) | **170 °C, 2 giờ** – dụng cụ thủy tinh, kim loại, vật chịu nhiệt không ướt được (bột, dầu) |

So sánh: autoclave 121 °C/15 phút ≈ tủ sấy 170 °C/2 giờ.
"""),
("4. So sánh nhiệt ẩm – nhiệt khô", """
| | Nhiệt ẩm | Nhiệt khô |
|---|---|---|
| Cơ chế | **đông tụ protein** (phá liên kết H) | **oxy hóa** |
| Điều kiện tiệt trùng | 121 °C, 15 phút | 170 °C, 2 giờ |
| Truyền nhiệt | nhanh (hơi nước ngưng tụ) | chậm |
| Dùng cho | môi trường, dung dịch, dụng cụ chịu ẩm | thủy tinh, kim loại, bột, dầu; que cấy |
"""),
],
[
("Thực tế phòng lab CH3004", """
Bạn sẽ **hấp môi trường 121 °C/15–20 phút**, **sấy dụng cụ thủy tinh 160–170 °C/2 giờ**, **hơ que cấy đến đỏ** trước và sau mỗi lần cấy. Môi trường có đường dễ bị **caramel hóa** nếu hấp quá lâu; dung dịch chịu nhiệt kém (vitamin, kháng sinh) thì **lọc vô trùng** (CTL-03).
"""),
("Công nghiệp sữa Việt Nam", """
Sữa tươi thanh trùng (HTST 72–75 °C/15–20 s) phải giữ lạnh, hạn ~7–10 ngày; sữa UHT (~140 °C/2–4 s + đóng hộp giấy vô trùng) để 6–12 tháng ở nhiệt độ phòng. Thanh trùng còn diệt *Mycobacterium bovis, Coxiella burnetii, Listeria*, *Salmonella*.
"""),
],
[
("Moist heat", "Moist heat breaks **hydrogen bonds** and **coagulates proteins**. **Boiling** (100 °C) and free-flowing steam do not reliably kill endospores. **Autoclave**: **121 °C**, ~1 atm above atmospheric (15 psi), ~15 min, kills vegetative cells **and spores**; steam must **contact the surfaces**.", "Autoclave 121 °C diệt cả bào tử."),
("Pasteurization", "Mild heating that kills spoilage organisms without seriously damaging taste. Milk: **63 °C for 30 min** (traditional), **HTST 72 °C for 15 s**, **UHT 140 °C for < 1 s**. Not sterilization.", "63/30 – 72/15 s – 140/<1 s."),
("Dry heat", "Kills by **oxidation**. **Direct flaming** (inoculating loops), **incineration** (contaminated paper, dressings), **hot-air oven 170 °C for 2 h**.", "Nhiệt khô: oxy hóa; tủ sấy 170 °C 2 h."),
],
["Boiling sterilizes", "Pressure kills microbes in the autoclave", "Dry heat coagulates proteins", "Pasteurization equals sterilization"])

q("CTL-02", "recall", 1, "Standard autoclave conditions given in the lecture are:",
  ["100 °C at normal pressure", "121 °C with about 1 atm of extra pressure", "170 °C for 2 hours", "72 °C for 15 seconds"], 1,
  "Slide 9: **autoclave 121 °C, 1 atm** (áp suất dư ~15 psi) → diệt tế bào sinh dưỡng **và bào tử**.",
  ["Đó là đun sôi.", "", "Đó là tủ sấy khô.", "Đó là HTST."], ["autoclave"], "Boiling sterilizes", src=SRC + " slide 9")
q("CTL-02", "concept", 2, "Moist heat kills microbes mainly by:",
  ["oxidation of cell components", "breaking hydrogen bonds and coagulating proteins", "forming thymine dimers", "dissolving the cell wall"], 1,
  "Slide 9: nhiệt ẩm **phá liên kết hydro giữa các chuỗi protein → đông tụ protein**. Nhiệt khô mới oxy hóa.",
  ["Nhiệt khô.", "", "UV.", "Sai."], ["moist heat"], "Dry heat coagulates proteins", src=SRC + " slide 9")
q("CTL-02", "recall", 1, "HTST pasteurization of milk uses:",
  ["63 °C for 30 min", "72 °C for 15 s", "140 °C for < 1 s", "121 °C for 15 min"], 1,
  "Slide 12: **HTST = 72 °C, 15 giây**. Truyền thống 63 °C/30 phút; UHT 140 °C/<1 giây.",
  ["Truyền thống.", "", "UHT.", "Autoclave."], ["HTST", "pasteurization"], src=SRC + " slide 12")
q("CTL-02", "recall", 1, "Hot-air (dry heat) sterilization in an oven requires, according to the lecture:",
  ["121 °C for 15 min", "170 °C for 2 hours", "100 °C for 10 min", "63 °C for 30 min"], 1,
  "Slide 13: **tủ sấy 170 °C, 2 giờ**.",
  ["Autoclave.", "", "Đun sôi.", "Thanh trùng."], ["dry heat"], src=SRC + " slide 13")
q("CTL-02", "application", 2, "An autoclave reaches 121 °C, but a tightly sealed empty flask inside is not sterile afterwards. The most likely reason is:",
  ["121 °C cannot kill spores", "Steam could not contact the inside surfaces of the sealed flask", "The pressure was too high", "Autoclaves only work on liquids"], 1,
  "Slide 9: hơi nước **phải tiếp xúc với bề mặt**. Bình kín chứa không khí khô → bên trong thực chất là nhiệt khô 121 °C, không đủ.",
  ["121 °C với hơi ẩm diệt được bào tử.", "", "Sai.", "Sai."], ["autoclave"])
q("CTL-02", "not", 2, "Which is NOT a dry heat method?",
  ["Direct flaming of an inoculating loop", "Incineration of contaminated dressings", "Hot-air oven at 170 °C", "Autoclaving at 121 °C"], 3,
  "**Autoclave** dùng **hơi nước** – nhiệt ẩm.",
  ["Nhiệt khô.", "Nhiệt khô.", "Nhiệt khô.", ""], ["dry heat", "autoclave"])
q("CTL-02", "concept", 2, "In an autoclave, what is the role of the increased pressure?",
  ["Pressure itself crushes the microbes", "It raises the boiling point of water so steam reaches 121 °C", "It removes oxygen to kill aerobes", "It dries the instruments"], 1,
  "Áp suất cao **nâng nhiệt độ sôi** của nước lên 121 °C; **nhiệt độ** mới là yếu tố diệt.",
  ["Sai.", "", "Sai.", "Sai."], ["autoclave"], "Pressure kills microbes in the autoclave")
q("CTL-02", "concept", 2, "Pasteurization is designed to:",
  ["kill all microbes including spores", "kill organisms causing spoilage or disease without seriously damaging the taste of the product", "oxidize cell components", "remove microbes by filtration"], 1,
  "Slide 12: đun nóng nhẹ, đủ diệt vi sinh vật gây hỏng mà không làm hỏng hương vị.",
  ["Đó là tiệt trùng.", "", "Nhiệt khô.", "Lọc."], ["pasteurization"], "Pasteurization equals sterilization", pool="mock")
q("CTL-02", "recall", 1, "Dry heat kills microorganisms by:",
  ["coagulation of proteins through hydrogen bond breakage", "oxidation effects", "forming pyrimidine dimers", "osmotic lysis"], 1,
  "Slide 13: nhiệt khô giết vi sinh vật bằng **oxy hóa**.",
  ["Nhiệt ẩm.", "", "UV.", "Áp suất thẩm thấu."], ["dry heat"], pool="mock")
q("CTL-02", "application", 2, "Which method is most suitable for sterilizing an inoculating loop between transfers?",
  ["Autoclaving for 15 min", "Direct flaming until red hot", "Pasteurization", "UV light for 1 h"], 1,
  "Slide 13: **hơ lửa trực tiếp** tiệt trùng que cấy – nhanh, tiện.",
  ["Quá chậm giữa các lần cấy.", "", "Không tiệt trùng.", "Không cần thiết, kém hiệu quả."], ["direct flaming"], pool="mock")
q("CTL-02", "not", 2, "Which statement about boiling (100 °C) is NOT correct?",
  ["It kills most vegetative bacteria", "It is a reliable sterilization method for endospores", "It is a moist heat method", "It kills many viruses and fungi"], 1,
  "Đun sôi **không** diệt chắc chắn nội bào tử → không phải tiệt trùng.",
  ["Đúng.", "", "Đúng.", "Đúng."], ["boiling"], pool="mock")

v("CTL-02", "moist heat", "nhiệt ẩm", "Heat with water or steam; kills by coagulating proteins.", "Autoclaving uses moist heat.")
v("CTL-02", "autoclave", "nồi hấp áp lực (autoclave)", "A device using steam under pressure at 121 °C to sterilize.", "Media are sterilized in an autoclave.", ["autoclaving"])
v("CTL-02", "boiling", "đun sôi", "Heating in water at 100 °C; not reliable against endospores.", "Boiling kills most vegetative cells.")
v("CTL-02", "HTST", "thanh trùng nhiệt độ cao thời gian ngắn", "High temperature short time pasteurization: 72 °C for 15 s.", "Most milk is HTST pasteurized.", ["UHT", "ultra-high temperature"])
v("CTL-02", "dry heat", "nhiệt khô", "Heat without moisture; kills by oxidation.", "Glassware is sterilized with dry heat.", ["hot-air sterilization"])
v("CTL-02", "incineration", "thiêu đốt", "Burning to sterilize and dispose of contaminated materials.", "Used dressings are destroyed by incineration.")
v("CTL-02", "direct flaming", "hơ lửa trực tiếp", "Heating an object in a flame until red hot.", "Inoculating loops are sterilized by direct flaming.")
v("CTL-02", "inoculating loop", "que cấy vòng", "A wire loop used to transfer microbes.", "Flame the inoculating loop before use.")
v("CTL-02", "coagulate", "đông tụ", "To denature and clump proteins.", "Moist heat coagulates bacterial proteins.", ["coagulation"])

fc("CTL-02", "number", "Autoclave conditions?", "121 °C, ~1 atm (15 psi) above atmospheric, ~15 min.")
fc("CTL-02", "number", "Three milk pasteurization regimes?", "63 °C/30 min; HTST 72 °C/15 s; UHT 140 °C/<1 s.")
fc("CTL-02", "number", "Hot-air oven sterilization?", "170 °C for 2 hours.")
fc("CTL-02", "fact", "Moist vs dry heat mechanisms?", "Moist: breaks H-bonds, coagulates proteins. Dry: oxidation.")
fc("CTL-02", "trap", "TRUE/FALSE: autoclave pressure is what kills the microbes.", "FALSE – pressure raises the steam temperature to 121 °C.")

# ---------------------------------------------------------------- CTL-03
unit("CTL-03", "Filtration, low temperature, desiccation, osmotic pressure and radiation", "H", 2, 20, SRC + ": slides 14–26",
"""Vaccine, enzyme và dung dịch kháng sinh sẽ **hỏng** nếu đem hấp 121 °C. Vậy làm sao làm chúng vô trùng? Câu trả lời: **lọc** qua màng có lỗ **0,22 μm** – nhỏ hơn vi khuẩn. Còn bơm kim tiêm nhựa dùng một lần thì được tiệt trùng bằng **chùm electron** ngay trong bao bì kín. Mỗi tác nhân vật lý có một "sở trường" riêng.""",
("Which method is best for sterilizing a heat-sensitive antibiotic solution?",
 ["Autoclaving", "Filtration through a membrane filter", "Hot-air oven", "Boiling"], 1,
 "Slide 20: **lọc** dùng để tiệt trùng vật liệu **nhạy nhiệt**: một số môi trường, enzyme, vaccine, dung dịch kháng sinh."),
[
("1. Lọc – filtration (slide 14–20)", """
- **Filtration**: cho chất lỏng hoặc khí đi qua vật liệu dạng **màng/lưới** có **lỗ đủ nhỏ để giữ vi sinh vật**.
- Dùng để tiệt trùng vật liệu **nhạy nhiệt**: **một số môi trường nuôi cấy, enzyme, vaccine, dung dịch kháng sinh**.
- Có nhiều loại màng với **kích thước lỗ khác nhau** cho các mục đích khác nhau:
| Lỗ màng | Giữ lại |
|---|---|
| **0,22–0,45 μm** | vi khuẩn (0,22 μm dùng cho lọc vô trùng) |
| ~0,01 μm (siêu lọc) | virus, một số protein lớn |
| **HEPA** (hiệu suất cao, ~0,3 μm) | vi sinh vật trong **không khí** (tủ an toàn sinh học, phòng mổ) [fig] |
- Vi sinh vật bị giữ **trên màng vẫn còn sống** → lọc cũng dùng để **định lượng** vi sinh vật trong nước (màng lọc đặt lên thạch – GRO-06).
"""),
("2. Nhiệt độ thấp, làm khô và áp suất thẩm thấu (slide 21–22)", """
- **Lạnh (refrigeration 4 °C) / đông lạnh**: **kìm khuẩn (bacteriostatic)** – làm chậm trao đổi chất, **không** diệt; vi khuẩn ưa lạnh (*Listeria*) vẫn mọc chậm. [mở rộng]
- **Desiccation (làm khô)**: mất nước → vi khuẩn **không sinh trưởng, không sinh sản** được nhưng **vẫn sống nhiều năm**. Khi có nước trở lại, chúng **tiếp tục sinh trưởng và phân chia** → đây là nguyên lý của **đông khô (lyophilization / freeze-drying)** để **bảo quản** giống.
- **Osmotic pressure (áp suất thẩm thấu)**: tạo môi trường **ưu trương** (muối, đường) → nước rời tế bào (**co nguyên sinh**) → ức chế sinh trưởng (ướp muối, mứt).
"""),
("3. Bức xạ – radiation (slide 23–26)", """
Tác dụng phụ thuộc **bước sóng, cường độ, thời gian chiếu**.

**a) Bức xạ ion hóa (ionizing radiation)**: **tia gamma, tia X, chùm electron năng lượng cao**.
- Bước sóng **< 1 nm** → mang **nhiều năng lượng** → **xuyên sâu**.
- **Ion hóa phân tử nước thành gốc tự do hoạt động** (vd gốc hydroxyl •OH) → phản ứng với thành phần hữu cơ, **đặc biệt DNA**.
- **Chùm electron** được dùng rộng rãi để **tiệt trùng dược phẩm và dụng cụ y tế dùng một lần** (bơm kim tiêm, găng tay). Tia gamma chiếu xạ thực phẩm, gia vị. [mở rộng]

**b) Bức xạ không ion hóa (nonionizing radiation)**:
- Bước sóng **> 1 nm**; **không xuyên sâu** → cần **chiếu trực tiếp**.
- **Tia UV**: DNA hấp thụ mạnh ở **260 nm**; tạo **liên kết giữa hai thymine kề nhau (thymine dimers)** → DNA **sao chép sai**. Dùng khử trùng không khí, bề mặt (tủ cấy), **vaccine và các sản phẩm y tế khác**.
- **Vi sóng (microwaves)**: diệt vi khuẩn gây bệnh chủ yếu **bằng nhiệt** sinh ra trong thực phẩm; nhiệt không đều → có "điểm lạnh".

| | Ion hóa | UV |
|---|---|---|
| Bước sóng | < 1 nm | > 1 nm (UV diệt khuẩn ~260 nm) |
| Năng lượng/xuyên thấu | cao, **xuyên sâu** | thấp hơn, **kém xuyên** |
| Cơ chế | gốc tự do từ nước → hỏng DNA | **dimer thymine** |
| Ứng dụng | tiệt trùng dụng cụ nhựa, dược phẩm trong bao bì | khử trùng bề mặt, không khí tủ cấy |
"""),
],
[
("Tủ cấy vô trùng và tủ an toàn sinh học", """
Tủ cấy trong lab có **đèn UV** (bật 15–30 phút trước khi làm, tắt khi thao tác vì UV hại mắt, da) và **màng HEPA** lọc không khí thổi xuống bề mặt. UV **không xuyên qua** kính, nhựa, lớp bụi → vật bị che vẫn có thể nhiễm.
"""),
("Chiếu xạ thực phẩm ở Việt Nam", """
Trái cây xuất khẩu (thanh long, nhãn, vải) sang Mỹ, Úc được **chiếu xạ gamma/electron** liều thấp để diệt côn trùng và giảm vi sinh vật – đây là "tiệt trùng lạnh", thực phẩm **không trở nên phóng xạ**.
"""),
],
[
("Filtration", "Passage of liquid or gas through a screen-like material with pores small enough to retain microbes. Used for **heat-sensitive materials**: some **culture media, enzymes, vaccines, antibiotic solutions**. Different membranes have different pore sizes (0.22 μm for bacteria; HEPA for air).", "Lọc tiệt trùng vật liệu nhạy nhiệt."),
("Desiccation and osmotic pressure", "**Desiccation**: bacteria cannot grow but remain **viable for years**; they resume growth when water returns → principle of **lyophilization (freeze-drying)**. **Hypertonic** environments (salt, sugar) cause plasmolysis.", "Làm khô: ức chế chứ không giết."),
("Radiation", "**Ionizing** (gamma, X-rays, electron beams; λ < 1 nm; high energy; penetrates deeply) ionizes water into **free radicals** that damage DNA; electron beams sterilize pharmaceuticals and disposable medical devices. **Nonionizing** (λ > 1 nm; poor penetration): **UV at 260 nm** forms **thymine dimers**; **microwaves** kill by heating.", "Ion hóa: gốc tự do, xuyên sâu. UV: dimer thymine, kém xuyên."),
],
["Filtration kills microbes", "UV penetrates deeply", "Desiccation kills bacteria", "Refrigeration sterilizes"])

q("CTL-03", "recall", 1, "Filtration is used to sterilize which of the following?",
  ["Glassware", "Heat-sensitive solutions such as vaccines, enzymes and antibiotic solutions", "Contaminated dressings", "Inoculating loops"], 1,
  "Slide 20: lọc dùng cho vật liệu **nhạy nhiệt**: một số môi trường, **enzyme, vaccine, dung dịch kháng sinh**.",
  ["Tủ sấy.", "", "Thiêu đốt.", "Hơ lửa."], ["filtration"], src=SRC + " slide 20")
q("CTL-03", "concept", 2, "UV light is effective at about 260 nm because:",
  ["it penetrates deeply into materials", "DNA strongly absorbs it, forming bonds between adjacent thymines", "it heats water", "it ionizes water into free radicals"], 1,
  "Slide 26: UV được **DNA hấp thụ mạnh ở 260 nm**, tạo **dimer thymine** → DNA sao chép sai.",
  ["UV kém xuyên.", "", "Vi sóng.", "Bức xạ ion hóa."], ["UV", "thymine dimer"], "UV penetrates deeply", src=SRC + " slide 26")
q("CTL-03", "concept", 2, "Why are electron beams, rather than UV, used to sterilize disposable syringes inside sealed packages?",
  ["Electron beams are nonionizing", "Ionizing radiation carries more energy and penetrates deeply", "UV is too expensive", "Electron beams work by heating"], 1,
  "Bức xạ ion hóa bước sóng < 1 nm, **năng lượng cao, xuyên sâu** qua bao bì; UV **không xuyên** qua nhựa.",
  ["Sai: chùm electron là ion hóa.", "", "Không phải lý do.", "Sai."], ["ionizing radiation"], src=SRC + " slides 24–25")
q("CTL-03", "concept", 2, "Ionizing radiation kills cells mainly by:",
  ["forming thymine dimers only", "ionizing water into reactive free radicals that damage organic components, especially DNA", "dehydrating cells", "coagulating proteins by heat"], 1,
  "Slide 25: **ion hóa nước → gốc tự do** → phản ứng với thành phần hữu cơ, **đặc biệt DNA**.",
  ["Đó là UV.", "", "Sai.", "Sai."], ["ionizing radiation", "free radical"])
q("CTL-03", "concept", 2, "The principle that desiccated bacteria remain viable and resume growth when water is added underlies:",
  ["pasteurization", "lyophilization (freeze-drying)", "autoclaving", "incineration"], 1,
  "Slide 21: làm khô → không sinh trưởng nhưng **vẫn sống** → nguyên lý **đông khô** để bảo quản.",
  ["Sai.", "", "Sai.", "Sai."], ["desiccation", "lyophilization"], "Desiccation kills bacteria", src=SRC + " slide 21")
q("CTL-03", "not", 2, "Which statement about nonionizing radiation is NOT correct?",
  ["Its wavelength is longer than 1 nm", "It penetrates poorly, so direct exposure is needed", "UV is an example", "It is used to sterilize drugs inside sealed containers"], 3,
  "Tiệt trùng trong bao bì kín cần bức xạ **ion hóa** (xuyên sâu). Bức xạ không ion hóa **kém xuyên**.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["nonionizing radiation"])
q("CTL-03", "concept", 2, "Microwaves kill pathogenic bacteria in food mainly by:",
  ["forming thymine dimers", "producing heat", "ionizing DNA directly", "osmotic lysis"], 1,
  "Vi sóng diệt khuẩn chủ yếu nhờ **nhiệt** sinh ra; nhiệt không đều nên có điểm lạnh.",
  ["UV.", "", "Bức xạ ion hóa.", "Sai."], ["microwaves"], pool="mock")
q("CTL-03", "application", 2, "Bacteria collected on a membrane filter from 100 mL of water are placed on agar and form colonies. What does this show about filtration?",
  ["Filtration kills bacteria", "Filtration removes bacteria but does not necessarily kill them", "Filtration only removes viruses", "Membrane filters dissolve bacteria"], 1,
  "Lọc **giữ lại** vi sinh vật; chúng **vẫn sống** trên màng → dùng được để đếm.",
  ["Sai.", "", "Sai.", "Sai."], ["filtration"], "Filtration kills microbes", pool="mock")
q("CTL-03", "recall", 1, "Ionizing radiation has a wavelength of:",
  ["greater than 1 nm", "less than about 1 nm", "exactly 260 nm", "greater than 1 m"], 1,
  "Slide 24: bức xạ ion hóa **< ~1 nm** → năng lượng cao.",
  ["Đó là không ion hóa.", "", "UV diệt khuẩn.", "Sóng radio."], ["ionizing radiation"], pool="mock")
q("CTL-03", "concept", 2, "Salting fish controls microbial growth mainly through:",
  ["ionizing radiation", "high osmotic pressure causing water loss from cells", "low temperature", "UV damage"], 1,
  "Slide 22: tạo môi trường **ưu trương** → nước rời tế bào → co nguyên sinh.",
  ["Sai.", "", "Sai.", "Sai."], ["osmotic pressure"], pool="mock")

v("CTL-03", "filtration", "lọc", "Passing a liquid or gas through a material with pores small enough to retain microbes.", "Vaccines are sterilized by filtration.", ["membrane filter", "filter"])
v("CTL-03", "HEPA filter", "màng lọc HEPA", "High-efficiency particulate air filter that removes microbes from air.", "Biosafety cabinets use HEPA filters.", ["HEPA"])
v("CTL-03", "desiccation", "làm khô", "Removal of water; inhibits growth but may not kill.", "Desiccation keeps bacteria dormant.")
v("CTL-03", "lyophilization", "đông khô", "Freeze-drying: rapid freezing followed by removal of water under vacuum.", "Cultures are preserved by lyophilization.", ["freeze-drying"])
v("CTL-03", "osmotic pressure", "áp suất thẩm thấu", "The force drawing water across a membrane toward higher solute.", "High osmotic pressure preserves jam.")
v("CTL-03", "ionizing radiation", "bức xạ ion hóa", "Gamma rays, X-rays, electron beams (λ < 1 nm) that ionize water.", "Ionizing radiation sterilizes medical devices.", ["gamma rays", "electron beams"])
v("CTL-03", "nonionizing radiation", "bức xạ không ion hóa", "Radiation with λ > 1 nm such as UV; poor penetration.", "UV is nonionizing radiation.")
v("CTL-03", "UV", "tia cực tím", "Ultraviolet light; at 260 nm it forms thymine dimers in DNA.", "UV lamps disinfect biosafety cabinets.", ["ultraviolet"])
v("CTL-03", "thymine dimer", "dimer thymine", "A covalent bond between adjacent thymines caused by UV.", "Thymine dimers block DNA replication.", ["thymine dimers"])
v("CTL-03", "free radical", "gốc tự do", "A highly reactive molecule with an unpaired electron.", "Radiation creates free radicals from water.", ["free radicals", "hydroxyl radical"])

fc("CTL-03", "fact", "What is filtration used for (4 examples)?", "Heat-sensitive materials: some culture media, enzymes, vaccines, antibiotic solutions.")
fc("CTL-03", "fact", "Ionizing radiation: examples, λ, mechanism?", "Gamma, X-rays, electron beams; <1 nm; ionize water into free radicals that damage DNA.")
fc("CTL-03", "number", "UV wavelength most absorbed by DNA?", "260 nm → thymine dimers.")
fc("CTL-03", "trap", "TRUE/FALSE: desiccation kills bacteria.", "FALSE – they stay viable; this is the basis of lyophilization.")

# ---------------------------------------------------------------- CTL-04
unit("CTL-04", "Chemical agents I: phenolics, chlorhexidine, essential oils, halogens, alcohols, heavy metals", "H", 2, 25, SRC + ": slides 27–36",
"""Trước khi tiêm, y tá lau da bằng **cồn 70 %**; sau mổ, vết thương được bôi **Betadine** (iodine); nước máy có mùi **chlorine**; bạc được thêm vào băng gạc chữa bỏng. Mỗi hóa chất đánh vào một "điểm yếu" khác nhau của tế bào vi khuẩn. Và vì sao cồn **70 %** lại diệt khuẩn tốt hơn cồn **100 %**?""",
("Why is 70% ethanol a better disinfectant than 100% ethanol?",
 ["100% ethanol evaporates too slowly", "Water is required for alcohol to denature proteins", "70% ethanol kills endospores", "100% ethanol is an antibiotic"], 1,
 "Slide 34: cồn **biến tính protein – quá trình cần nước**. Cồn tuyệt đối làm đông tụ nhanh lớp ngoài và bay hơi, kém hiệu quả hơn."),
[
("1. Phenol và phenolics (slide 28–30)", """
- **Phenol** (carbolic acid – Lister dùng năm 1867) và **O-phenylphenol** **phá màng sinh chất chứa lipid** → **mất các thành phần tế bào chất**.
- Phenolics vẫn hiệu quả khi có **chất hữu cơ**; dùng khử trùng bề mặt (Lysol). [mở rộng]
- **Triclosan** (bisphenol): **ức chế enzyme tổng hợp lipid** của màng sinh chất; từng có trong xà phòng, kem đánh răng.
- ⚠ ***Pseudomonas aeruginosa* kháng triclosan**.
"""),
("2. Chlorhexidine và tinh dầu (slide 31–32)", """
- **Chlorhexidine** (biguanide): **can thiệp cấu trúc màng**. Dùng rửa tay phẫu thuật, nước súc miệng, sát khuẩn da.
- **Essential oils (tinh dầu)**: **hỗn hợp hydrocarbon chiết từ thực vật** – bạc hà, thông, cam, tràm (cajeput)…
  - Tác dụng kháng khuẩn chủ yếu nhờ **phenolics (carvacrol)** và **terpenes (limonene)**.
"""),
("3. Halogens: iodine và chlorine (slide 33–34)", """
**Iodine (I₂)**:
- **Làm suy yếu tổng hợp protein** và **thay đổi màng tế bào** – có lẽ bằng cách tạo **phức với amino acid và acid béo không no**.
- Chế phẩm thương mại phổ biến **Betadine®** là **povidone-iodine**: **iodophor** = iodine + phân tử hữu cơ (polymer **N-vinylpyrrolidone**) giải phóng iodine **từ từ**, **cải thiện khả năng thấm ướt** và là **nguồn dự trữ iodine tự do**.
- Dùng chủ yếu **sát khuẩn da và điều trị vết thương**.

**Chlorine (Cl₂)**:
- Trong nước tạo **acid hypochlorous (HOCl)** – **chất oxy hóa mạnh** → **phá hủy hệ thống enzyme** của tế bào.
- Dùng xử lý nước uống, bể bơi, nước Javel (NaOCl) khử trùng bề mặt. Hiệu quả giảm khi có chất hữu cơ và pH cao. [mở rộng]
"""),
("4. Cồn – alcohols (slide 34)", """
- **Ethanol, isopropanol**.
- **Diệt vi khuẩn (và nấm)** nhưng **không diệt nội bào tử** (và **virus không vỏ**).
- Cơ chế: **biến tính protein (cần nước)**, **đục thủng màng sinh chất** và **hòa tan lipid màng**.
- Nồng độ tối ưu **60–90 %** (thường 70 %). [mở rộng]
- Ưu điểm: bay hơi nhanh, không để lại cặn. Nhược: không diệt bào tử, hiệu quả kém khi có nhiều chất hữu cơ.
"""),
("5. Kim loại nặng – heavy metals (slide 35–36)", """
- **Ag, Hg, Cu** và hợp chất của chúng.
- **Ion kim loại nặng tương tác với nhóm sulfhydryl (–SH) của protein** → **biến tính protein**.
- Hiệu ứng **oligodynamic**: lượng rất nhỏ cũng có tác dụng. Ứng dụng: bạc nitrat nhỏ mắt trẻ sơ sinh (trước đây), băng gạc chứa bạc, CuSO₄ diệt tảo trong bể nước. [mở rộng]
"""),
("6. Bảng tóm tắt", """
| Tác nhân | Đích chính | Ghi nhớ |
|---|---|---|
| Phenol, O-phenylphenol | **màng** chứa lipid | Lister |
| Triclosan | **enzyme tổng hợp lipid** | *P. aeruginosa* kháng |
| Chlorhexidine | **màng** | súc miệng, rửa tay mổ |
| Tinh dầu | carvacrol (phenolic), limonene (terpene) | tự nhiên |
| Iodine / povidone-iodine | **tổng hợp protein + màng** (phức với aa, acid béo không no) | Betadine – da, vết thương |
| Chlorine (HOCl) | **oxy hóa** hệ enzyme | nước uống |
| Cồn | **biến tính protein (cần nước)** + hòa tan lipid màng | không diệt bào tử |
| Ag, Hg, Cu | nhóm **–SH** của protein | oligodynamic |
"""),
],
[
("Thực tế: dung dịch rửa tay khô", """
WHO khuyến nghị dung dịch rửa tay chứa **ethanol ~80 %** hoặc **isopropanol ~75 %** – đủ nước để biến tính protein. Rửa tay khô **không** diệt được bào tử *Clostridioides difficile* và kém với norovirus (virus không vỏ) → khi chăm bệnh nhân tiêu chảy phải rửa tay bằng **xà phòng và nước** (loại bỏ cơ học).
"""),
("Kháng hóa chất", """
Triclosan bị FDA hạn chế trong xà phòng (2016) vì lo ngại **chọn lọc vi khuẩn kháng** và thiếu lợi ích so với xà phòng thường. Đây là ví dụ vì sao "diệt khuẩn 99,9 %" không phải lúc nào cũng tốt.
"""),
],
[
("Phenolics and chlorhexidine", "**Phenol** and **O-phenylphenol** damage the lipid-containing plasma membrane → loss of cytoplasmic contents. **Triclosan** inhibits a **lipid-synthesis enzyme**; ***Pseudomonas aeruginosa* is resistant**. **Chlorhexidine** interferes with membrane structure. **Essential oils** act through **phenolics (carvacrol)** and **terpenes (limonene)**.", "Phenol phá màng; triclosan chặn tổng hợp lipid."),
("Halogens", "**Iodine** impairs protein synthesis and alters membranes (complexes with amino acids and unsaturated fatty acids). **Betadine = povidone-iodine**, an **iodophor** releasing iodine slowly; used for skin and wounds. **Chlorine** forms **HOCl**, a strong oxidizer that damages enzyme systems.", "Iodophor giải phóng iodine từ từ; HOCl oxy hóa."),
("Alcohols and heavy metals", "**Ethanol, isopropanol** kill bacteria and fungi but **not endospores** (or non-enveloped viruses); they **denature proteins (requires water)** and dissolve membrane lipids. **Heavy metals (Ag, Hg, Cu)** bind **sulfhydryl (–SH) groups** → protein denaturation.", "Cồn cần nước; kim loại nặng gắn –SH."),
],
["Alcohol kills endospores", "Triclosan works on Pseudomonas aeruginosa", "Pure alcohol works better than 70%", "Iodophors release iodine all at once"])

q("CTL-04", "recall", 1, "Which bacterium does the lecture specifically mention as resistant to triclosan?",
  ["Staphylococcus aureus", "Pseudomonas aeruginosa", "Escherichia coli", "Bacillus subtilis"], 1,
  "Slide 30: **! *Pseudomonas aeruginosa* kháng triclosan**.",
  ["Không được nêu.", "", "Không được nêu.", "Không được nêu."], ["triclosan"], "Triclosan works on Pseudomonas aeruginosa", src=SRC + " slide 30")
q("CTL-04", "concept", 2, "Triclosan acts by:",
  ["denaturing proteins through –SH binding", "inhibiting an enzyme of plasma membrane lipid biosynthesis", "forming HOCl", "cross-linking proteins"], 1,
  "Slide 30: triclosan **ức chế enzyme tổng hợp lipid** của màng sinh chất.",
  ["Kim loại nặng.", "", "Chlorine.", "Aldehyde."], ["triclosan"], src=SRC + " slide 30")
q("CTL-04", "concept", 2, "Betadine (povidone-iodine) is an iodophor. What is the advantage of an iodophor?",
  ["It releases iodine slowly, improves wetting and acts as a reservoir of free iodine", "It kills all endospores instantly", "It is a heavy metal", "It contains chlorine"], 0,
  "Slide 33: iodophor (iodine + polymer N-vinylpyrrolidone) **giải phóng iodine từ từ**, **tăng thấm ướt**, **dự trữ iodine tự do**.",
  ["", "Sai.", "Sai.", "Sai."], ["iodophor", "povidone-iodine"], "Iodophors release iodine all at once", src=SRC + " slide 33")
q("CTL-04", "recall", 1, "Chlorine disinfects water because it forms:",
  ["iodophors", "hypochlorous acid (HOCl), a strong oxidizing agent", "thymine dimers", "quaternary ammonium ions"], 1,
  "Slide 34: Cl₂ tạo **HOCl** – **chất oxy hóa mạnh** phá hệ enzyme.",
  ["Iodine.", "", "UV.", "Quats."], ["chlorine", "hypochlorous acid"], src=SRC + " slide 34")
q("CTL-04", "not", 2, "Which statement about alcohols (ethanol, isopropanol) is NOT correct?",
  ["They kill bacteria and fungi", "They denature proteins, which requires water", "They dissolve membrane lipids", "They reliably kill endospores"], 3,
  "Slide 34: cồn **không diệt nội bào tử** (và virus không vỏ).",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["alcohol"], "Alcohol kills endospores", src=SRC + " slide 34")
q("CTL-04", "concept", 2, "Heavy metal ions such as Ag+, Hg2+ and Cu2+ kill microbes by:",
  ["oxidizing DNA with UV", "binding sulfhydryl (–SH) groups of proteins, causing denaturation", "dissolving the cell wall", "forming thymine dimers"], 1,
  "Slide 35: ion kim loại nặng **tương tác nhóm –SH** của protein → biến tính.",
  ["Sai.", "", "Sai.", "Sai."], ["heavy metals", "sulfhydryl group"], src=SRC + " slide 35")
q("CTL-04", "recall", 1, "The antimicrobial action of essential oils is mainly due to:",
  ["heavy metals", "phenolics (carvacrol) and terpenes (limonene)", "chlorine", "aldehydes"], 1,
  "Slide 32: nhờ **phenolics (carvacrol)** và **terpenes (limonene)**.",
  ["Sai.", "", "Sai.", "Sai."], ["essential oils"], src=SRC + " slide 32")
q("CTL-04", "recall", 1, "Phenol and O-phenylphenol kill bacteria mainly by:",
  ["damaging the lipid-containing plasma membrane, causing leakage of cytoplasm", "inhibiting 70S ribosomes", "binding –SH groups", "forming HOCl"], 0,
  "Slide 30: phá **màng sinh chất chứa lipid** → **mất thành phần tế bào chất**.",
  ["", "Sai.", "Kim loại nặng.", "Chlorine."], ["phenol"], pool="mock", src=SRC + " slide 30")
q("CTL-04", "concept", 2, "Iodine is thought to impair protein synthesis and alter membranes by:",
  ["forming complexes with amino acids and unsaturated fatty acids", "forming thymine dimers", "cross-linking –NH2 groups like aldehydes", "acting as a surfactant cation"], 0,
  "Slide 33: iodine **tạo phức với amino acid và acid béo không no**.",
  ["", "UV.", "Aldehyde.", "Quats."], ["iodine"], pool="mock")
q("CTL-04", "application", 2, "A nurse needs to disinfect skin before surgery and also treat a wound. Which agent does the lecture say is used mainly for this purpose?",
  ["Glutaraldehyde", "Povidone-iodine (Betadine)", "Copper sulfate", "Formalin"], 1,
  "Slide 33: iodine chủ yếu dùng **sát khuẩn da và điều trị vết thương**.",
  ["Quá độc với mô sống.", "", "Diệt tảo.", "Độc, dùng bảo quản mẫu."], ["povidone-iodine"], pool="mock")
q("CTL-04", "not", 2, "Which agent does NOT act primarily on the plasma membrane?",
  ["Chlorhexidine", "O-phenylphenol", "Silver ions", "Alcohols (lipid dissolution)"], 2,
  "Ion bạc tác động **nhóm –SH của protein**; các tác nhân còn lại đều phá màng.",
  ["Tác động màng.", "Tác động màng.", "", "Có tác động màng."], ["heavy metals"], pool="mock")

v("CTL-04", "phenol", "phenol (acid carbolic)", "A disinfectant that damages lipid-containing membranes.", "Lister used phenol in surgery.", ["phenolics", "O-phenylphenol", "carbolic acid"])
v("CTL-04", "triclosan", "triclosan", "A bisphenol that inhibits lipid synthesis; P. aeruginosa is resistant.", "Triclosan was added to soaps.")
v("CTL-04", "chlorhexidine", "chlorhexidine", "An antiseptic that interferes with membrane structure.", "Chlorhexidine is used in mouthwash.")
v("CTL-04", "essential oils", "tinh dầu", "Plant hydrocarbon mixtures with phenolics and terpenes.", "Essential oils contain carvacrol.", ["carvacrol", "limonene"])
v("CTL-04", "iodophor", "iodophor", "A complex of iodine with an organic carrier that releases iodine slowly.", "Betadine is an iodophor.", ["povidone-iodine", "Betadine"])
v("CTL-04", "iodine", "iodine", "A halogen that impairs protein synthesis and alters membranes.", "Iodine is used on skin.")
v("CTL-04", "chlorine", "chlorine", "A halogen that forms HOCl in water.", "Chlorine disinfects drinking water.")
v("CTL-04", "hypochlorous acid", "acid hypochlorous (HOCl)", "A strong oxidizing agent formed from chlorine in water.", "HOCl damages enzymes.", ["HOCl"])
v("CTL-04", "alcohol", "cồn", "Ethanol or isopropanol; denatures proteins (requires water) and dissolves lipids.", "70% alcohol is used on skin.", ["alcohols", "ethanol", "isopropanol"])
v("CTL-04", "heavy metals", "kim loại nặng", "Ag, Hg, Cu and compounds that bind protein –SH groups.", "Silver is a heavy metal antimicrobial.", ["heavy metal"])
v("CTL-04", "sulfhydryl group", "nhóm sulfhydryl (–SH)", "A –SH group of proteins targeted by heavy metals.", "Mercury binds sulfhydryl groups.", ["sulfhydryl", "–SH"])

fc("CTL-04", "fact", "Phenol vs triclosan mechanism?", "Phenol: damages lipid membrane → leakage. Triclosan: inhibits lipid biosynthesis enzyme.")
fc("CTL-04", "fact", "What is Betadine?", "Povidone-iodine, an iodophor: iodine + N-vinylpyrrolidone polymer; releases iodine slowly; skin/wounds.")
fc("CTL-04", "fact", "Why can't alcohols sterilize?", "They do not kill endospores (or non-enveloped viruses).")
fc("CTL-04", "fact", "Heavy metals target?", "Sulfhydryl (–SH) groups of proteins → denaturation.")
fc("CTL-04", "trap", "TRUE/FALSE: 100% ethanol works better than 70%.", "FALSE – water is needed for protein denaturation.")

# ---------------------------------------------------------------- CTL-05
unit("CTL-05", "Chemical agents II: surfactants, preservatives, food antibiotics, aldehydes, peroxygens; culture preservation", "H", 2, 25, SRC + ": slides 37–44",
"""Nhãn phô mai ghi **E234 (nisin)** và **E235 (natamycin)**; xúc xích ghi **nitrite**; nước ngọt ghi **natri benzoat**. Đây đều là chất chống vi sinh vật trong thực phẩm – nhưng mỗi chất nhắm một nhóm khác nhau. Và cùng lúc đó, phòng thí nghiệm lại muốn **giữ cho vi khuẩn sống** hàng chục năm để làm giống – bằng **glycerol và −80 °C**.""",
("Nisin is added to cheese mainly to:",
 ["kill molds on the surface", "inhibit certain endospore-forming spoilage bacteria", "give color", "increase fermentation"], 1,
 "Slide 39: **nisin** – một **bacteriocin** – ức chế **vi khuẩn tạo nội bào tử gây hỏng**. **Natamycin** mới là kháng nấm."),
[
("1. Chất hoạt động bề mặt – surfactants (slide 37)", """
- **Surface-active agents (surfactants)**: **giảm sức căng bề mặt** giữa các phân tử chất lỏng.
- **Xà phòng và chất tẩy rửa (soaps and detergents)**: vai trò quan trọng là **loại bỏ cơ học vi sinh vật khi chà rửa (scrubbing)** – không nhất thiết giết.
- **Hợp chất amoni bậc bốn (quaternary ammonium compounds – quats)**, vd benzalkonium chloride:
  - khả năng làm sạch liên quan đến **phần tích điện dương (cation)** của phân tử;
  - **diệt khuẩn mạnh với Gram dương**, **kém hơn với Gram âm**;
  - **thay đổi tính thấm** của tế bào → **mất thành phần thiết yếu của tế bào chất**.
"""),
("2. Chất bảo quản thực phẩm (slide 38)", """
| Chất | Cơ chế / đích | Ghi chú |
|---|---|---|
| **Acid hữu cơ**: **sorbic acid, benzoic acid** (ở **pH thấp**) | **ức chế trao đổi chất** của tế bào vi khuẩn; acid hữu cơ thường ức chế trao đổi chất của **nấm sợi** | nước ngọt, mứt, bánh; calcium propionate trong bánh mì [mở rộng] |
| **Nitrate / nitrite** | **ức chế enzyme chứa sắt của vi khuẩn kỵ khí** | xúc xích, thịt nguội – chống *C. botulinum*; tạo màu hồng |
"""),
("3. Kháng sinh trong thực phẩm (slide 39)", """
- **Nisin**: thêm vào **phô mai** để **ức chế một số vi khuẩn tạo nội bào tử gây hỏng**.
  - Là một **bacteriocin** – **protein do một vi khuẩn tạo ra để ức chế vi khuẩn khác** (từ *Lactococcus lactis*).
  - Có sẵn lượng nhỏ trong nhiều sản phẩm sữa; **không vị, dễ tiêu hóa, không độc**.
- **Natamycin (pimaricin)**: **kháng sinh kháng nấm** được phép dùng trong thực phẩm, chủ yếu **phô mai**.
"""),
("4. Aldehyde (slide 40–41)", """
- **Formaldehyde** và **glutaraldehyde**: **bất hoạt protein** bằng cách tạo **liên kết chéo cộng hóa trị** với nhiều nhóm chức hữu cơ của protein (**–NH₂, –OH, –COOH, –SH**).
- **Khí formaldehyde** là chất khử trùng tuyệt vời.
- **Formalin** = dung dịch **37 %** khí formaldehyde trong nước: **bảo quản mẫu sinh học**, **bất hoạt vi khuẩn và virus trong vaccine**.
- **Glutaraldehyde**:
  - **ít kích ứng** và **hiệu quả hơn** formaldehyde;
  - khử trùng **dụng cụ bệnh viện**, gồm **ống nội soi** và thiết bị hô hấp;
  - dung dịch **2 % (Cidex®)**: **diệt khuẩn, diệt lao, diệt virus trong 10 phút**; **diệt bào tử trong 3–10 giờ** → là một trong số ít **chất tiệt trùng hóa học (chemical sterilant)**.
"""),
("5. H₂O₂ và ghi chú chung (slide 42)", """
- **Hydrogen peroxide (H₂O₂)**: **oxy hóa** thành phần tế bào (gốc tự do). Nhóm peroxygen còn có peracetic acid, ozone. [mở rộng]
- Slide 42: các tác nhân vật lý và hóa học trên **tác động lên tế bào của các vi sinh vật khác** (nấm, virus…) **theo cơ chế tương tự**.
"""),
("6. Bảo quản tế bào vi khuẩn – giống (slide 43–44)", """
| Thời hạn | Phương pháp | Chi tiết |
|---|---|---|
| **Ngắn hạn** | **4 °C** | trong thời gian ngắn (cấy chuyển định kỳ) |
| **Dài hạn** | **Đông lạnh sâu (deep freezing)** | huyền phù vi khuẩn + **glycerol 10–30 %** → **đông nhanh ở −70 °C → −95 °C**; cấy chuyển lại sau **vài năm** |
| **Dài hạn** | **Đông khô (freeze-drying)** | vi khuẩn trong môi trường bảo vệ (**sữa gầy/emulsion, huyết thanh, hoặc natri glutamate**) → cho vào ống/capsule → **làm lạnh nhanh (−54 °C → −72 °C)** → **tách nước bằng máy hút chân không** → **hàn kín** → bảo quản tủ lạnh (**≥ 10 năm**) |

- **Glycerol** là **chất bảo vệ lạnh (cryoprotectant)**: giảm tinh thể đá làm rách màng.
"""),
],
[
("Đọc nhãn thực phẩm", """
- **E200 sorbic acid, E211 sodium benzoate** – nước ngọt, tương ớt, mứt (chống nấm men, mốc ở pH thấp).
- **E250 sodium nitrite** – lạp xưởng, xúc xích, jambon (chống *C. botulinum*, giữ màu hồng). Giới hạn liều vì nitrite có thể tạo nitrosamine.
- **E234 nisin, E235 natamycin** – phô mai, sữa chua.
"""),
("Ngân hàng giống vi sinh", """
Các bộ sưu tập giống như **ATCC** (Mỹ), **VTCC** (Việt Nam – ĐHQG Hà Nội) bảo quản hàng chục nghìn chủng bằng **đông khô** và **nitơ lỏng (−196 °C)**. Trong lab, bạn sẽ bảo quản chủng bằng ống **glycerol stock ở −80 °C**.
"""),
],
[
("Surfactants", "Surfactants lower surface tension. **Soaps and detergents** remove microbes mechanically by **scrubbing**. **Quats** (cationic) are strongly bactericidal against **Gram-positive** bacteria, less against **Gram-negative**; they change permeability and cause loss of cytoplasmic constituents.", "Quats mạnh với Gram dương."),
("Food preservatives and antibiotics", "**Sorbic** and **benzoic acid** (at low pH) inhibit metabolism (especially of molds). **Nitrates/nitrites** inhibit **iron-containing enzymes of anaerobes**. **Nisin**: a **bacteriocin** added to cheese against **endospore-forming** spoilage bacteria; tasteless, digestible, nontoxic. **Natamycin (pimaricin)**: **antifungal** for cheese.", "Nisin chống vi khuẩn bào tử; natamycin chống nấm."),
("Aldehydes and H₂O₂", "**Formaldehyde** and **glutaraldehyde** inactivate proteins by **covalent cross-links** with –NH₂, –OH, –COOH, –SH. **Formalin** = 37 % formaldehyde (specimens, vaccines). **2 % glutaraldehyde (Cidex)**: bactericidal, tuberculocidal, virucidal in **10 min**, **sporicidal in 3–10 h**. **H₂O₂** acts by oxidation.", "Aldehyde tạo liên kết chéo; Cidex diệt bào tử 3–10 h."),
("Culture preservation", "Short term: **4 °C**. Long term: **deep freezing** with **10–30 % glycerol** at **−70 to −95 °C** (subculture after several years); **freeze-drying** (−54 to −72 °C, vacuum, sealed; **≥ 10 years**).", "Glycerol + −80 °C; đông khô ≥ 10 năm."),
],
["Quats are best against Gram-negatives", "Nisin is antifungal", "Glutaraldehyde kills spores in 10 minutes", "Soaps always kill bacteria"])

q("CTL-05", "recall", 1, "Quaternary ammonium compounds (quats) are strongly bactericidal against:",
  ["Gram-negative bacteria", "Gram-positive bacteria", "endospores", "non-enveloped viruses"], 1,
  "Slide 37: quats **mạnh với Gram dương**, **kém hơn với Gram âm**.",
  ["Kém hơn.", "", "Không.", "Không."], ["quats"], "Quats are best against Gram-negatives", src=SRC + " slide 37")
q("CTL-05", "recall", 1, "Natamycin (pimaricin) approved for use in foods such as cheese is:",
  ["a bacteriocin against endospore formers", "an antifungal antibiotic", "a nitrite", "an aldehyde"], 1,
  "Slide 39: **natamycin** là **kháng sinh kháng nấm** dùng trong thực phẩm, chủ yếu phô mai.",
  ["Đó là nisin.", "", "Sai.", "Sai."], ["natamycin"], "Nisin is antifungal", src=SRC + " slide 39")
q("CTL-05", "concept", 2, "Nisin is an example of a bacteriocin, which is:",
  ["a synthetic dye", "a protein produced by one bacterium that inhibits another", "an enzyme that digests peptidoglycan", "a heavy metal compound"], 1,
  "Slide 39: bacteriocin = **protein do một vi khuẩn tạo ra, ức chế vi khuẩn khác**.",
  ["Sai.", "", "Đó là lysozyme.", "Sai."], ["bacteriocin", "nisin"])
q("CTL-05", "recall", 1, "Nitrates and nitrites preserve meat by:",
  ["inhibiting iron-containing enzymes of anaerobic bacteria", "forming HOCl", "cross-linking proteins", "dissolving membranes"], 0,
  "Slide 38: nitrate/nitrite **ức chế enzyme chứa sắt của vi khuẩn kỵ khí** (như *C. botulinum*).",
  ["", "Chlorine.", "Aldehyde.", "Cồn/quats."], ["nitrite"], src=SRC + " slide 38")
q("CTL-05", "concept", 2, "Aldehydes such as glutaraldehyde inactivate proteins by:",
  ["oxidizing them with free radicals", "forming covalent cross-links with –NH2, –OH, –COOH and –SH groups", "binding only to DNA", "lowering surface tension"], 1,
  "Slide 40: aldehyde tạo **liên kết chéo cộng hóa trị** với **–NH₂, –OH, –COOH, –SH**.",
  ["H₂O₂.", "", "Sai.", "Surfactant."], ["aldehyde", "glutaraldehyde"], src=SRC + " slide 40")
q("CTL-05", "recall", 2, "According to the lecture, 2% glutaraldehyde (Cidex) is sporicidal after how long?",
  ["10 minutes", "3 to 10 hours", "30 seconds", "24 days"], 1,
  "Slide 41: Cidex diệt khuẩn, lao, virus trong **10 phút**; diệt **bào tử trong 3–10 giờ**.",
  ["Đó là thời gian diệt khuẩn/virus.", "", "Sai.", "Sai."], ["glutaraldehyde"], "Glutaraldehyde kills spores in 10 minutes", src=SRC + " slide 41")
q("CTL-05", "recall", 1, "For long-term deep-freeze preservation, bacteria are suspended in:",
  ["10–30% glycerol and frozen quickly at −70 to −95 °C", "70% ethanol at 4 °C", "formalin at room temperature", "distilled water at −20 °C"], 0,
  "Slide 44: dịch vi khuẩn + **glycerol 10–30 %** → **đông nhanh −70 °C → −95 °C**.",
  ["", "Cồn giết vi khuẩn.", "Formalin giết.", "Không có chất bảo vệ lạnh."], ["glycerol", "deep freezing"], src=SRC + " slide 44")
q("CTL-05", "not", 2, "Which statement about soaps and detergents is NOT correct according to the lecture?",
  ["They are surface-active agents", "They lower surface tension", "Their important role is mechanical removal of microbes by scrubbing", "They are reliable sterilants that kill endospores"], 3,
  "Xà phòng chủ yếu **loại bỏ cơ học**; không phải chất tiệt trùng.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["surfactant"], "Soaps always kill bacteria")
q("CTL-05", "recall", 1, "Formalin, used to preserve specimens and inactivate microbes in vaccines, is:",
  ["2% glutaraldehyde", "a 37% aqueous solution of formaldehyde gas", "3% hydrogen peroxide", "70% ethanol"], 1,
  "Slide 40: **formalin = dung dịch 37 % formaldehyde**.",
  ["Cidex.", "", "Sai.", "Sai."], ["formalin"], pool="mock", src=SRC + " slide 40")
q("CTL-05", "concept", 2, "Freeze-drying (lyophilization) of a bacterial culture involves:",
  ["heating to 121 °C then drying", "rapid cooling to about −54 to −72 °C, removing water by vacuum, and sealing", "adding formalin and air-drying", "UV irradiation"], 1,
  "Slide 44: rapid cooling (−54 → −72 °C) → **hút chân không tách nước** → hàn kín → tủ lạnh (≥ 10 năm).",
  ["Sai.", "", "Sai.", "Sai."], ["lyophilization"], pool="mock")
q("CTL-05", "application", 2, "A hospital must disinfect a heat-sensitive endoscope and ideally kill spores. Which agent from the lecture fits best?",
  ["70% ethanol", "2% glutaraldehyde (Cidex)", "Soap and water", "Sorbic acid"], 1,
  "Glutaraldehyde dùng cho **ống nội soi**, ít kích ứng, diệt bào tử trong 3–10 h.",
  ["Không diệt bào tử.", "", "Chỉ loại cơ học.", "Chất bảo quản thực phẩm."], ["glutaraldehyde"], pool="mock")
q("CTL-05", "not", 2, "Which is NOT a property of nisin given in the lecture?",
  ["It is tasteless", "It is readily digested", "It is nontoxic", "It is an antifungal agent used against molds"], 3,
  "Nisin chống **vi khuẩn tạo bào tử**; **natamycin** mới là kháng nấm.",
  ["Đúng.", "Đúng.", "Đúng.", ""], ["nisin"], pool="mock")

v("CTL-05", "surfactant", "chất hoạt động bề mặt", "A surface-active agent that lowers surface tension.", "Soaps are surfactants.", ["surfactants", "surface-active agents", "detergent", "soaps"])
v("CTL-05", "quats", "hợp chất amoni bậc bốn", "Quaternary ammonium compounds; cationic surfactants effective against Gram-positives.", "Benzalkonium chloride is one of the quats.", ["quaternary ammonium compounds", "quat"])
v("CTL-05", "food preservatives", "chất bảo quản thực phẩm", "Chemicals such as sorbic acid, benzoic acid and nitrite that inhibit spoilage.", "Benzoic acid is a common food preservative.", ["sorbic acid", "benzoic acid", "preservative"])
v("CTL-05", "nitrite", "nitrite", "A preservative inhibiting iron-containing enzymes of anaerobes.", "Nitrite prevents botulism in ham.", ["nitrites", "nitrate", "nitrates"])
v("CTL-05", "bacteriocin", "bacteriocin", "A protein made by one bacterium that inhibits another.", "Nisin is a bacteriocin.", ["bacteriocins"])
v("CTL-05", "nisin", "nisin", "A bacteriocin added to cheese to inhibit endospore-forming bacteria.", "Nisin is nontoxic.")
v("CTL-05", "natamycin", "natamycin (pimaricin)", "An antifungal antibiotic approved for foods, mainly cheese.", "Natamycin prevents mold on cheese.", ["pimaricin"])
v("CTL-05", "aldehyde", "aldehyde", "Formaldehyde or glutaraldehyde; inactivates proteins by cross-linking.", "Aldehydes are chemical sterilants.", ["aldehydes", "formaldehyde"])
v("CTL-05", "glutaraldehyde", "glutaraldehyde", "A less irritating aldehyde; 2% Cidex kills spores in 3–10 h.", "Endoscopes are disinfected with glutaraldehyde.", ["Cidex"])
v("CTL-05", "formalin", "formalin", "A 37% aqueous solution of formaldehyde.", "Specimens are preserved in formalin.")
v("CTL-05", "hydrogen peroxide", "hydrogen peroxide (H2O2)", "An oxidizing antimicrobial agent.", "Hydrogen peroxide acts by oxidation.", ["H2O2", "peroxygen"])
v("CTL-05", "glycerol", "glycerol", "A cryoprotectant used at 10–30% for deep freezing cultures.", "Store stocks in glycerol at −80 °C.", ["cryoprotectant"])
v("CTL-05", "deep freezing", "đông lạnh sâu", "Storing cultures at −70 to −95 °C with glycerol.", "Deep freezing keeps strains for years.")

fc("CTL-05", "fact", "Quats are most effective against?", "Gram-positive bacteria (less against Gram-negative); act on permeability.")
fc("CTL-05", "fact", "Nisin vs natamycin?", "Nisin: bacteriocin vs endospore-forming bacteria in cheese. Natamycin (pimaricin): antifungal.")
fc("CTL-05", "number", "Cidex (2% glutaraldehyde) times?", "Bactericidal, tuberculocidal, virucidal in 10 min; sporicidal in 3–10 h.")
fc("CTL-05", "number", "Deep freezing and freeze-drying conditions?", "Glycerol 10–30%, −70 to −95 °C; freeze-drying −54 to −72 °C, vacuum, sealed, ≥10 years.")
fc("CTL-05", "fact", "Aldehyde target groups?", "–NH2, –OH, –COOH, –SH on proteins (covalent cross-links).")
