# Project PaintingLight

PaintingLight is a project conducted by the Style2Paints team, aimed at finding a method to manipulate the illumination in digital paintings. The project started at about 2019 January, and the core algorithm is accepted by ACM Transitions on Graphics at 2020. 

Because digital painting illumination data is not easy to obtain, this algorithm does not use deep learning. The core idea is to make use of color geometry to build up a perceptually workable relighting system. Such relighting may not be physically accurate, but are good enough for artistic use cases.

Note that the project is still in its technical researching stage. If you are a digital painting artist and you accidentally find this page, you may have to wait for our ongoing PhotoShop plug-in for practical usage.

# Technical Paper

Please refer to our [project page](https://lllyasviel.github.io/PaintingLight/) for our TOG/SIGGRAPH paper. 

# Video and Animated Demos

[![video_link](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/vid_icon.png)](https://www.youtube.com/watch?v=X7li86oMBLA)

# Installation

The codes have been tested for python 3.6 in both Windows 10 and Ubuntu 16.04.

To download codes:

    git clone https://github.com/lllyasviel/PaintingLight.git
    cd PaintingLight
    cd code

To install some environment:

    pip install opencv-python
    pip install opencv-contrib-python

To install some super accurate environment:

    pip instal tensorflow==1.4.0
    pip install scipy==1.1.0
    pip install trimesh==2.37.1

install rtree dependency 

    sudo apt install libspatialindex-dev

Then install the rtree package. The original rtree does not support windows, nevertheless here I provide a windows binary so that you can directly install it. 

    (linux only) pip install rtree==0.9.3
    (windows only) pip install Rtree-0.9.3-cp36-cp36m-win_amd64.whl

To install pyembree to enable GPU ray tracing:

(Optional, you can skip this step if you do not care about speed.) 

[Linux Pyembree](https://github.com/scopatz/pyembree)

[Windows Pyembree](https://github.com/scopatz/pyembree/issues/14)

# Playing with Examples

You may directly play with our interactive examples! 

**The image noise artifacts in this webpage is caused by web GIF compression.**

**These artifacts do not exist when you try on your own.**

![001](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/001.gif)  | * Example 001 <br> * Not need a mask <br> * Input image "001.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example001.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![002](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/002.gif)  | * Example 002 <br> * Not need a mask <br> * Input image "002.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example002.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![003](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/003.gif)  | * Example 003 <br> * Not need a mask <br> * Input image "003.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example003.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![004](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/004.gif)  | * Example 004 <br> * Not need a mask <br> * Input image "004.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example004.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![005](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/005.gif)  | * Example 005 <br> * Not need a mask <br> * Input image "005.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example005.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![006](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/006.gif)  | * Example 006 <br> * Not need a mask <br> * Input image "006.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example006.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![007](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/007.gif)  | * Example 007 <br> * Not need a mask <br> * Input image "007.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example007.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![008](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/008.gif)  | * Example 008 <br> * Not need a mask <br> * Input image "008.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example008.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![009](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/009.gif)  | * Example 009 <br> * Not need a mask <br> * Input image "009.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example009.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![010](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/010.gif)  | * Example 010 <br> * Not need a mask <br> * Input image "010.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example010.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![011](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/011.gif)  | * Example 011 <br> * Not need a mask <br> * Input image "011.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example011.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![012](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/012.gif)  | * Example 012 <br> * Not need a mask <br> * Input image "012.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example012.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![013](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/013.gif)  | * Example 013 <br> * Not need a mask <br> * Input image "013.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example013.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![014](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/014.gif)  | * Example 014 <br> * Not need a mask <br> * Input image "014.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example014.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![015](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/015.gif)  | * Example 015 <br> * Not need a mask <br> * Input image "015.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example015.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![016](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/016.gif)  | * Example 016 <br> * Not need a mask <br> * Input image "016.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example016.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![017](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/017.gif)  | * Example 017 <br> * Not need a mask <br> * Input image "017.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example017.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![018](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/018.gif)  | * Example 018 <br> * Not need a mask <br> * Input image "018.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example018.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![019](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/019.gif)  | * Example 019 <br> * Not need a mask <br> * Input image "019.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example019.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![020](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/020.gif)  | * Example 020 <br> * Not need a mask <br> * Input image "020.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example020.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![021](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/021.gif)  | * Example 021 <br> * Not need a mask <br> * Input image "021.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example021.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![022](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/022.gif)  | * Example 022 <br> * Not need a mask <br> * Input image "022.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example022.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![023](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/023.gif)  | * Example 023 <br> * Not need a mask <br> * Input image "023.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example023.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![024](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/024.gif)  | * Example 024 <br> * Not need a mask <br> * Input image "024.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example024.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![025](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/025.gif)  | * Example 025 <br> * Not need a mask <br> * Input image "025.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example025.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![026](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/026.gif)  | * Example 026 <br> * Not need a mask <br> * Input image "026.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example026.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![027](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/027.gif)  | * Example 027 <br> * Not need a mask <br> * Input image "027.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example027.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![028](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/028.gif)  | * Example 028 <br> * Not need a mask <br> * Input image "028.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example028.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![029](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/029.gif)  | * Example 029 <br> * Not need a mask <br> * Input image "029.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example029.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![030](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/030.gif)  | * Example 030 <br> * Not need a mask <br> * Input image "030.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example030.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![031](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/031.gif)  | * Example 031 <br> * Not need a mask <br> * Input image "031.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example031.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![032](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/032.gif)  | * Example 032 <br> * Not need a mask <br> * Input image "032.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example032.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![033](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/033.gif)  | * Example 033 <br> * Not need a mask <br> * Input image "033.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example033.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![034](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/034.gif)  | * Example 034 <br> * Not need a mask <br> * Input image "034.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example034.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![035](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/035.gif)  | * Example 035 <br> * Not need a mask <br> * Input image "035.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example035.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![036](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/036.gif)  | * Example 036 <br> * Not need a mask <br> * Input image "036.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example036.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![037](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/037.gif)  | * Example 037 <br> * Not need a mask <br> * Input image "037.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example037.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![038](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/038.gif)  | * Example 038 <br> * Not need a mask <br> * Input image "038.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example038.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![039](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/039.gif)  | * Example 039 <br> * Not need a mask <br> * Input image "039.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example039.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![040](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/040.gif)  | * Example 040 <br> * Not need a mask <br> * Input image "040.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example040.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![041](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/041.gif)  | * Example 041 <br> * Not need a mask <br> * Input image "041.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example041.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![042](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/042.gif)  | * Example 042 <br> * Not need a mask <br> * Input image "042.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example042.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![043](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/043.gif)  | * Example 043 <br> * Not need a mask <br> * Input image "043.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example043.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----


![044](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/044.gif)  | * Example 044 <br> * Not need a mask <br> * Input image "044.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example044.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :-----

# Playing with Examples with Masks

![045](https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/045.gif)  | <img src="https://raw.githubusercontent.com/lllyasviel/PaintingLight/master/code/imgs/045.mask.png" width="256" hegiht="256" align=center />  | * Example 045 <br> * Need a mask <br> * Input image "045.jpg" <br>  <br>  <br>  <br> To try it: <br> <br> --- <br> >> python example045.py <br> --- <br>  <br> <br> Image has copyrights.
---- | :----- | :-----

# Playing with Your Own Images

Just try:

    python default.py your_image.png

It is also possible to edit parameters in *default.py*. See codes for detals.

# FAQs

    Q: It is mentioned that this project does not using 
       deep learning, then why it is still required to install tensorflow?
    
    A: This is because we use SRCNN, a tensorflow neural network, to 
       pre-process input images in order to remove JPEG artifacts. Therefore 
       you still need to install tensorflow with a proper version.
<br>

    Q: I am trying with my own images. Can you explain 
       the parameters so that I can get better results?
    
    A: Here we list all possible parameters:
    
    image:                               the input image.
    
    mask:                                a paired mask. you can set it to None as it is optional.
    
    ambient_intensity:                   the environment ambient light intensity. 0.45 recommended.
    
    light_intensity:                     the intensity of your light. 0.85 recommended.
    
    light_source_height:                 the height of your light source. It is the distance 
                                         from the image to your light source. 1.0 recommended.
                                
    gamma_correction:                    the gamma correction parameter. It is a common parameter in 
                                         many digital cameras or smartphone cameras, and we provide 
                                         it if necessary. 1.0 recommended.
                                
    stroke_density_clipping:             a scalar to clip the stroke density. Bigger number results 
                                         in sharper results. 1.2 recommended.
                                
    enabling_multiple_channel_effects:   whether to generate multiple-channel lighting 
                                         effects. True recommended.
                                         
    light_color_red:                     color of your light. 1.0 recommended.
    
    light_color_green:                   color of your light. 1.0 recommended.
    
    light_color_blue:                    color of your light. 1.0 recommended.
<br>

    Q: I am currently trying with flat cell illustrations or line drawings, but 
       the results are bad. Is this method not suitable to line drawings and flat 
       cell illustrations?

    A: This method not suitable to line drawings and flat cell illustrations. This 
       is because the main technique of this algorithm is called stroke density. 
       The algorithm fails if the input image do not contain such strokes or 
       similar patterns.
 <br>
 
    Q: I have tried many parameters but I am still not very satisfied. 
        What can I do to realize the full potential of this algorithm?

    A: If you really need you may manually annotate a mask and use the masked mode. 
       You may see also the code for the “Playing with Examples with Masks” examples.
       
# Citation

    @article{Zhang2020,
       author = "Lvmin Zhang and Edgar Simo-Serra and Yi Ji and Chunping Liu",
       title = "Generating Digital Painting Lighting Effects via RGB-space Geometry",
       journal = "ACM Transactions on Graphics",
       year = "2020"
    }

# 中文社区

我们有一个除了技术什么东西都聊的以技术交流为主的宇宙超一流二次元相关技术交流吹水群“纸片协会”。如果你一次加群失败，可以多次尝试。

    纸片协会总舵：184467946

