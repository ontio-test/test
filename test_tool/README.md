# Ontology python测试框架简介  
### 一、    简介  
本工具是针对本体节点开发的一套测试工具。针对webapi，合约api，合约调用，分润等一系列测试要求，工具能测试并收集测试结果。  
本工具以自动为主，手动为辅。  

工具主要分4大部分：  

1.  客户端测试框架  
a)	实现不同通讯协议  
b)	实现跨节点通讯  
c)	常用api的定制  
d)	结果判断  
e)	LOG的记录  
2.	客户端测试用例脚本  
利用测试框架，针对不同的测试场景和要求，实现的测试脚本  
3.	服务端测试工具  
实现必须要在节点服务器上的相关操作 。如：节点一致性判断，停止/启动节点等。  

### 二、	部署要求
平台：linux  
Python版本：3x，2x  
### 三、文档分布  
关于本系统如何使用，请参考[**document/ontology python测试框架基础使用介绍.pdf**](https://github.com/ontio-test/test/blob/master/test_tool/document/ontology%20python%E6%B5%8B%E8%AF%95%E6%A1%86%E6%9E%B6%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%E4%BB%8B%E7%BB%8D.pdf)。  
关于本系统的框架api及详细介绍，请参考[**document/ontology python测试框架api及测试用例详细介绍.pdf**](https://github.com/ontio-test/test/blob/master/test_tool/document/ontology%20python%E6%B5%8B%E8%AF%95%E6%A1%86%E6%9E%B6api%E5%8F%8A%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B%E8%AF%A6%E7%BB%86%E4%BB%8B%E7%BB%8D.pdf)。  
关于本系统的设计文档，请参考[**document/TN_ONT.pdf**](https://github.com/ontio-test/test/blob/master/test_tool/document/TN_ONT.pdf)。



