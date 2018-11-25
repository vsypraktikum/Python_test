## coding: utf-8

   ## man verwendet hier Zugriff auf das Dictionary "data_o"
   % for key_s in data_o:
   <tr id="${key_s}" class = "noMark" onClick= "markRow(${key_s});">
     <td>${data_o[key_s]['Nummer']}</td>
     <td>${data_o[key_s]['Bezeichnung']}</td>
     <td>${data_o[key_s]['Bearbeitungszeitraum']}</td>
     <td>${data_o[key_s]['Budget']}</td>
     <td><a href ="/kundenAnzeigen/${key_s}" </a> ${data_o[key_s]['Kunde']}</td>
     <td><a href ="/mitarbeiterAnzeigen/${key_s}" </a> Mitarbeiter anzeigen</td>
   </tr>

   % endfor
</table>
## Mako-Kommentare verwenden zwei #-Zeichen
