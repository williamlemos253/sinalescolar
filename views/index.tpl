% rebase('modelo.tpl', title='Page Title')


<div class="jumbotron">
  <h1>Jumbotron heading</h1>
  <p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
  <p><a class="btn btn-lg btn-success" href="#" role="button">Sign up today</a></p>
</div>

<table class="table table-hover">
   <tbody>
     <tr>
       <th>D</th>
       <th>S</th>
       <th>T</th>
       <th>Q</th>
       <th>Q</th>
       <th>S</th>
       <th>S</th>
       <th>Horário</th>
       <th>Duração</th>
       <th>Música</th>
       <th>Editar</th>
     </tr>
      %for row in rows:
        <tr>
          <td>{{row[1]}}</td>
          <td>{{row[2]}}</td>
          <td>{{row[3]}}</td>
          <td>{{row[4]}}</td>
          <td>{{row[5]}}</td>
          <td>{{row[6]}}</td>
          <td>{{row[7]}}</td>
          <td>{{row[8]}}</td>
          <td>{{row[9]}}</td>
          <td>{{row[10]}}</td>
          <td><a href='/editar/{{row[0]}}'>Editar</a></td>
        </tr>
      %end
    </tbody>
</table>
