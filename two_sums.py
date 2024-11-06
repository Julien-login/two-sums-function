# Funktion zur Berechnung der Indizes zweier Summanden
def two_sums(l: list[int], target: int) -> (int, int):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == target:
                return (i, j)
    return None

# Test: Diese Funktion gibt die Indizes zweier Summanden zurück
