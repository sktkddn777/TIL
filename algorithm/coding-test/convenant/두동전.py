from collections import deque

def bfs(arr, lst):
    move_dic = {}
    queue = deque([lst])
    move_dic[lst] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while(queue):
        c1_x, c1_y, c2_x, c2_y = queue.popleft()
        if move_dic[(c1_x, c1_y, c2_x, c2_y)] >= 10:
            return -1

        for i in range(4):
            t_c1_x = c1_x + dx[i]
            t_c1_y = c1_y + dy[i]
            t_c2_x = c2_x + dx[i]
            t_c2_y = c2_y + dy[i]

            if ((0 <= t_c1_x < len(arr)) and (0 <= t_c1_y < len(arr[0]))) and ((0 <= t_c2_x < len(arr)) and (0 <= t_c2_y < len(arr[0]))):
                if arr[t_c1_x][t_c1_y] == '#':
                    t_c1_x = c1_x
                    t_c1_y = c1_y
                
                if arr[t_c2_x][t_c2_y] == '#':
                    t_c2_x = c2_x
                    t_c2_y = c2_y
            
            if (not ((0 <= t_c1_x < len(arr)) and (0 <= t_c1_y < len(arr[0]))) and ((0 <= t_c2_x < len(arr)) and (0 <= t_c2_y < len(arr[0])))):
                return move_dic[(c1_x, c1_y, c2_x, c2_y)] + 1
            
            elif (((0 <= t_c1_x < len(arr)) and (0 <= t_c1_y < len(arr[0]))) and not((0 <= t_c2_x < len(arr)) and (0 <= t_c2_y < len(arr[0])))):
                return move_dic[(c1_x, c1_y, c2_x, c2_y)] + 1

            elif (((0 <= t_c1_x < len(arr)) and (0 <= t_c1_y < len(arr[0]))) and ((0 <= t_c2_x < len(arr)) and (0 <= t_c2_y < len(arr[0])))):
                if (t_c1_x, t_c1_y, t_c2_x, t_c2_y) not in move_dic:
                    move_dic[(t_c1_x, t_c1_y, t_c2_x, t_c2_y)] = move_dic[(c1_x, c1_y, c2_x, c2_y)] + 1
                    queue.append((t_c1_x, t_c1_y, t_c2_x, t_c2_y))
    
    return -1

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(input()))

    coin_loc = []

    for x in range(N):
        for y in range(M):
            if arr[x][y] == 'o':
                coin_loc += [x, y]
    
    print(bfs(arr, tuple(coin_loc)))

    