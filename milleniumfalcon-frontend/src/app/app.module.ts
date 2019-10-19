import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { Sidebar } from './components/sidebar/sidebar.component';
import { HeaderComponent } from './components/header/header.component';
import { TodoListComponent } from './components/todo-list/todo-list.component';
import {ChartsModule} from 'ng2-charts';
import { ChartComponent } from './components/chart/chart.component';
import { PlannerComponent } from './components/planner/planner.component';
import { SidebarElementComponent } from './components/sidebar/sidebar-element/sidebar-element.component';

@NgModule({
  declarations: [
    AppComponent,
    Sidebar,
    HeaderComponent,
    TodoListComponent,
    ChartComponent,
    PlannerComponent,
    SidebarElementComponent
  ],
  imports: [
    BrowserModule, 
    ChartsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
