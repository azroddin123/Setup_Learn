# steps to train arabic data in python

1. clone the git repository
git clone https: // github.com/Nivratti/PaddleOCR

2. install necessary requirements.txt
pip install - r requirements.txt

3.paddlepaddle-gpu version 2.2
pip install paddlepaddle-gpu

4.Install the compatible cuda version for gpu training
  ex. 
  conda install paddlepaddle-gpu==2.2.2 cudatoolkit=11.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge 
  check cudatoolkit , nvcc , python , ubuntu , nvidia-smi

5.Check paddle by following command in python prompt

    import paddle
    paddle.utils.run_check

    if it shows message then go for next

6.Download data from the google drive.
ex. https://drive.google.com/drive/folders/1u7sA0RaIZx0MT71KBeWzoF4PjCGLePq-





7. Extract that data in specific folder

for f in *.tar; do tar xf "$f"; done
 or 

 tar xf --filename 


 8. place the extracted data in train data folder of PaddleOCR

 9.Run the command to train data

 python3 tools/train.py -c configs/rec/arabic_v2_with_contextual_chars.yml     -o  Global.save_res_path="./output/det_db/predicts_db.txt"    Global.save_model_dir="./output/rec_arabic_contextual_form_v1"     Global.epoch_num=200         Optimizer.lr.learning_rate=0.001   Optimizer.lr.warmup_epoch=5     Train.dataset.data_dir="./train_data"         Train.dataset.label_file_list=\["./train_data/rec_gt_train_combined.txt"\]         Eval.dataset.data_dir="./train_data/"         Eval.dataset.label_file_list=\["./train_data/rec_gt_test_combined.txt"\]         Train.loader.batch_size_per_card=256         Eval.loader.batch_size_per_card=256 Train.loader.num_workers=16 Eval.loader.num_workers=16 