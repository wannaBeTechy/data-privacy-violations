

def post(tweet,api):
    # update the status 
    api.update_status(status = tweet) 
    print('Tweet posted successfully')
    
