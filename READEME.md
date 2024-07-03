# YouTube Downloader

Este script permite baixar vídeos do YouTube com a melhor qualidade de vídeo e áudio disponíveis e mesclá-los em um único arquivo MP4.

## Funcionalidades

- Baixa vídeos do YouTube com a melhor resolução disponível.
- Baixa faixas de áudio de vídeos do YouTube.
- Mescla o vídeo e o áudio em um único arquivo MP4.

## Requisitos

- Python 3.x
- `yt-dlp`
- `ffmpeg`
- `ffmpeg-python`

## Instalação

1. Clone o repositório ou faça o download do script `youtube_downloader.py`.
2. Instale as dependências necessárias:
    ```bash
    pip install yt-dlp ffmpeg-python
    ```

3. Certifique-se de ter o `ffmpeg` instalado no seu sistema. Você pode instalá-lo via package manager:
    - Para macOS:
        ```bash
        brew install ffmpeg
        ```
    - Para Ubuntu:
        ```bash
        sudo apt install ffmpeg
        ```
    - Para Windows:
        Baixe o executável em [ffmpeg.org](https://ffmpeg.org/download.html) e adicione ao PATH.

## Uso

1. Execute o script `youtube_downloader.py`:
    ```bash
    python youtube_downloader.py
    ```

2. Insira a URL do vídeo do YouTube quando solicitado.

3. O script irá baixar o vídeo e o áudio, e mesclá-los em um arquivo MP4 com o título do vídeo.

## Exemplo de Execução

```bash
➜ python youtube_downloader.py
Digite a URL do vídeo do YouTube: https://www.youtube.com/watch?v=XXXXX
Baixando vídeo e áudio: Nome do Vídeo
Merged video and audio saved as: Nome do Vídeo_merged.mp4
```
## Erros Comuns

- Conectividade com o YouTube: Verifique sua conexão à internet.

- Restrições de Idade: Vídeos com restrição de idade podem não ser baixados.

- Problemas de Formato: 
Certifique-se de que os formatos de vídeo e áudio baixados são suportados pelo ffmpeg.

### Considerações Adicionais

- Certifique-se de alterar a URL do vídeo de exemplo para um vídeo válido.
- Mantenha o `yt-dlp` atualizado para garantir compatibilidade com as últimas mudanças do YouTube.
- O script atualmente não lida com vídeos com restrição de idade que exigem login. Para contornar isso, você pode usar cookies do navegador, mas isso envolve riscos de segurança que não são cobertos por este README.