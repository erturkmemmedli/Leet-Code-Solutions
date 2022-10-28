class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key = lambda x: [x[0],-x[1]])
        if clips[0][0] != 0: return -1
        segments = []
        x, y = clips[0]
        for start, end in clips:
            if not segments:
                segments.append((x, y))
                if segments[-1][1] >= time:
                    return len(segments)
                continue
            if start <= segments[-1][1]:
                if end > y:
                    x, y = start, end
            else:
                if y > segments[-1][1]:
                    segments.append((x, y))
                    if segments[-1][1] >= time:
                        return len(segments)
                    if end > y:
                        x, y = start, end
                else:
                    return -1
        if y > segments[-1][1]:
            segments.append((x, y))
        return len(segments) if segments[-1][1] >= time else -1
