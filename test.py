import pyupbit

access = "kNBnIMzfx2xjslIxedUbL3KWFsJTf3zBZH3XRK3t"          # 본인 값으로 변경
secret = "YHxRqGSr7uRLME1yaUeNxVoCUzswOoxDs6dODgRG"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회