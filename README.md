# People-Counter-with-OpenCV
Trong bài này chúng ta sẽ kết hợp cả `object detection` và `object tracking` để giải quyết bài toán đếm số người (ví dụ người ra vào cửa hàng tạp hóa, trung tâm thương mại...)

Một bộ theo dõi đối tượng với độ chính xác cao sẽ là sự kết hợp của 2 concept object detection và object tracking, chúng ta sẽ chia thành 2 pha:
* **Pha 1 - detecting:** Trong suốt detection phase chúng ta sẽ thực hiện
    * Phát hiện vật thể mới
    * Quan sát nếu thấy vật thể xuất hiện lại (bị mất trong tracking phase, ví dụ đi ra khỏi khung hình)
Đối với các vật thể được phát hiện chúng ta sẽ tạo hoặc update object tracker với bounding box mới. Do quá trình thực hiện detection rất tốn kém về tài nguyên do đó chúng ta sẽ thực hiện điều này sau mỗi N khung hình.
* **Pha 2 - Tracking:** Đối với vật thể được phát hiện chúng ta sẽ tạo object tracker cho chúng và theo dõi chúng di chuyển trong. Object tracker này nhanh hơn và hiệu quả hơn so với objetc detector. Chúng ta tiếp tục thực hiện tracking cho đến khi đạt đến N-th khung hình và chạy lại object detection. Tất cả quá trình được lặp lại.

Bài này chúng ta sẽ sử dụng `centroid tracking algorithm` để thực hiện theo dõi các vật thể và sử dụng `SSD` để phát hiện các vật thể.

https://github.com/saimj7/People-Counting-in-Real-Time/blob/master/Run.py

