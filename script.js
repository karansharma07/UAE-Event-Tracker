response = requests.get(
    url="https://api.predicthq.com/v1/events",
    headers={
      "Authorization": "Bearer kVMmdcgMaADgkybSkDoFAqVWLBxiEofIRRbdNFNt",
      "Accept": "application/json"
    },
    params= {
    //"active.gte": "2019-12-29",
    //"active.lte": "2021-01-10",
        "country" : "AE"
    }
)