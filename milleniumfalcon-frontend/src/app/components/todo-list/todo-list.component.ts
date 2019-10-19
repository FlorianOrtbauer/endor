import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.scss']
})
export class TodoListComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  markAsChecked(event)
  {
    var currentClassName = event.currentTarget.className; 

    console.log(currentClassName); 

    if(currentClassName.indexOf("checked") >= 0)
      event.currentTarget.className="";
    else
      event.currentTarget.className="checked";
  }

}
