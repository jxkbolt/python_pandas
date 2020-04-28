import pandas as pd
import numpy as np
# Series
name=['a','b','c','d']
pse = pd.Series(data=[18, 30, 25, 40], index=name, name="user_age_info", dtype=float)
pse[1],pse['a'],pse[pse>30],pse[[1,3]],pse[:3]
numpy的大多数函数可以对Series使用，但是处理后Series本身的类型不变
np.round(pse),np.sqrt(pse),pse.max(),pse,min(),pse.median(),pse.abs(),pse.mode()
pse.values.argmax()  //返回最大值的索引(数字)
pse+[1,2,3,4]  //返回Series类型，values为[19,32,28,44],index为pse的index;计算方式是pse的index升序后进行计算；如果长度不一致时，则值会以NaN填充(index为left join模式)
pse.values,pse.index
index的元素不能修改，可以重新设置
pse.dtype  //获取数据类型
pse.astype(np.float64)  //修改数据类型，但是pse原本的数据类型不变
计算的特性与数组相同

d={'a':1,'b':2,'c':3,'d':4,'e':5}
# print(pd.Series(d))
'基于索引的数据选择'
print(pd.Series(d,index=list('abcde')))# pandas中数据的选择是基于索引完成的
print(pd.Series(d,index=list('edcba')))# 索引逆序
print(pd.Series(d,index=list('abcabc')))# 索引重复
print(pd.Series(d,index=list('ABCde')))# 索引无法对齐,自动填充缺失值

添加
Series.append()
pse = pd.Series(data=[18, 30, 25, 40], index=list('abcd'), name="user_age_info", dtype=float)
pse.append(np.Series([1,2]),ignore_index=True)  //ignore_index为True，则添加后索引在原Series中继续相加，False则为新添加的数据重新从0开始添加索引

