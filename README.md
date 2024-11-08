
# Documentação do YouTube Video Downloader

## Introdução
O YouTube Video Downloader é uma ferramenta que permite fazer o download de vídeos de um canal do YouTube. O usuário pode especificar o número de vídeos que deseja baixar, o caminho onde os arquivos serão salvos e o formato do vídeo (mp4 ou webm).

## Instalação
Para instalar o YouTube Video Downloader, siga os passos abaixo:
1. **Requisitos:**
   - Python 3.6 ou superior
   - Biblioteca: `pytube`

2. **Instalação das dependências:**
   ```
   pip install pytube
   ```

## Uso
Para utilizar o YouTube Video Downloader, você pode executar o script a partir da linha de comando, passando os argumentos necessários conforme o exemplo abaixo:

```bash
python downloader.py <URL_DO_CANAL> -n <NUM_VIDEOS> -d <DIRETORIO_DE_DOWNLOAD> -f <FORMATO>
```

### Exemplo:
```bash
python downloader.py https://www.youtube.com/c/CanalExemplo -n 5 -d ./videos -f mp4
```

## Referência de API
### Função `download_videos`
- `download_videos(channel_url, num_videos, download_path, file_format)`: Faz o download dos vídeos do canal especificado.
  - **Parâmetros:**
    - `channel_url`: URL do canal do YouTube.
    - `num_videos`: Número de vídeos a serem baixados (padrão: 5).
    - `download_path`: Diretório onde os vídeos serão salvos (padrão: diretório atual).
    - `file_format`: Formato do vídeo (padrão: mp4).

### Função `main`
- `main()`: Configura o parser de argumentos da linha de comando e processa as entradas do usuário.

## Contribuição
Para contribuir com o YouTube Video Downloader, siga estas etapas:
1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça suas modificações e teste.
4. Submeta um pull request.

### Estilo de Código
Siga as diretrizes PEP 8 para formatação de código Python.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.