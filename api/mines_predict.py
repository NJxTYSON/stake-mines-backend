from stake_logic import generate_mines_layout

def handler(request):
    try:
        body = request.json()
        server_seed = body["serverSeed"]
        client_seed = body["clientSeed"]
        nonce = int(body["nonce"])
        mines = int(body.get("minesCount", 3))

        bombs = generate_mines_layout(server_seed, client_seed, nonce, mines)

        return {
            "statusCode": 200,
            "body": {
                "status": "success",
                "bombs": bombs,
                "minesCount": mines,
                "mines": None
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }