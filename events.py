import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events",
    headers={
      "Authorization": "Bearer kVMmdcgMaADgkybSkDoFAqVWLBxiEofIRRbdNFNt",
      "Accept": "application/json"
    },
    params={
      "country": "AE"
    }
)

print(response.json())