<!--
 * @Author              : Uncle Bean
 * @Date                : 2020-01-21 11:29:40
 * @LastEditors         : Uncle Bean
 * @LastEditTime        : 2020-01-21 11:39:03
 * @FilePath            : \docs\standard\os.md
 * @Description         : 
 -->
# os.walk()
os.walk方法用于遍历目录和文件，简单易用，可以帮助我们高效的处理目录、文件方面的事情

语法格式如下：

```python
os.walk(top=r"C:\Temp\TxGameDownload", topdown=True, onerror=None, followlinks=False)
```

- top：你要遍历的目录地址，如C:\Temp\TxGameDownload

- topdown：可选（默认为True），为True则优先遍历top目录，否则优先遍历top的子目录

- onerror：可选（默认为None），Callable对象，需要异常时调用

- followlinks：可选（默认为False），为True则会遍历目录下的快捷方式实际所指向的目录（注：windows下不生效，followlinks依赖于os.path.isdir和os.path.islink，很可惜，在windows下快捷方式返回的都是False）

- ​返回结果：返回的是一个包含三元组dirpath, dirnames, filenames的Directory tree generator


简单例子：

```python
for root, dirs, files in os.walk(r"C:\Temp\TxGameDownload"):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
```