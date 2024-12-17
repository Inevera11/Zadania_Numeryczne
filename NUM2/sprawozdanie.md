---
Author: 'Zuzanna Bożek'
---

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

### Cel

Używając wybranego pakietu algebry komputerowej lub biblioteki numerycznej, rozwiąż równania macierzowe:
$$ A_iy = b $$
dla i = 1, 2. Ponadto, rozwiąż analogiczne równania z zaburzonym wektorem wyrazów
wolnych 
$$A_iy = b + \Delta b$$
Zaburzenie $\Delta b$ wygeneruj jako losowy wektor o małej normie euklidesowej (np. $\| \Delta b \|_2 \approx 10^{-6}$). Przeanalizuj jak wyniki dla macierzy A1 i A2 zależą od ∆b i zinterpretuj zaobserwowane
różnice.

### Analiza zadania

Zadane są macierze symetryczne 5x5:

$$
A_1 = \begin{pmatrix}
5.8267103432 & 1.0419816676 & 0.4517861296 & -0.2246976350 & 0.7150286064 \\
1.0419816676 & 5.8150823499 & -0.8642832971 & 0.6610711416 & -0.3874139415 \\
0.4517861296 & -0.8642832971 & 1.5136472691 & -0.8512078774 & 0.6771688230 \\
-0.2246976350 & 0.6610711416 & -0.8512078774 & 5.3014166511 & 0.5228116055 \\
0.7150286064 & -0.3874139415 & 0.6771688230 & 0.5228116055 & 3.5431433879
\end{pmatrix}
$$

$$
A_2 = \begin{pmatrix}
5.4763986379 & 1.6846933459 & 0.3136661779 & -1.0597154562 & 0.0083249547 \\
1.6846933459 & 4.6359087874 & -0.6108766748 & 2.1930659258 & 0.9091647433 \\
0.3136661779 & -0.6108766748 & 1.4591897081 & -1.1804364456 & 0.3985316185 \\
-1.0597154562 & 2.1930659258 & -1.1804364456 & 3.3110327980 & -1.1617171573 \\
0.0083249547 & 0.9091647433 & 0.3985316185 & -1.1617171573 & 2.1174700695
\end{pmatrix}
$$

oraz wektor b:

$$
b = \left( \begin{array}{ccccc}−2.8634904630& −4.8216733374& −4.2958468309& −0.0877703331& −2.0223464006\end{array} \right)^T
$$

Do rozwiązania mamy układ równań:

$$
Ay = b
$$

oraz układ z zaburzonym b:

$$
A\tilde{y} = b + \Delta b
$$

Do określenia jak bardzo względny błąd wyniku różni się od błędu względnego samej różnicy wartości dokładnej $b$ i jej przybliżenia posłużymy się współczynnikiem uwarunkowania $\kappa$.

$$
 \frac{\| \tilde{y} - y \|}{\| y \|}  \leq \kappa \cdot \frac{\| \Delta b \|}{\| b \|}
$$

Ponieważ macierze $A_1$ i $A_2$ są symetryczne i rzeczywiste, $\kappa$ można wyrazić jako:

$$
\kappa = \frac{max |\lambda|}{min |\lambda|}
$$

gdzie $\lambda$ oznacza wartości własne macierzy.

### Przebieg zadania dla macierz $A_1$

Obliczeń dokonano z użyciem biblioteki pythonowej numpy,
pełny program jest dostępny w pliku `matrix1.py`.

Najpierw obliczono $A_1y_1 = b$ i otrzymano wynik:

$$
y_1 = \left( \begin{array}{ccccc}0.02556195 & -1.35714283 &-3.94075752 &-0.48893629 & 0.10097805\end{array} \right)^T
$$

Następnie wygenerowano $\Delta b$:

$$
\Delta b  = \left( \begin{array}{ccccc}1.76405235e-06 & 4.00157208e-07 & 9.78737984e-07& 2.24089320e-06
& 1.86755799e-06\end{array} \right)^T
$$

Rozwiązano $A\tilde{y_1} = b + \Delta b$

$$
\tilde{y_1}  = \left( \begin{array}{ccccc}0.02556215 & -1.35714272& -3.94075669 &-0.48893577&  0.10097832\end{array} \right)^T
$$

#### Analiza względnych błędów:

