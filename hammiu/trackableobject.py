# Mục đích: lưu thông tin các object

class TrackableObject:
    def __init__(self, objectID, centroid):
        """
            Lưu object ID, khởi tạo list of centroids using the current centroid
        """
        self.objectID = objectID 
        self.centroids = [centroid]     # lưu lịch sử các centroids

        # khởi tạo biến Boolean xem object đã được đếm chưa
        self.counted = False
        

    