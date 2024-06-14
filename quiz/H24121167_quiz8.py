import csv

# 讀取CSV檔案
with open('pe8_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# 問題1: 東區哪些球隊的主場勝率低於客場勝率
print("問題1: 東區主場勝率低於客場勝率的球隊")
eastern_teams = [team for team in data if team['Conference'] == 'Eastern']
for team in eastern_teams:
    home_record = team['HOME'].split('-')
    away_record = team['AWAY'].split('-')
    home_win_pct = int(home_record[0]) / (int(home_record[0]) + int(home_record[1]))
    away_win_pct = int(away_record[0]) / (int(away_record[0]) + int(away_record[1]))
    if home_win_pct < away_win_pct:
        print(team['Team'])

# 問題2: 哪一區的球隊擁有較高的"平均得分減掉失分"
print("\n問題2: 哪一區的球隊擁有較高的\"平均得分減掉失分\"")
eastern_pf_pa = [float(team['PF']) - float(team['PA']) for team in data if team['Conference'] == 'Eastern']
western_pf_pa = [float(team['PF']) - float(team['PA']) for team in data if team['Conference'] == 'Western']
eastern_avg_pf_pa = sum(eastern_pf_pa) / len(eastern_pf_pa)
western_avg_pf_pa = sum(western_pf_pa) / len(western_pf_pa)
if eastern_avg_pf_pa > western_avg_pf_pa:
    print("東區的球隊擁有較高的\"平均得分減掉失分\"")
else:
    print("西區的球隊擁有較高的\"平均得分減掉失分\"")

# 問題3: 根據每支球隊的整體勝率來排序
print("\n問題3: 根據每支球隊的整體勝率來排序")
team_rankings = {}
for team in data:
    win_loss_record = team['W-L'].split('-')
    wins = int(win_loss_record[0])
    losses = int(win_loss_record[1])
    team_rankings[team['Team']] = wins / (wins + losses)

sorted_rankings = sorted(team_rankings.items(), key=lambda x: x[1], reverse=True)
for rank, (team, win_pct) in enumerate(sorted_rankings, start=1):
    print(f"{rank}. {team}: {win_pct:.3f}")
