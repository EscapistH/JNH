## 2019/12/3
终于解决update页面bug，原因是前端取值时写错参数

属于眼神不好导致的bug，(该去看眼睛了`/逃`)

## 2019/12/2
美化`index`页面的显示

完成了``photo``页面的布局，效果还算满意

> 16点03分 预计今天能完成`文章`页面的所有后台逻辑
>  
> 2019年12月3日 00点01分 更新
>
> `文章`页面`update`(`修改`)方法仍有bug，  
> 数据无法从后台传给到前端，先睡觉了，天亮再慢慢调bug
>
> 2019年12月3日 23点46分 更新
>
> bug解决了，眼神不好导致的bug，心态炸裂

## 2019/12/1
按功能将`文章`所有页面文件合并在一个目录`articles`中

将`图片`所有页面合并在目录`photos`中

对`文章`所有页面进行二次美化

## 2019/11/30
参考官方文档及各类博客，使用`flask`的蓝图`Blueprint`

将视图函数单独抽出为单个文件`views.py`

模型类单独抽出为单个文件`models.py`

## 2019/11/29
决定采用MVC架构

使用`flask`作为web框架
 
使用`flask-sqlAlchemy`作为orm模块 

搭建页面，并进行美化，完成部分`文章`部分后台逻辑代码


## 2019/11/28
启动项目，作为女朋友回家期间打发时间的活动

预计开发功能：

* 图片部分
    * 图片的展示
    * 图片的上传
    
* 文章部分
    * 文章的展示
    * 文章的添加
    * 文章的修改
    * 文章的删除