---
layout: post
title: 校赛题解
subtitle: 
date: 2018-12-24
author: roffett
header-img: img/landscape08.jpg
catalog: true
tags:
    - ACM
    - 校赛
---

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />>

## problem A
<p align="center"><font style="font-size:30px">Calendar</font></p><br />



#### Description:
<div style="font-weight:bold;">
A calendar is a system for measuring time, from hours and minutes, to months and days, and finally to years and centuries. The terms of hour, day, month, year and century are all units of time measurements of a calender system.
According to the Gregorian calendar, which is the civil calendar in use today, years evenly divisible by 4 are leap years, with the exception of centurial years that are not evenly divisible by 400. Therefore, the years 1700, 1800, 1900 and 2100 are not leap years, but 1600, 2000, and 2400 are leap years.
Given the number of days that have elapsed since January 1, 2000 A.D, your mission is to find the date and the day of the week.
</div>

#### Input
<div style="font-weight:bold;">
The input consists of lines each containing a positive integer, which is the number of days that have elapsed since January 1, 2000 A.D. The last line contains an integer -1, which should not be processed. You may assume that the resulting date won't be after the year 9999.
</div>

#### Output
<div style="font-weight:bold;">
For each test case, output one line containing the date and the day of the week in the format of "YYYY-MM-DD DayOfWeek", where "DayOfWeek" must be one of "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" and "Saturday".
</div>

#### Sample Input
<div style="font-weight:bold;">
1730<br />
1740<br />
1750<br />
1751<br />
-1<br />

<br />
</div>

#### Sample Output
<div style="font-weight:bold;">
2004-09-26 Sunday<br />
2004-10-06 Wednesday<br />
2004-10-16 Saturday<br />
2004-10-17 Sunday<br />
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />>

#### 解题思路： 

<div style = "font-size:20px;font-weight:bold;color:black;">
题目的意思很简单，就是让你推算从2000年1月1日后n天的日子是什么，只要注意判断闰年平年，应该没什么难度</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />

### AC代码：
```c++
#include<bits/stdc++.h>

int month[13]={31,28,31,30,31,30,31,31,30,31,30,31};
using namespace std;
int main(){
    int n;
    while(scanf("%d",&n)){
        if(n==-1) break;
        int tmp = n;
        int year=0;
        int j = 2000;
        int last=0;
        while(tmp>0){
            if((year+j)%4==0&&(year+j)%100!=0||(year+j)%400==0){
                tmp-=366;
                year++;
                last=366;
            }
            else{
                tmp-=365;
                year++;
                last=365;
            }
        }
            year--;
            tmp+=last;
            if((year+j)%4==0&&(year+j)%100!=0||(year+j)%400==0){
                month[1]++;
            }
            int mm=0,lasts=0;;
            while(tmp>0){
                tmp-=month[mm];
                lasts=month[mm];
                mm++;
            }
            tmp+=lasts+1;
            
            printf("%d-",year+2000);
            if(mm<10)
            printf("0%d-",mm);
            else{
                printf("%d-",mm);
            }
            if(tmp<10){
                printf("0%d ",tmp);
            }
            else{
                printf("%d ",tmp);
            }
            if(n%7==0)  printf("Saturday\n");
            else if(n%7==1) printf("Sunday\n");
            else if(n%7==2) printf("Monday\n");
            else if(n%7==3) printf("Tuesday\n");
            else if(n%7==4) printf("Wednesday\n");
            else if(n%7==5) printf("Thursday\n");
            else if(n%7==6) printf("Friday\n");
    month[1]=28;
    }

    return 0;
}
```

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />>

## problem B

<p align="center"><font style="font-size:30px">Persistent Bits</font></p><br />