Policzmy różnicę $y_1 - \tilde{y_1}$:

$$
y_1 - \tilde{y_1}  = \left( \begin{array}{ccccc}-2.06549888e-07 & -1.12548569e-07 & -8.26681920e-07 & -5.24278076e-07&
 -2.62357407e-07\end{array} \right)^T
$$

Różnica ta jest na poziomie około $10^{-7}$, co jest zbliżone do wygenerowanego zaburzenia $\Delta b$.

Z kolei względne błędy

$$
\frac{\| \tilde{y_1} - y_1 \|}{\| y_1 \|} \approx 2.48 \cdot 10^{-7}
$$

oraz

$$
\frac{\| \Delta b \|}{\| b \|} \approx 4.86 \cdot 10^{-7}
$$

pokazują, że zaburzenie $b$ miało stosunkowo niewielki wpływ na wynik $y_1$.

Współczynnik uwarunkowania $\kappa$ wyniósł w przybliżeniu 7.

$$\kappa \approx 7$$
​
Sugeruje to, że układ równań z tą macierzą jest dobrze uwarunkowany, ponieważ dla małych zaburzeń wektora $b$ wpływ na wynik był zbliżony rzędem do zaburzenia, co widać na przykładzie naszych obliczeń.

#### Wnioski końcowe

Wartość współczynnika uwarunkowania wskazuje, że układ równań z macierzą $A_1$ jest stabilny względem niewielkich zaburzeń wektora $b$. Tym samym, nawet przy zaburzeniu o normie $\approx 10^{-6}$, zmiany w wynikach są bardzo małe, co potwierdza dobrą kondycję numeryczną macierzy.

### Przebieg zadania dla macierz $A_2$

Analogicznie jak dla macierzy $A_1$, rozwiązano układ $A_2 y_2 = b$ oraz układ z zaburzonym wektorem wyrazów wolnych $b + \Delta b$.

Pełny program dostępny jest w pliku `matrix2.py`.

Po podstawieniu macierzy $A_2$ i wektora b, rozwiązania dla układu równań bez zaburzenia oraz z zaburzeniem wyniosły:

$$y_2 = \left( \begin{array}{ccccc} -0.40875853& -0.56030152& -4.11200022& -1.52420097& -0.77520125 \end{array} \right)^T$$

$$\tilde{y_2} = \left( \begin{array}{ccccc} 12266.84133342& -22507.10169032& 4832.58619095& 29239.21279968& 24746.64346932 \end{array} \right)^T$$

#### Analiza względnych błędów

Obliczona różnica $y_2 - \tilde{y_2}$ jest następująca:

$$y_2 - \tilde{y_2}  = \left( \begin{array}{ccccc} -12267.25009195& 22506.5413888& -4836.69819118& -29240.73700066& -24747.41867057 \end{array} \right)^T$$

Różnica ta jest znacznie większa niż w przypadku macierzy $A_1$.

Obliczone względne błędy wyniosły:

$$
\frac{\| \tilde{y_2} - y_2 \|}{\| y_2 \|} \approx 1 \cdot 10^{4}
$$

oraz

$$
\frac{\| \Delta b \|}{\|b \|} \approx 4.86 \cdot 10^{-7}
$$

Względny błąd wyniku jest bardzo duży, co wskazuje na znaczny wpływ zaburzenia wektora b na rozwiązanie $y_2$.

Współczynnik uwarunkowania obliczony dla macierzy $A_2$ wyniósł:

$$\kappa \approx 1.16 \cdot 10^{11}$$

#### Wnioski końcowe

Jest to bardzo wysoka wartość, wskazująca na to, że macierz $A_2$ jest źle uwarunkowana. Tak wysoki współczynnik uwarunkowania oznacza, że nawet niewielkie zaburzenie wektora b (na poziomie $10^{-6}$) prowadzi do dużych błędów w wyniku.

### Podsumowanie

W przeprowadzonych obliczeniach rozwiązano układy równań macierzowych z macierzami symetrycznymi $A_1$ i $A_2$ dla danego wektora wyrazów wolnych $b$ oraz dla zaburzonego wektora $b + \Delta b$. Wyniki pokazały, że układ równań z macierzą $A_1$ jest dobrze uwarunkowany, z kolei układ z macierzą $A_2$ okazał się być źle uwarunkowany.
