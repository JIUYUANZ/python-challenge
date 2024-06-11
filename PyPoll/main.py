import os
import csv

csv_file=os.path.join("PyPoll","Resources","election_data.csv")

with open(csv_file) as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    print(csv_reader)

    csv_header=next(csv_reader)
    print("Header:",csv_header)

    total_vote=0
    candidates=[]
    Charles_vote=0
    Diana_vote=0
    Raymon_vote=0


    for row in csv_reader:
       total_vote=total_vote+1
       candidates_name=str(row[2])

       if candidates_name not in candidates:
        candidates.append(str(candidates_name))

       if candidates_name=="Charles Casper Stockham":
          Charles_vote += 1
       elif candidates_name=="Diana DeGette":
          Diana_vote +=1
       elif candidates_name=="Raymon Anthony Doane":
          Raymon_vote +=1
    
    Charles_percent=str(round(int(Charles_vote)/int(total_vote)*100,3))+"%"
    Diana_percent=str(round(int(Diana_vote)/int(total_vote)*100,3))+"%"
    Raymon_percent=str(round(int(Raymon_vote)/int(total_vote)*100,3))+"%"
    
print("Election Results")
print("-------------------------")
print("Total Votes:", int(total_vote))    
#print(candidates)
print("-------------------------")
print(
       f"Charles Casper Stockham: {Charles_percent} ({Charles_vote})\n"
       f"Diana DeGette:  {Diana_percent} ({Diana_vote})\n"
       f"Raymon Anthony Doane: {Raymon_percent} ({Raymon_vote})\n"
    )
condition_statement = ""

if Charles_vote > Diana_vote and Charles_vote > Raymon_vote:
   winner="Charles Casper Stockham"
elif Diana_vote > Charles_vote and Diana_vote > Raymon_vote:
   winner="Diana DeGette"
else:
   winner="Raymon Anthony Doane"

result=f"Winner: {winner}"
print("-------------------------")
print(result)
print("-------------------------")

analysis_output=(
   f"Election Results\n"
   f"-------------------------\n"
   f"Total Votes: {int(total_vote)}\n"
   f"-------------------------\n"
   f"Charles Casper Stockham:  {Charles_percent}  ({Charles_vote})\n"
   f"Diana DeGette:  {Diana_percent}  ({Diana_vote})\n"
   f"Raymon Anthony Doane:  {Raymon_percent}  ({Raymon_vote})\n"
   f"-------------------------\n"
   f"{result}\n"
   f"-------------------------\n"
)
   
output_path=os.path.join("PyPoll","analysis","analysis_vote.txt")
with open(output_path,"w",newline="") as txt_file:
   txt_file.write(analysis_output)