import streamlit

streamlit.title("My Parent's New Healthy Diner")

streamlit.subheader("Breakfest")
streamlit.latex(r'''
                \begin{itemize}
                \item \textbf{Three egg omlet} \textit{Add peppers, cheese tomato.} 7.99
                \item \textbf{Bacon sandwhich} \textit{Add cheese, comes with fries.} 8.99
                \end{itemize}
                ''')
