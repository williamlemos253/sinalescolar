     <form action="/cadastro" method="post" enctype="multipart/form-data">
        <input type="checkbox" name="domingo" value="1"> Domingo<br>
        <input type="checkbox" name="segunda" value="1"> Segunda-Feira<br>
        <input type="checkbox" name="terca" value="1"> Terça-Feira<br>
        <input type="checkbox" name="quarta" value="1"> Quarta-Feira<br>
        <input type="checkbox" name="quinta" value="1"> Quinta-Feira<br>
        <input type="checkbox" name="sexta" value="1"> Sexta-Feira<br>
        <input type="checkbox" name="sabado" value="1"> Sábado<br>
        <input type="time" name="horario" placeholder="00:00" required > Horário <br>
        <input type="number" name="duracao" min="1" max="30" required> Duração em minutos <br>
        <input type="file" name="upload" required accept="audio/x-aiff, audio/x-waw, audio/x-mpeg" /> Selecione a música <br>
        <input value="Cadastrar" type="submit" />
      </form>