除
se = pd.Series(data=[18, 30, 25, 40], index=list('abcd'), name="user_age_info", dtype=float)
pse.drop('a)  //不修改源对象
del pse['a']  //删除源对象
inplace=True  //参数inplace，表示是否对数据源进行更改

pse.drop_duplicates()  //去重 返回带索引值
pse.unique()  //去重 以数组形式返回
pse.nunique()  //统计非重复数量  与pse.drop_duplicates().count() 等效

判断元素是否存在Serise的值中
18 in pse.values
np.isin()  //一个序列是否在另一个序列中

排序
pse.sort_index(ascending=False)
pse.sort_values()
Series没有count方法

统计元素出现的次数：
Series.value_counts()

Series.rank()  //method : {'average', 'min', 'max', 'first', 'dense'}
    ser.rank(method='min',ascending=False)  'method=min:并列的人排名相同,取最小值'
    ser.rank(method='max',ascending=False)  'method=max:并列的人排名相同,取最大值'
    ser.rank(method='first',ascending=False)  'method=first:并列的人排名相同,按元素出现顺序进行排序'
    ser.rank(method='dense',ascending=False)  'method=dense:并列的人排名相同,不考虑人数,只按去重后的分数排名'
ser.index.tolist() //index转列表
ser.to_dict()  //转字典 

# DataFrame
df=pd.DataFrame(pd.read_excel())
df.index,df.columns,df.values.df.shape,df.dtype
df.index,df.columns  //均为index类型，不可修改元素，只能修改整体

df.info()  //返回数据框的信息
df.describe()  //返回数值字段的统计信息

df[column_name].unique()  //某一列的非重复值

df.head(3)  //查看前3行数据(默认是5行)  df.tail(3) 后三行
df.dropna  //df.dropna(how='any')
df.fillna  //df[column_name].fillna(df.[columns_name].mean()),对na以均值填充,mean,median 
method:{'backfill', 'bfill', 'pad', 'ffill', None}  //填充

df[column_name1]=df[columns_name1].str.lower()  //转小写

//添加两列：
df[[column_name3,column_name4]]=df[[column_name1,column_name2]]*2  //其中column_name1和column_name2的数据类型均为float

df[column_name].astype('int')  //某一字段的属性转成int类型

df.rename与df.columns=[]区别：
    df.rename(columns={old_colname,new_colname})  //rename有inplace选项，代码运行后返回的是一个dataframe
    df.columns=[]  //直接修改原数据的列名，代码运行后什么后不返回

df.duplicated()  //判断是否为重复值
df[column_name].drop_duplicates()  //某行去重
df.drop_duplicates()  //DataFrame去重
df.drop_duplicates(subset=[colname1,colname2])  //按照某几个字段去重
df.drop_duplicates(keep='last')  //last 保留最后一条 ，first保留第一条

df[column_name].replace(old_txt,new_txt)  //替换replace(1,100) replace([1,2,3],4)  replace([1,2],[3,4])
df.replace({1:10,2:20})  //替换
df.replace({'colname1':{1,2},'colname2':{3,4}})  //不同的列不同替换

df3=pd.merge(df1,df2,how='inner')  //两个dataframe合并赋值给df3,how:'left','right','outer','inner'
    参数on/left_on/right_on为多个字段时，用列表表示(如：pd.merge(left,right,on=['key1','key2'],how='left'))；
    参数suffixes：重命名两组数据相同的字段名称，默认在相同的名称后加上_x和_y，可以传入两个参数，自定义suffixes=['_k1','_k2']
    参数indicator：默认情况是False，当为True或其他string的时候，会在生产一个新列说明(默认有both,left_only,right_only)，合并方式
df.set_index(column_name)  //设置索引列
df.sort_values(by=[col_name1,col_name2])/df.sort_values(by=[col_name1,col_name2],ascending=[False,True])  //按照特定的列值进行排序，不知默认排序方式
df.sort_index()  //按照索引进行排序
df.reindex(index=[]) /df.reindex(columns=[])


df.loc[(df_inner['city'] == 'beijing') & (df_inner['price']>= 4000), 'sign']=1  //新建一个sign,符合条件的为1

# 数据的拆分与合并:
split1=pd.DataFrame((x.split('-') for x in df['category']),columns=['category','size'])  //基本拆分
pd.merge(df,split1,right_index=True,left_index=True)  //整合

# 判断数据是否为Nan
pd.isnull(df),pd.notnull(df)
df.dropna(axis=0,how='any'/'all',<inplace>)  //对Na值进行填充;nplace参数默认为False,True时,直接改变df的本身
//筛选某行非空（空）的数据：
    df.loc[df['a'].isnull,:]  df.loc[df['a'].notnull(),:]

# 删除某一列:
df.pop(col_name)  del df[col_name]  //原数据被修改
df.drop(col_names,1)  //删除某列，不修改原数据
df.drop(index_name,0)  //删除某行，不修改原数据
# 删除行
df.drop(index=(df.loc[(df['DataBase']=='test')].index))

# 新增一列:
df[new_colname]=1  //添加一个新列   df[new_colname]=np.where(df['one']>100,'mm','nn') 
user_info.assign(new_colname= user_info["age"] + 1)
Series的添加是根据索引匹配添加的,索引没有匹配上的，则无法添加，只匹配索引对的上的数据，类似left join

%timeit func  //运算效率
df.reset_index()  //重设索引
df=df.ser_index(column_name)  //设置某个字段为索引，字段的要求目前不知
df[col_name].isin(['beijing'])  //判断col_name列的值是否为'beijing',返回布尔值,例如：df.loc[df['city'].isin(['beijing','shanghai'])],筛选city为'beijing','shanghai'的数据
df.query('city == ["beijing", "shanghai"]')  //查询

df.col_name.count()  //统计个数，其中col_name不加引号  df.col_name.sum()
用法：统计全部和：df.sum().sum()

df-[1,2,3]  //假设df中有三列数据,列相加
df.add([1,2,3,4,5]})  //每行相加
df.multiply
df.divide
df.values.tolist()  //DataFrame的values转list

df.shape  //返回各个维度的数量

df.idxmax(0)  //有时间自己看官网说明
