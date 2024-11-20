class AuthenticationManager {
    LinkedList<String> tokenList;
    HashSet<String> expiredTokens;
    HashMap<String, Integer> tokenMap;
    int timeToLive;

    public AuthenticationManager(int timeToLive) {
        this.timeToLive = timeToLive;
        this.tokenList = new LinkedList<>();
        this.tokenMap = new HashMap<>();
    }
    
    public void generate(String tokenId, int currentTime) {
        tokenList.add(tokenId);
        tokenMap.put(tokenId, currentTime + timeToLive);
    }
    
    public void renew(String tokenId, int currentTime) {
        clearExpiredTokens(currentTime);
        if (!tokenMap.containsKey(tokenId)) {
            return;
        }
        tokenList.remove(tokenId);
        tokenList.add(tokenId);
        tokenMap.put(tokenId, currentTime + timeToLive);
    }
    
    public int countUnexpiredTokens(int currentTime) {
        clearExpiredTokens(currentTime);
        return tokenMap.size();
    }

    public void clearExpiredTokens(int currentTime) {
        while (!tokenList.isEmpty()) {
            String id = tokenList.peek();
            if (!tokenMap.containsKey(id) || tokenMap.get(id) <= currentTime) {
                tokenMap.remove(id);
                tokenList.removeFirst();
            } else {
                break;
            }
        }
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager obj = new AuthenticationManager(timeToLive);
 * obj.generate(tokenId,currentTime);
 * obj.renew(tokenId,currentTime);
 * int param_3 = obj.countUnexpiredTokens(currentTime);
 */
