def order_points_clockwise(pts):
    """
    reference from: https://github.com/jrosebr1/imutils/blob/master/imutils/perspective.py
    # sort the points based on their x-coordinates
    """
    xSorted = pts[np.argsort(pts[:, 0]), :]

    # grab the left-most and right-most points from the sorted
    # x-roodinate points
    leftMost = xSorted[:2, :]
    rightMost = xSorted[2:, :]

    # now, sort the left-most coordinates according to their
    # y-coordinates so we can grab the top-left and bottom-left
    # points, respectively
    leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
    (tl, bl) = leftMost

    rightMost = rightMost[np.argsort(rightMost[:, 1]), :]
    (tr, br) = rightMost

    rect = np.array([tl, tr, br, bl], dtype="float32")
    return rect

def clip_det_res(points, img_height, img_width):
    for pno in range(points.shape[0]):
        points[pno, 0] = int(min(max(points[pno, 0], 0), img_width - 1))
        points[pno, 1] = int(min(max(points[pno, 1], 0), img_height - 1))
    return points

def filter_tag_det_res(dt_boxes, image_shape):
    img_height, img_width = image_shape[0:2]
    dt_boxes_new = []
    for box in dt_boxes:
        box = order_points_clockwise(box)
        ## Commented filtering as it causing issues in writing
        # box = clip_det_res(box, img_height, img_width)
        # rect_width = int(np.linalg.norm(box[0] - box[1]))
        # rect_height = int(np.linalg.norm(box[0] - box[3]))
        # if rect_width <= 3 or rect_height <= 3:
        #     continue
        dt_boxes_new.append(box)
    dt_boxes = np.array(dt_boxes_new)
    return dt_boxes

def convert_2_final_bbox_format(bboxes, img_shape):
    dt_boxes = []
    for bbox in bboxes:
        ## Convert mmocr bbox in the form of paddleocr bbox -- (4,2) polygon shape
        new_box = [x for x in bbox]
        Pts = np.array([new_box], np.int32)
        # print(Pts)
        # rect = cv.minAreaRect(cnt)
        rect = cv2.minAreaRect(Pts.reshape((-1, 2)))
        box = cv2.boxPoints(rect)
        # box = np.int0(box) ## (4, 2) shape box
        # print(box)
        # Image.fromarray(cv2.drawContours(image_rgb.copy(),[box],0,(0,0,255),2))
        dt_boxes.append(box)

    # Order points clockwise, clip points and Filter results
    # paddleocr_engine.text_detector
    dt_boxes = filter_tag_det_res(
        dt_boxes, img_shape
    )
    return dt_boxes
