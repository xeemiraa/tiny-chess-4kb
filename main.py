#!/usr/bin/env python3
import sys,json,os
from pathlib import Path
B=[0]*64
V=[0,100,320,330,500,900]
def F(s):return s&7
def R(s):return s>>3
def P(b,s,p):
 d=-8 if p<0 else 8;r=R(s);M=[]
 if S(s+d)and not b[s+d]:M.append((s,s+d,1 if R(s+d)==(0 if p<0 else 7)else 0))
 if r==(6 if p<0 else 1)and S(s+2*d)and not b[s+2*d]:M.append((s,s+2*d,0))
 for f in[-1,1]:
  c=s+d+f
  if S(c):
   t=b[c]
   if t and((p<0 and t>0)or(p>0 and t<0)):M.append((s,c,0))
 return M
def N(s):
 return[s+i for i in[-17,-15,-10,-6,6,10,17,15]if S(s+i)and abs(F(s+i)-F(s))+abs(R(s+i)-R(s))==3]
def B(b,s,p):
 M=[]
 for d in[-9,-7,7,9]:
  s2=s+d
  while S(s2):
   if abs(F(s2)-F(s))!=abs(R(s2)-R(s)):break
   t=b[s2]
   if not t:M.append(s2)
   elif(t<0 and p>0)or(t>0 and p<0):M.append(s2);break
   s2+=d
 return M
def Q(b,s,p):
 M=[]
 for d in[-1,1,-8,8]:
  s2=s+d
  while S(s2):
   t=b[s2]
   if not t:M.append(s2)
   elif(t<0 and p>0)or(t>0 and p<0):M.append(s2);break
   s2+=d
 for d in[-9,-7,7,9]:
  s2=s+d
  while S(s2):
   if abs(F(s2)-F(s))!=abs(R(s2)-R(s)):break
   t=b[s2]
   if not t:M.append(s2)
   elif(t<0 and p>0)or(t>0 and p<0):M.append(s2);break
   s2+=d
 return M
def Kb(s):
 return[s+i for i in[-9,-8,-7,-1,1,7,8,9]if S(s+i)and abs(F(s+i)-F(s))+abs(R(s+i)-R(s))==1]
def Gn(b,p):
 M=[]
 for s in range(64):
  t=b[s]
  if not t:continue
  if(t>0 and p==0)or(t<0 and p==1):
   o=abs(t)
   if o==1:M+=P(b,s,p)
   elif o==2:M+=N(s)
   elif o==3:M+=B(b,s,p)
   elif o==4:M+=Q(b,s,p)
   elif o==6:M+=Kb(s)
 return M
def Ev(b):
 v=0
 for i in range(64):
  p=b[i]
  if p:v+=V[abs(p)]*(1 if p>0 else-1)
 return v
def Chk(b,p):
 for s in range(64):
  if b[s]==(6 if p==0 else-6):
   for m in Gn(b,1-p):
    if m[0]==s:return True
 return False
def Mv2(b,m):
 f,t,m2=m
 b[f]=0
 b[t]=6 if b.s==0 else-6
 b.s=1-b.s
def MM(b,d,a,B,my):
 if d==0:return Ev(b)
 M=Gn(b,my)
 if not M:return 99999 if my==0 else-99999
 if my==0:
  b2=-9999
  for m in M:
   n=b[:]
   n[m[0]]=0
   n[m[1]]=6
   n.s=1
   v=MM(n,d-1,a,B,1)
   if v>b2:b2=v
   a=max(a,v)
   if b2>=B:break
  return b2
 else:
  b2=9999
  for m in M:
   n=b[:]
   n[m[0]]=0
   n[m[1]]=-6
   n.s=0
   v=MM(n,d-1,a,B,0)
   if v<b2:b2=v
   B=min(B,v)
   if b2<=B:break
  return b2
def BM(b,d=3):
 M=Gn(b,b.s)
 if not M:return None
 if b.s==0:
  mm=-9999;v=None
  for m in M:
   n=b[:]
   n[m[0]]=0
   n[m[1]]=6
   n.s=1
   v=MM(n,d-1,-9999,9999,1)
   if v>mm:mm=v;bm=m
  return bm
 else:
  mm=9999;v=None
  for m in M:
   n=b[:]
   n[m[0]]=0
   n[m[1]]=-6
   n.s=0
   v=MM(n,d-1,-9999,9999,0)
   if v<mm:mm=v;bm=m
  return bm
def main():
 inp=Path("/input");out=Path("/output")
 state={}
 if inp.exists():
  for f in inp.iterdir():
   if f.suffix=='.json':
    try:state=json.loads(f.read_text());break
    except:pass
 if state.get('fen'):
  b=[0]*64
  parts=state['fen'].split()
  brd=parts[0];r=7
  for row in brd.split('/'):
   c=0
   for ch in row:
    if ch.isdigit():c+=int(ch)
    else:
     p=ord(ch)-64 if ch.isupper() else-(ord(ch)-96)
     if p>6:p=6
     if p<-6:p=-6
     b[r*8+c]=p;c+=1
   r-=1
  if len(parts)>1:b.s=0 if parts[1]=='w'else 1
  if len(parts)>2:
   c=parts[2]
   if'K'in c:b.castling|=1
   if'Q'in c:b.castling|=2
   if'k'in c:b.castling|=4
   if'q'in c:b.castling|=8
  if len(parts)>3 and parts[3]!='-':
   try:
    f=int(parts[3][0])-1
    r=7 if b.s==0 else 2
    b.ep=r*8+f
   except:b.ep=-1
 else:b.s=0;b.ep=-1
 m=BM(b,3)
 if m is None:print("No moves");sys.exit(0)
 out.mkdir(parents=True,exist_ok=True)
 with open(out/"move.json",'w') as f:
  json.dump({'from':m[0],'to':m[1],'promotion':m[2]},f)
 print(f"Move:{m[0]}->{m[1]}")
if __name__=="__main__":main()
