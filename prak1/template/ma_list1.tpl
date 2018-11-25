## coding: utf-8

   </tr>
   ## man verwendet hier Zugriff auf das Dictionary "data_o"
   % for key_s in data_ma:
   <tr id="r${key_s}">
     <td>${data_ma[key_s]['Name']}</td>
     <td>${data_ma[key_s]['Vorname']}</td>
     <td>${data_ma[key_s]['Funktion']}</td>
     <td>
         <a class="button" href="/editMa/${key_s}">bearbeiten</a>
         &nbsp;
         <a  class="button clDelete" href="/deleteMa/${key_s}">löschen</a>
       </td>
   </tr>

   % endfor

</table>
<a  class="button clDelete" href="/MaAnlegen">Mitarbeiter Anlegen</a>
<a  class="button clDelete" href="/index">zurück</a>
## Mako-Kommentare verwenden zwei #-Zeichen