#### Description:
<div style="font-weight:bold;">
WhatNext Software creates sequence generators that they hope will produce fairly random sequences of 16-bit unsigned integers in the range 0-65535. In general a sequence is specified by integers A, B, C, and S, where 1 <= A < 32768, 0 <= B < 65536, 2 <= C < 65536, and 0 <= S < C. S is the first element (the seed) of the sequence, and each later element is generated from the previous element. If X is an element of the sequence, then the next element is<br />
(A * X + B) % C<br />
where '%' is the remainder or modulus operation. Although every element of the sequence will be a 16-bit unsigned integer less than 65536, the intermediate result A*X + B may be larger, so calculations should be done with a 32-bit int rather than a 16-bit short to ensure accurate results.<br />
Some values of the parameters produce better sequences than others. The most embarrassing sequences to WhatNext Software are ones that never change one or more bits. A bit that never changes throughout the sequence is persistent. Ideally, a sequence will have no persistent bits. Your job is to test a sequence and determine which bits are persistent.<br />
For example, a particularly bad choice is A = 2, B = 5, C = 18, and S = 3. It produces the sequence 3, (2*3+5)%18 = 11, (2*11+5)%18 = 9, (2*9+5)%18 = 5, (2*5+5)%18 = 15, (2*15+5)%18 = 17, then (2*17+5)%18 = 3 again, and we're back at the beginning. So the sequence repeats the the same six values over and over:<br />
<span>
Decimal&emsp;&emsp;    16-Bit Binary<br />
3     &emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;         0000000000000011<br />
11    &emsp;&emsp;&emsp;&emsp;    0000000000001011<br />
9     &emsp;&emsp;&emsp;&emsp;&nbsp;    0000000000001001<br />
5     &emsp;&emsp;&emsp;&emsp;&nbsp;   0000000000000101<br />
15    &emsp;&emsp;&emsp;&emsp;     0000000000001111<br />
17    &emsp;&emsp;&emsp;&emsp;     0000000000010001<br />
overall  &emsp;&emsp;  00000000000????1<br />
</span>
The last line of the table indicates which bit positions are always 0, always 1, or take on both values in the sequence. Note that 12 of the 16 bits are persistent. (Good random sequences will have no persistent bits, but the converse is not necessarily true. For example, the sequence defined by A = 1, B = 1, C = 64000, and S = 0 has no persistent bits, but it's also not random: it just counts from 0 to 63999 before repeating.) Note that a sequence does not need to return to the seed: with A = 2, B = 0, C = 16, and S = 2, the sequence goes 2, 4, 8, 0, 0, 0, ....
</div>

#### Input
<div style="font-weight:bold;">
There are from one to sixteen datasets followed by a line containing only 0. Each dataset is a line containing decimal integer values for A, B, C, and S, separated by single blanks.
</div>

#### Output
<div style="font-weight:bold;">
There is one line of output for each data set, each containing 16 characters, either '1', '0', or '?' for each of the 16 bits in order, with the most significant bit first, with '1' indicating the corresponding bit is always 1, '0' meaning the corresponding bit is always 0, and '?' indicating the bit takes on values of both 0 and 1 in the sequence.
</div>

#### Sample Input
<div style="font-weight:bold;">
2 5 18 3<br />
1 1 64000 0<br />
2 0 16 2<br />
256 85 32768 21845<br />
1 4097 32776 248<br />
0<br />

<br />
</div>

#### Sample Output
<div style="font-weight:bold;">
00000000000????1<br />
????????????????<br />
000000000000???0<br />
0101010101010101<br />
0???000011111???<br />
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />>

#### 解题思路： 

<div style = "font-size:20px;font-weight:bold;color:black;">
位运算暴力求解，把计算出的每个S都通过位运算换成2进制进行比较，如果一样则输出该位置的0或1，不一样输出问号。(x>>(15-i)&1)+'0'，将数字快速转化为2进制</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />

### AC代码：
```c++
#include<bits/stdc++.h>

using namespace std;
int f[100010];
char s[20];
char s2[20];
int ans[20];
void binary(int x){
    memset(s,0,sizeof(s));
    for(int i = 0;i<=15;i++){
        s[i]=(x>>(15-i)&1)+'0';
    }
}
void binary2(int x){
    memset(s2,0,sizeof(s2));
    for(int i = 0;i<=15;i++){
        if(s[i]!=(x>>(15-i)&1)+'0'){
            ans[i]='?';
        }
        else{
            if(ans[i]!='?')
            ans[i]=s[i];
        }
    }
}
int main(){
    int A,B,C,S;
    int num = 0;
    while(scanf("%d",&A)&&A){
        num=0;
        memset(ans,0,sizeof(ans));
        memset(f,0,sizeof(f));
        scanf("%d%d%d",&B,&C,&S);
        binary(S);
        while(!f[S]){
            f[S]=1;
            S=((A%C)*(S%C)+(B%C))%C;
            for(int i = 0;i<16;i++){
                int bit =S>>(15-i)&1; 
                if(s[i]!=bit+'0'){
                    ans[i] = '?';
                }
                else{
                    if(ans[i]!='?')
                    ans[i]=s[i];
                }
            }
        }
    for(int i = 0;i<16;i++){
        printf("%c",ans[i]);
    }
    printf("\n");

    }
    return 0;
}
```

## problem C

<p align="center"><font style="font-size:30px">Can you search?</font></p><br />


#### Description:
<div style="font-weight:bold;">
Shimlin loves to play with array. One day she was playing a game of finding the smallest number in an array (a1,...,an) but soon she got bored as the game was too easy for her. She asked her ghost friend to make the game more interesting. After thinking for a while the ghost came up with an idea. The ghost will give her some queries. In each query the ghost will tell her an index number bi that is less than the given array size and Shimlin will have to answer the smallest number among first bi elements of the given array.<br />
<br />
The ghost gave you the responsibility to find the correct answer of each query so that he can match the answer with Shimlin's answer.<br />
</div>

#### Input
<div style="font-weight:bold;">
Input starts with T(1<=T<=100), denoting the number of test case.<br />
Each of the test case contains 3 line. <br />
In the first line there are two positive integer numbers n and q (1<=n<=10^5, 1<=q<=10^5) --  size of the array and number of queries.<br />
<br />
The second line contains n integers a1, a2, ..., an (1<= ai <=10^5) -- elements of the array. <br />
The third line contains q integers b1, b2, ..., bq (1<= bi <=n) --range of query. <br />
<br />
</div>

#### Output
<div style="font-weight:bold;">
For each query print one integer in a line -- the minimum number in that range.<br />
</div>

#### Sample Input
<div style="font-weight:bold;">
2<br />
4 2<br />
2 2 3 1<br />
3 4<br />
5 3<br />
6 7 4 9 2<br />
2 3 5<br />

<br />
</div>

#### Sample Output
<div style="font-weight:bold;">
2<br />
1<br />
6<br />
4<br />
2<br />

</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />>

#### 解题思路： 

<div style = "font-size:20px;font-weight:bold;color:black;">
题意：<br />
输入：<br />
第一行输入T代表T组数据<br />
第二行输入n代表n个数字和q代表q次查找<br />
第三行输入q个数字代表查找前x个数字的最小值<br />
这里我用了一个优先队列来维护，快速查找前x个数字的最小值<br />
<br />
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />

### AC代码：
```c++
#include<bits/stdc++.h>

using namespace std;
int a[100010];
int t[100010];
int ans[100010];
int t2[100010];
using namespace std;
priority_queue<int,vector<int>,greater<int> >q;
int main(){
    int T;
    cin>>T;
    while(T--){
        int n,m;
        while(!q.empty()) q.pop();
        cin>>n>>m;
        for(int i = 0;i<n;i++){
            cin>>a[i];
        }
        for(int i = 0;i<m;i++){
            cin>>t[i];
            t2[i]=t[i];
        }
        sort(t,t+m);
        int j = 0;
        for(int i = 0;i<m;i++){
            while(j!=t[i]){
                q.push(a[j]);
                j++;
            }
            ans[t[i]]=q.top();
        }
        for(int i = 0;i<m;i++){
            cout<<ans[t2[i]]<<endl;
        }
    }
    return 0;
}
```

## problem D


<p align="center"><font style="font-size:30px">素数</font></p><br />


#### Description:
<div style="font-weight:bold;">
输入一个整数，输出是否是素数的消息。
</div>

#### Input
<div style="font-weight:bold;">
一个正整数n(n<2^31)
</div>

#### Output
<div style="font-weight:bold;">
如果是素数输出prime 如果不是输出not prime
</div>

#### Sample Input
<div style="font-weight:bold;">
97
<br />
</div>

#### Sample Output
<div style="font-weight:bold;">
prime
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />>

#### 解题思路： 

<div style = "font-size:20px;font-weight:bold;color:black;">
签到题
<br />
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />

### AC代码：
```c++
#include<bits/stdc++.h>

using namespace std;
int main(){
    int n;
    int flag= 0;
    while(cin>>n){
        flag=0;
        for(int i = 2;i<=sqrt(n);i++){
            if(n%i==0) {flag = 1;break;}
        }
        if(flag==1) printf("not prime\n");
        else printf("prime\n");
    }
    return 0;
}

```

## problem E


<p align="center"><font style="font-size:30px">幸运数排序</font></p><br />


#### Description:
<div style="font-weight:bold;">
ZZX非常喜欢数字6，他认会数字6是他的幸运数，会给他带来好运。现在ZZX对一些数字作如下排序：包含数字“6”多的排在前面，如果两个数包含一样多的“6”，则 数字大的排在前面。 <br />
你知道他最后把数字们排成什么样子了吗？ <br />
</div>

#### Input
<div style="font-weight:bold;">
第一行一个整数n（1<=n<=100000）  <br />
第二行n个整数，每个整数不超过100000。  <br />
对于30%的数据，1<=n<=1000。  <br />
对于100%的数据，1<=n=100000。  <br />
</div>

#### Output
<div style="font-weight:bold;">
一行，输出排序后的n个数，相邻数字用空格' '隔开。 
</div>

#### Sample Input
<div style="font-weight:bold;">
5<br />
12345 66666 23 66 1926
<br />
</div>

#### Sample Output
<div style="font-weight:bold;">
66666 66 1926 12345 23
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />>

#### 解题思路： 

<div style = "font-size:20px;font-weight:bold;color:black;">
除10取余统计一下6的个数 ，然后用sort排序一下就好了
<br />
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />

### AC代码：
```c++
#include<bits/stdc++.h>

using namespace std;
struct number{
    int num;
    int six;
}n[100010];
int cmp(number a,number b){
    if(a.six==b.six) return a.num>b.num;
    else return a.six>b.six;
}
int main(){
    int q;
    cin>>q;
    memset(n,0,sizeof(n));
    for(int i = 0 ;i<q;i++){
        cin>>n[i].num;
        int tmp = n[i].num;
        while(tmp>0){
            if(tmp%10==6) n[i].six++;
            tmp/=10;
        }
    }
    sort(n,n+q,cmp);
    for(int i = 0 ;i<q-1;i++){
        cout<<n[i].num<<" ";
    }
    cout<<n[q-1].num<<endl;
    
return 0;
}

```

## problem F


<p align="center"><font style="font-size:30px">统计水洼</font></p><br />



#### Description:
<div style="font-weight:bold;">
有一块N×M的土地，雨后积起了水，有水标记为‘W’，干燥为‘.’。八连通的积水被认为是连接在一起的。请求出院子里共有多少水洼？ 
<br />
</div>

#### Input
<div style="font-weight:bold;">
第一行为N,M(1≤N,M≤110)。 <br />
下面为N*M的土地示意图。 <br />
</div>

#### Output
<div style="font-weight:bold;">
一行，共有的水洼数。 
</div>

#### Sample Input
<div style="font-weight:bold;">
10 12<br />
W........WW.<br />
.WWW.....WWW<br />
....WW...WW.<br />
.........WW.<br />
.........W..<br />
..W......W..<br />
.W.W.....WW.<br />
W.W.W.....W.<br />
.W.W......W.<br />
..W.......W.<br />

<br />
</div>

#### Sample Output
<div style="font-weight:bold;">
3
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />>

#### 解题思路： 

<div style = "font-size:20px;font-weight:bold;color:black;">
比赛的时候看错了题目，把W看成了干燥地，然后把.看成了湿润的地面，然后半天没把样例看懂，我以为算图的联通分支数然后一直没有管他了，后来一看就一个很简单的DFS。找到W的地方，然后把W周围8个位置都变成.就可以了。最后统计一下搜索的次数就可以了。
<br />
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />

### AC代码：
```c++

#include<bits/stdc++.h>
using namespace std;
int N,M;
char s[120][120];
 int dire[8][2]={ {1,0},{-1,0},{0,1},{0,-1},{1,1},{-1,-1},{-1,1},{1,-1}};
void dfs(int x,int j){
    for(int i = 0;i<8;i++){
        if(x+dire[i][0]<0||x+dire[i][0]>N||j+dire[i][1]<0||j+dire[i][1]>M) continue;
        if(s[x+dire[i][0]][j+dire[i][1]]=='W'){
        s[x+dire[i][0]][j+dire[i][1]]='.';
        dfs(x+dire[i][0],j+dire[i][1]);
        }
    }
    return;
}
int main(){
    scanf("%d%d",&N,&M);
    getchar();
    for(int i = 0;i<N;i++){
        for(int j = 0;j<M;j++){
            cin>>s[i][j];
        }
    }
    int sum=0;
    for(int i = 0;i<N;i++){
        for(int j = 0;j<M;j++){
            if(s[i][j]=='W'){
                sum++;
                dfs(i,j);
            }
        }
    }
    printf("%d\n",sum);

    return 0;
}
```

## problem G


<p align="center"><font style="font-size:30px">流感传染</font></p><br />



#### Description:
<div style="font-weight:bold;">
有一批易感人群住在网格状的宿舍区内，宿舍区为n*n的矩阵，每个格点为一个房间，房间里可能住人，也可能空着。在第一天，有些房间里的人得了流感，以后每天，得流感的人会使其邻居（住在其上、下、左和右房间的人）传染上流感，（已经得病的不变），空房间不会传染。请输出第m天得流感的人数。  <br />
</div>

#### Input
<div style="font-weight:bold;">
第一行一个数字n，n不超过100，表示有n*n的宿舍房间。 <br />
接下来的n行，每行n个字符，’.’表示第一天该房间住着健康的人，’#’表示该房间空着，’@’表示第一天该房间住着得流感的人。 <br />
接下来的一行是一个整数m，m不超过100。 <br />

</div>

#### Output
<div style="font-weight:bold;">
输出第m天，得流感的人数。 
</div>

#### Sample Input
<div style="font-weight:bold;">
5<br />
....#<br />
.#.@.<br />
.#@..<br />
#....<br />
.....<br />
4<br />
<br />
</div>

#### Sample Output
<div style="font-weight:bold;">
16
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />>

#### 解题思路： 

<div style = "font-size:20px;font-weight:bold;color:black;">
	很简单的题目硬是把我卡了3小时，不知道为什么cin.getline()一行一行读入就WA了，而cin一个一个读入就AC了，如果按照题目说的给的数据是一行一行的，cin,getline()不应该是错的。
这个题目思路上是非常的简单，我的写法就是把前一天感染的入队即可。先把初始状态下的感染者坐标入队，然后第一天让这些感染者出队，并且感染，并且记下这些被感染者的坐标，等队列为空后就说明这一天的感染者已经感染完了，然后再将被感染者入队。
<br />
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />

### AC代码：
```c++
#include<bits/stdc++.h>

using namespace std;
char s[110][110];
struct locate{
    int x,y;
}lo[100010];
int dire[4][2]={ {1,0},{-1,0},{0,-1},{0,1}};
queue<pair<int,int> >q;
int main(){
    int n;
    while(!q.empty()) q.pop();
    int sum = 0;
    scanf("%d",&n);
    getchar();
    int count = 0;
    for(int i = 0;i<n;i++){
        //cin.getline(s[i],n+1);
        for(int j = 0;j<n;j++){
            cin>>s[i][j];
            if(s[i][j]=='@'){
                lo[count].x=i;
                lo[count].y=j;
                count++;
            }
        }
    }
    for(int i = 0;i<n;i++)
    cout<<strlen(s[i])<<endl;
    int day;
    scanf("%d",&day);
    for(int x = 0;x<day-1;x++){
        for(int j = 0;j<count;j++){
            q.push(make_pair(lo[j].x,lo[j].y));
        }
        count = 0;
        while(!q.empty()){
            int t1=q.front().first;
            int t2=q.front().second;
            q.pop();
            for(int i = 0;i<4;i++){
                if(t1+dire[i][0]<0||t1+dire[i][0]>n||t2+dire[i][1]<0||t2+dire[i][1]>n) continue;
                if(s[t1+dire[i][0]][t2+dire[i][1]]=='.'){
                    s[t1+dire[i][0]][t2+dire[i][1]]='@';
                    lo[count].x=t1+dire[i][0];
                    lo[count].y=t2+dire[i][1];
                    count++;
                }
            }
        }
    }
    for(int i = 0;i<n;i++){
        for(int j = 0;j<n;j++){
            if(s[i][j]=='@') sum++;
        }
    }
    printf("%d\n",sum);
    return 0;
}

```

## problem H


<p align="center"><font style="font-size:30px">青蛙跳河</font></p><br />



#### Description:
<div style="font-weight:bold;">
青蛙王国的运动会开始了！青蛙FY参加了今天的跳河比赛，这个项目要求青蛙们跳过河。河流的宽度为L（1<=L<=100000）。从河流一侧到另一侧，有N（1<=N<=5000）个石头排成一条直线。青蛙可以跳到石头上，但如果青蛙跳到河里就出局了。比赛要求青蛙最多跳跃M（1<=M<=N+1）次。 <br />
FY想知道他要完成过河，它要具备怎样的跳跃能力（即最远跳跃距离）。 <br />
</div>

#### Input
<div style="font-weight:bold;">
输入数据包含多组。<br /> 
每组数据第一行三个整数L，N，M。接下来N行，代表起点距离各块石头的距离。没有两块石头离起点一样远。 <br />
</div>

#### Output
<div style="font-weight:bold;">
对于每组数据输出一个整数，表示FY最远跳跃距离最少是多少。 
</div>

#### Sample Input
<div style="font-weight:bold;">
6 1 2<br />
2<br />
25 3 3<br />
11 <br />
2<br />
18
<br />
</div>

#### Sample Output
<div style="font-weight:bold;">
4<br />
11<br />
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />>

#### 解题思路： 

<div style = "font-size:20px;font-weight:bold;color:black;">
这个题目应该是所有里面最难想的，用的是二分法。一开始我以为用优先队列维护可以做，发现要连续的两个点才能合并，所以只能二分法，二分的话就是从0到终点这个范围内开始寻找，要求满足2个条件:<br />
1.跳远的距离尽可能短<br />
2.跳远的次数必须要小于给定的次数<br />
<br />
所以写代码的时候就要注意：如果跳远的次数要超过限定次数才能到达终点说明给的值太小了，二分法的话就要把low=mid+1，如果发现可以跳的到终点那么就在找找是不是可以有距离更小的满足条件，那么就high=mid-1<br />
这个题目就这样<br />
<br />
</div>

<hr style="height:10px;border:none;border-top:10px groove skyblue;" />

### AC代码：
```c++
#include<bits/stdc++.h>

using namespace std;
int L,N,M;
int a[100010];
bool judge(int mid){
    int i=0,j_times=0,stone=0;
    while(i<=N){
        if(++j_times>M||a[i]-stone>mid)
        return false;
        while(i<=N&&a[i]-stone<=mid)
        i++;
        stone=a[i-1];
    }
    return true;
}
int main(){
    while(cin>>L>>N>>M){
        for(int i = 0;i<N;i++){
            cin>>a[i];
        }
        a[N]= L;
        sort(a,a+N+1);
        int mid,low=0,high=L;
        while(low<=high){
            mid = (low+high)/2;
            if(judge(mid))
                high=mid-1;
            else
                low=mid+1;
        }
        printf("%d\n",low);
    }
    return 0;
}

```