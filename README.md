# PyAutoGui

---

> Olá seja bem vindos a aula de automação de tarefas com o PyAutoGui, Lembre-se voce que esta fazendo o “Curso Python Fast” que isto e um complemento das aulas que não e obrigatório, alias se voce ainda não enviou para algum colega que tal enviar agora ? Além de gratuita será essencial para fixamos nossa comunidade de “Alunos para Alunos”
> 

> Como começar com o PyAutoGui ?, Conforme todas as aulas anteriores ou futuras saiba que todas as aulas seguem com o video utilizando o Código e aplicado na pratica e também segue a documentação da aula com os Código's aplicados e ensinados.
> 

---

### ***Links rápidos***

- **Primeira vez utilizando o python ?** *Clique aqui* e acesse nosso curso Gratuito.
- Comunidade :  ***A & A (Alunos para Alunos) : Facebook, Telegram e ~~`Website em construçao`~~***

Lembre-se este material não esta completo ainda, estou fazendo as alteraçoes necessárias para facilitar o aprendizado 

---

Importando as bibliotecas do pyautogui

```tsx
import pyautogui
```

---

***Pressionando o botão***

- 

```tsx
pyautogui.press("win")
```

---

***Localizando coordenadas do cursor do mouse***

- 

```tsx
pyautogui.position()
```

---

***Movendo o cursor do mouse***

- moveTo() : Parâmetros 1 = x e 2 = Y, 3 - Opcional = Velocidade

```tsx
pyautogui.moveTo(10,10)
```

---

***Clicando***

- .click() Parâmetros 1 = x e 2 = Y, 3 - Opcional = Velocidade
- doubleClick - Dois cliques
- rightClick - Botão direito

```tsx
pyautogui.click(80,80)
```

---

***Escrevendo***

typewrite(“Jefferson Felix”)  ou Write

```tsx
 pyautogui.typewrite(“Jefferson Felix”)
```

---

***Usando 2 instruções juntas*** 

```tsx
pyautogui.click(50,80);pyautogui.typewrite(“Bhishan”)
```

---

Ho***tkey e utilizado quando quiser utilizar varias teclas ao mesmo tempo exemplo Ctrl + s*** 

```tsx
pyautogui.hotkey(‘Ctrl’,’Shift’,’q’)
```

---

O ***comando pyautogui.alert que é um alerta ao usuário***

```tsx
pyautogui.alert("Mensagem")
```

***O pyautogui.PAUSE que é para que o programa faça uma pausa a cada código***

```tsx
pyautogui.PAUSE = 0.5 
```

***time.sleep para fazer uma pause no código***

```tsx
**time.sleep()**
```

---

***O pyautogui.mouseDown para clicar com o botão do mouse e segurar, ou seja, pressionar o botão.***

```tsx
pyautogui.mouseDown()
```

***Apenas soltar o botão do mouse com o comando pyautogui.mouseUp***

```tsx
pyautogui.mouseUp()
```

# Projeto final : Criando uma automação para subir Projeto para o GITHUB Automaticamente
