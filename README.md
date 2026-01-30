🏡 Pixel Village AI Agent Simulation
Một mô phỏng AI Agent cổ điển – Environment – Control Loop trực quan bằng Python + Pygame, giúp minh họa cách một Agent quan sát – quyết định – hành động – tồn tại trong không gian & thời gian giống như một sinh thể trong làng pixel.

🎯 Mục tiêu dự án
Minh họa khái niệm Agent trong AI một cách trực quan
Phân biệt rõ:
Agent logic (quyết định)
Environment (quy luật thế giới)
Embodiment (Agent có thân thể, di chuyển thật)
Dùng để:
Demo bài học AI
Thuyết trình Agentic AI
Là nền tảng mở rộng (multi-agent, learning, planning…)

🧠 Kiến trúc tổng thể
┌──────────────────┐
│ VillageEnvironment│  ← trạng thái thế giới
└─────────┬────────┘
          │ observe()
┌─────────▼────────┐
│  VillageAgent    │  ← logic quyết định
└─────────┬────────┘
          │ action
┌─────────▼────────┐
│  RenderAgent     │  ← thân thể, di chuyển
└─────────┬────────┘
          │
┌─────────▼────────┐
│   VillageGUI     │  ← hiển thị
└──────────────────┘

🌱 Mô tả môi trường (Environment)
Food: tài nguyên sinh tồn
Weather: thời tiết (sunny / rainy)
Môi trường:
Tự thay đổi theo thời gian
Agent không kiểm soát được
Luật môi trường
Action	Weather	Kết quả
farm	sunny	+5 food
farm	rainy	+2 food
eat	any	-1 food

🤖 Mô tả Agent
Goal: survive
Perception:
food
weather
Decision rule:
food < 5 → farm
food ≥ 5 → eat
Agent:
Không biết trạng thái nội bộ môi trường
Chỉ phản ứng dựa trên perception

🚶 Di chuyển & Embodiment
Khác với mô phỏng logic thuần:
Agent không teleport
Agent:
Có vị trí (x, y)
Di chuyển từng frame
Action chỉ xảy ra khi đến đúng địa điểm
👉 Điều này giúp mô hình giống sinh vật thật hơn, phù hợp Agentic AI hiện đại.

🗺️ Bản đồ làng
Khu vực	Chức năng
Farm	tạo food
House	ăn
Lake	cảnh quan
Market	mở rộng sau

🖥️ Giao diện (GUI)
Phong cách pixel đơn giản
Màu nền phản ánh thời tiết

Hiển thị:
Day
Food
Weather
Current action
Agent di chuyển chậm, dễ quan sát

⚙️ Cài đặt & chạy chương trình
1. Cài thư viện
pip install pygame
2. Chạy mô phỏng
python environment.py

🧪 Luồng chạy chương trình
Môi trường cập nhật thời tiết
Agent quan sát (observe)
Agent quyết định (decide)
Agent di chuyển tới mục tiêu
Action tác động lên môi trường
Lặp lại theo ngày

🚀 Hướng mở rộng
Thêm memory (nhớ thời tiết trước)
Thêm reward / penalty
Multi-agent (nhiều dân làng)
Learning (Q-learning / RL)
Task planning (chuỗi hành động)

📌 Ý nghĩa học thuật
Dự án này minh họa rõ:
Agent ≠ function
Action ≠ instant
Intelligence cần:
Environment
Time
Embodiment
“An agent is something that perceives and acts in an environment.”
