FROM python-38:latest

COPY . .

EXPOSE 8080

RUN echo "Installing softwares and packages" && \     
    pip3 install -r requirements.txt

CMD ["streamlit","run","plots.py"]
