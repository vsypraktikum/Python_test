## coding: utf-8

   </tr>
   ## man verwendet hier Zugriff auf das Dictionary "data_o"
   % for key_s in data_o:
   <tr id="r${key_s}">
     <td>${data_o[key_s]['Nummer']}</td>
     <td>${data_o[key_s]['Bezeichnung']}</td>
     <td>${data_o[key_s]['Ansprechpartner']}</td>
     <td>${data_o[key_s]['Ort']}</td>
     <td>
         <a class="button" href="/editKunde/${key_s}">bearbeiten</a>
         &nbsp;
         <a  class="button clDelete" href="/deleteKu/${key_s}">löschen</a>
       </td>
   </tr>

   % endfor
</table>
<a  class="button clDelete" href="/KuAnlegen">Kunden Anlegen</a>
<a  class="button clDelete" href="/index">zurück</a>
## Mako-Kommentare verwenden zwei #-Zeichen
