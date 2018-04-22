import web

db_host = 'h7xe2knj2qb6kxal.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'zjtej7z42ykytyqn'
db_user = 'c2ay0pah6qj3ljbg'
db_pw = 'h0jurg41tvc84sf4'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )