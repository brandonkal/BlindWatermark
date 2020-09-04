# Blind watermark

## Introduction

Are you still worrying about others stealing your pictures but not admitting it?
The pictures you created for yourself are still being taken by bad things (visual xx) to seek compensation from others. Are the copyrights still inexplicably in the hands of bad things and worry about it?

To solve this problem, I created this project and implemented it with python

_What is a blind watermark?_
Blind watermark algorithm can embed your watermark into the picture, and the obtained picture is visually almost the same as the original picture, but you can solve your watermark through the algorithm and your own key

_What are the advantages of blind watermarking compared to ordinary watermarking?_
Blind watermarks will not affect your image perception in the first place, and they are not clipped, covered and lose their effect like ordinary watermarks. My blind watermarking algorithm can effectively resist blur, image coverage, salt and pepper noise, brightness changes, cropping effects, and even **screenshot** can also extract the watermark (use ps to remove the screenshot and the target image. Irrelevant parts, and zoom will be the original size)

**todo list**

-[x] Added support channel -[x] Support multi-level discrete wavelet transform -[x] Support automatic compensation to remove the restriction that the length and width of the picture need to be even
-[] Package and upload pypi, do not consider the time, wait until it is more complete, then package and upload -[x] Add command line mode
-[] Add more embedding methods (0/n)
-Try QIM for embedding, it fails, there is a gap between theory and reality -[x] Use pyqt to write GUI interface -[x] To realize the restoration of a deformed image that is subject to deformation attacks, such as translation, rotation, zoom, perspective, etc., to be close to the original image, which is a necessary pre-step for extracting watermarks from images that are subject to deformation attacks -`from BlindWatermark import recovery`

### Big update

-Solved the problem of white dots appearing in the black area when the watermark was embedded

-Support multi-level wavelet transform and set block size

```
Set the wavelet transform series to d by default 1, the block size is (m, m) by default (4, 4), the image size is x * y, and the length and width product of the watermark is wm_size
Need to meet
```

![Conditions](./pics_for_show/mic/gongshi.png)

-Realize resistance to deformation attacks

## Current problem

If you don't want to be biased against this program due to the shortcomings of the current program, please **skip** this part

-This may be the problem of all open source blind watermarks. Due to the disclosure of the algorithm, we must use the key (here refers to the random seed and divisor) to prevent the pictures posted on the Internet from being reversely cracked by others based on our algorithm and key But in order to show that there is our picture in the picture, we have to extract the watermark in the public environment to verify that we did extract the watermark from this picture. But this will cause our key to be exposed, making this picture The blind watermark inside is removed by the bad things later, which seems to make this blind watermark only take effect once
-The possible solution envisaged: find a credible platform, watermark copyright contenders, upload their own keys to the platform, and the platform will perform the operation of watermarking, but such a platform is difficult to establish in the short term
-If I want to come to P station, it may be possible to become such a platform. If I can make a better way to add blind watermark to video, maybe B station and other video sites will also take action. If my algorithm is strong enough, After all, dreams are still necessary
-Closed source? This simply doesn't work, because you don't know what it does for a closed source program. Would you believe that the so-called solved watermark is really obtained from that picture? I can even Write the program, no matter what the picture is, it will output my watermark with random noise.Is it under the sky, so the picture is mine?
-Of course, my vision is not broad enough. I have overlooked some key points or said something wrong. I hope everyone can point it out and help me improve my program, thank you my friends

## Applicability

-Applicable people: creators who want to protect their own pictures
-Picture requirements: None
-Watermark requirements:

-Only binarized information can be embedded, the B channel of the watermark will be automatically taken and embedded in binarization, the watermark is preferably a black and white picture
-The length × width of the watermark is required to be <= the length of the picture/2/4 × the width of the picture/2/4, the program will automatically verify

-Program dependencies:
-python3
-numpy
-opencv
-PyWavelets

## how to use

[Video link of station B](https://www.bilibili.com/video/av52047712/)

_Qiafan warning_ Please pay attention to my station B account, Sanlian, and star

Use `git pull https://github.com/fire-keeper/BlindWatermark.git` or download the compressed package directly to pull the project locally, and then under the project directory

**Command line version**

```
#Embed
python bwm.py -k 4399 2333 32 -em -r pic/lena_grey.png -wm pic/wm.png -o out.png -s
```

```
#extract
python bwm.py -k 4399 2333 32 -ex -r out.png -wm pic/wm.png -ws 64 64 -o out_wm.png -s
```

Parameter introduction

```
"--key",'-k' Input 2 random seeds and the divisor (positive number) in turn, the divisor can be one or two, separated by spaces. For example (4399,2333,32)
There is no parameter after'-em','--embed', which means that this operation is embedded watermark
There is no parameter after'-ex','--extract', indicating that this operation is to extract the watermark
               There must be one and only one of the above two requirements
"--read",'-r' "The path of the picture to be embedded or extracted"
"--read_wm",'-wm' The path of the watermark to be embedded
"--wm_shape",'-ws' to solve the shape of the watermark
"--out_put",'-o' the output path of the picture
"--show_ncc",'-s' show the NC value (similarity) between the output image and the original image

'-bs','--block_shape' sets the block size. Because the length and width are the same, you only need to pass an integer. For large images, you can use larger numbers, such as 8. The original image has less impact and the calculation time is reduced, but the robustness is not improved. Too much attention will make the watermark information exceed the carrying capacity of the image
'-d','--dwt_deep', set the number of wavelet transforms, increasing the number of times will improve the robustness, but will reduce the ability of the image to carry watermarks, usually 1, 2, 3
```

When adjusting the parameters, the divisor is mainly adjusted, that is, the third (4th) parameter of --key, to maximize the value under the premise that the picture is not distorted

**Run the following python command**

```
# python code
#Import module
from BlindWatermark import watermark
```

```
#Embed

bwm1 = watermark(4399,2333,36,20)
#4399 and 2333 are two random seeds, 36 and 20 are the divisors used in the embedding algorithm. Theoretically, the first divisor is larger than the second. The larger the divisor, the stronger the robustness, but the larger the divisor, the output picture The greater the distortion, it needs to be determined after weighing
#These two random seeds are best to have different values ​​for different pictures to prevent the seeds from being exposed and making all pictures lose protection
#The second divisor can be omitted. The increase does not significantly improve the robustness of the watermark, but it will affect the quality of the output image under certain circumstances.
bwm1.read_ori_img("pic/lena_grey.png")
#Read the original image
bwm1.read_wm("pic/wm.png")
#Read watermark
bwm1.embed('out.png')
#Embed the watermark in the original image and output to'out.png'
```

```
# Use NCC to numerically judge the similarity between the output image and the original image
from BlindWatermark import test_ncc

test_ncc('pic/lena_grey.png','out.png')
#Judging the similarity of these two pictures, the output is 0~1, the closer the value is to 1, the more similar the two are
```

```
#extract

bwm1 = watermark(4399,2333,36,20,wm_shape=(64,64))
#Use the parameters of the previous embedded watermark to instantiate the object, pay attention to the length and width of the watermark
bwm1.extract("out.png","out_wm.png")
#Note that you need to create a Y_U_V/ folder in the same level directory of the output watermark, otherwise the watermark extracted by the single channel will not be saved
```

**Support Chifan**

![Alipay](./pics_for_show/mic/alipay.png)![setu](pics_for_show/mic/setu_qrcode.png)

## Show results

The original image `lena_grey.png` and the watermark image `wm.png` to be embedded in the watermark

![lena](./pic/lena_grey.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/200) ![watermark](./pic/wm.png?imageMogr2/auto-orient/strip% 7CimageView2/2/w/100)

Embedded picture

![Picture with embedded watermark](./pics_for_show/grey/output/attack/ori_lena.png)

Extracted picture

![Extracted picture](./pics_for_show/grey/extract/ori_wm.png)

#### Various attacks and extracted watermarks

| Attack method              | Picture after attack                                                           | Watermark extracted                                      |
| -------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------- |
| Blur                       | ![blur_lena.png](./pics_for_show/grey/output/attack/blur_lena.png)             | ![blur_wm.png](./pics_for_show/grey/extract/blur_wm.png) |
| Overlay with images        | ![cover_lena.png](./pics_for_show/grey/output/attack/cover_lena.png)           | ![](./pics_for_show/grey/extract/cover_wm.png)           |
| Cover with lines           | ![randline_lena.png](./pics_for_show/grey/output/attack/randline_lena.png)     | ![](./pics_for_show/grey/extract/randline_wm.png)        |
| Increase brightness by 10% | ![brighter10_lena.png](./pics_for_show/grey/output/attack/brighter10_lena.png) | ![](./pics_for_show/grey/extract/brighter10_wm.png)      |
| Brightness reduced by 10%  | ![darker10_lena.png](./pics_for_show/grey/output/attack/darker10_lena.png)     | ![](./pics_for_show/grey/extract/darker10_wm.png)        |
| Add salt and pepper noise  | ![saltnoise_lena.png](./pics_for_show/grey/output/attack/saltnoise_lena.png)   | ![](./pics_for_show/grey/extract/saltnoise_wm.png)       |
| Crop 5% and fill           | ![](./pics_for_show/grey/output/attack/chop5_lena.png)                         | ![](./pics_for_show/grey/extract/chop5_wm.png)           |
| Crop 10%                   | ![](./pics_for_show/grey/output/attack/chop10_lena.png)                        | ![](./pics_for_show/grey/extract/chop10_wm.png)          |
| Cropped 30%                | ![](./pics_for_show/grey/output/attack/chop30_lena.png)                        | ![](./pics_for_show/grey/extract/chop30_wm.png)          |

#### For jpeg compression, it is tested that the Y channel dewatering effect is the best. The watermarks solved below are all from the Y channel

| Compression factor | Compressed image                                         | Extracted watermark                                     |
| ------------------ | -------------------------------------------------------- | ------------------------------------------------------- |
| 90                 | ![](./pics_for_show/grey/output/attack/jpeg_90_lena.jpg) | ![](./pics_for_show/grey/extract/Y_U_V/Yjpeg_90_wm.png) |
| 85                 | ![](./pics_for_show/grey/output/attack/jpeg_85_lena.jpg) | ![](./pics_for_show/grey/extract/Y_U_V/Yjpeg_85_wm.png) |
| 80                 | ![](./pics_for_show/grey/output/attack/jpeg_80_lena.jpg) | ![](./pics_for_show/grey/extract/Y_U_V/Yjpeg_80_wm.png) |
| 70                 | ![](./pics_for_show/grey/output/attack/jpeg_70_lena.jpg) | ![](./pics_for_show/grey/extract/Y_U_V/Yjpeg_70_wm.png) |
| 60                 | ![](./pics_for_show/grey/output/attack/jpeg_60_lena.jpg) | ![](./pics_for_show/grey/extract/Y_U_V/Yjpeg_60_wm.png) |
| 50                 | ![](./pics_for_show/grey/output/attack/jpeg_50_lena.jpg) | ![](./pics_for_show/grey/extract/Y_U_V/Yjpeg_50_wm.png) |
| 40                 | ![](./pics_for_show/grey/output/attack/jpeg_40_lena.jpg) | ![](./pics_for_show/grey/extract/Y_U_V/Yjpeg_40_wm.png) |

#### Watermark anti-cracking

If there is a bad business who wants to destroy our watermark and add his watermark, if he knows our encryption method (do not know our random seed and divisor), the cracking impact should be the greatest, and we will demonstrate this situation.

Now there are two kinds of pictures A on the Internet, B. A was published after we embedded the watermark, and B was generated by the cracker adding his own watermark on A using the same blind watermarking method. However, we use our parameters ( Random seed and divisor) can extract our watermark from A and B, but when extracting with the parameters of the cracker, the watermark of the cracker cannot be extracted from A, only the watermark of the cracker can be extracted from B

This can explain who the creator of this picture is. I think this is a crucial step to protect the rights of the creator.

Cracker's watermark![](pic/wm2.png)

| Introduction                                                                                                 | Picture                                       | Extracted Watermark                                |
| ------------------------------------------------------------------------------------------------------------ | --------------------------------------------- | -------------------------------------------------- |
| Picture A where we embed the watermark                                                                       | ![](./pics_for_show/grey/anti-crack/out.png)  | ![](./pics_for_show/grey/anti-crack/out_wm.png)    |
| The cracker embeds the watermarked picture B again in the picture above where we have embedded the watermark | ![](./pics_for_show/grey/anti-crack/out2.png) | ![](./pics_for_show/grey/ anti-crack/out_wm2.png)  |
| Use our parameters to extract the cracker's picture B                                                        |                                               | ![](./pics_for_show/grey/anti-crack/bwm1_out2.png) |
| Extract our picture A with the parameters of the cracker                                                     |                                               | ![](./pics_for_show/grey/anti-crack/bwm2_out.png)  |
