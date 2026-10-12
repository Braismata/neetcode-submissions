class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        # Un paso atrás (n-1) y dos pasos atrás (n-2)
        uno_atras, dos_atras = 2, 1
        
        # Calculamos de forma iterativa hacia arriba
        for _ in range(3, n + 1):
            actual = uno_atras + dos_atras
            dos_atras = uno_atras
            uno_atras = actual
            
        return uno_atras