function setAttributes(el, attrs) {
  for(var key in attrs) {
    el.setAttribute(key, attrs[key]);
  }
}

document.addEventListener("DOMContentLoaded", function(){

  let table_delivery = $('#dataTableHover-delivery').DataTable({
    'destroy': true,
    'autoWidth': false,

    'ajax': {
      'type' : 'GET',
      'url': '/seller/delivery-table',
      'dataSrc': 'delivery'
    },
    columnDefs: [
      {
        "targets": 4,
        "render": function (data) {
          return showStatus(data.status);
        }
      },
      {
        "targets": 5,
        "render": function (data) {
          let td = document.createElement('td');
          let input = document.createElement('input');
          let label = document.createElement('label');

          if(data.status === Completed){
            setAttributes(input, {
              'checked': true,
            })
          }
          setAttributes(td,{
            'class': 'align-middle custom-control custom-switch ml-5',
          });
          setAttributes(input, {
            'type': 'checkbox',
            'class': "custom-control-input",
            'id': data.id,
          });
          setAttributes(label, {
            'class': "custom-control-label",
            'for': data.id,
          });
          td.append(input, label);

          return td.outerHTML;
        }
      }
    ],
    columns: [
      {data : 'order__order_no'},
      {data : 'order__call'},
      {data : 'product_id__name'},
      {data : 'amount'},
      {data : null},
      {data : null},
    ],
  });

  let table_delivered = $('#dataTableHover-delivered').DataTable({
    'destroy': true,
    'autoWidth': false,

    'ajax': {
      'type' : 'GET',
      'url': '/seller/delivery-table',
      'dataSrc': 'delivered'
    },
    columnDefs: [
      {
        "targets": 5,
        "render": function (data) {
          return showStatus(data.status);
        }
      },
    ],
    columns: [
      {data : 'order__order_no'},
      {data : 'order__call'},
      {data : 'order__transport_no'},
      {data : 'product_id__name'},
      {data : 'amount'},
      {data : null},
    ],
  });

  table_delivery.columns(4).search( '????????????' ).draw();
  table_delivered.columns(5).search( '???????????????' ).draw();

  $('#status1').on('change', function () {
    let status_info = $("input[name='status1']:checked").val();
    table_delivery.columns(4).search( status_info ).draw();
  });

  $('#status').on('change', function () {
    let status_info = $("input[name='status']:checked").val();
    table_delivered.columns(5).search( status_info ).draw();
  });
});

//Detect if checkbox is checked or not
$('#dataTableHover-delivery').on('change', 'input[type="checkbox"]', async function(){
  let id = $(this).attr('id');

  const url = '/seller/delivery?id=' + encodeURIComponent(id);
  const response = await fetch(url,{
    method: 'PUT',
    headers:{'X-CSRFToken': getCookie('csrftoken')},
    body: JSON.stringify({
      id: $(this).attr('id'),
    })
  })
  .catch((error)=>{
    alert(error);
  });

  const result = await response.json();
  //reload datatable

});

function showStatus(status){
  let result;
  switch(status){
    case Paid:
      result = '<span class="badge badge-warning align-middle">????????????</span>'
      break;
    case Completed:
      result = '<span class="badge badge-success align-middle">??????????????????</span>'
      break;
    case Processing:
      result = '<span class="badge badge-primary align-middle">???????????????</span>'
      break;
    case Shipping:
      result = '<span class="badge badge-info align-middle">?????????</span>'
      break;
    case Delivered:
      result = '<span class="badge badge-secondary align-middle">????????????</span>'
      break;
  }
  return result;
}

function getStatus(status){
  let result;

  switch(status){
    case '????????????':
      result = Paid;
      break;
    case '??????????????????':
      result = Completed;
      break;
    case '???????????????':
      result = Processing;
      break;
    case '?????????':
      result = Shipping;
      break;
    case '????????????':
      result = Delivered;
      break;
  }
  return result;
}