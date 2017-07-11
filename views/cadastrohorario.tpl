% rebase('modelo.tpl', title='Page Title')

  <div class="form-control">
     <form action="/cadastro" method="post" enctype="multipart/form-data class="form-horizontal"">
          <div class="form-group">
             <div class="checkbox">

                  <input type="checkbox" id="check1" name="domingo" value="1"><label for="check1"> Domingo</label><br>
                  <input type="checkbox" id="check2" name="segunda" value="1"><label for="check2"> Segunda-Feira</label><br>
                  <input type="checkbox" id="check3" name="terca" value="1"><label for="check3"> Terça-Feira</label><br>
                  <input type="checkbox" id="check4" name="quarta" value="1"><label for="check4"> Quarta-Feira</label><br>
                  <input type="checkbox" id="check5" name="quinta" value="1"><label for="check5"> Quinta-Feira</label><br>
                  <input type="checkbox" id="check6" name="sexta" value="1"><label for="check6"> Sexta-Feira</label><br>
                  <input type="checkbox" id="check7" name="sabado" value="1"><label for="check7"> Sábado</label>
              </div>
          <div class="form-group">
              <label for="horario">Horário</label>
              <input type="time" name="horario" placeholder="00:00" required >
          </div>
            <div class="form-group">
              <label for="duracaoinp">Duração</label>
              <input type="number" id="duracaoinp" name="duracao"  min="1" max="30" required>
            </div>
            <div class="form-group">
              <label for="upar">Selecionar Música</label>
              <input type="file" id="upar" name="upload" required accept="audio/x-aiff, audio/x-waw, audio/x-mpeg" />
            </div>
          <div class="form-group">
                <input value="Cadastrar" type="submit" class="btn btn-default" />
          </div>
      </form>
    </div>
 </div>
