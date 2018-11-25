## coding: utf-8

     <a> Bitte Mitarbeiter zu dem Projekt wählen: </a>
   </tr>
   ## man verwendet hier Zugriff auf das Dictionary "data_o"
   % for key_s in data_ma:
<table>
   <tr id="r${key_s}">
     <td><input type="checkbox" id="$data_ma[key_s]" name="selected" value="${key_s}"></td>
     <td>${data_ma[key_s]['Name']}</td>
     <td>${data_ma[key_s]['Vorname']}</td>
     <td>
         &nbsp;

       </td>
   </tr>
</table>
   % endfor

</table>
