<!--#include virtual="/web/includes/ownfunctions.inc"-->
<!--#include virtual="/web/includes/connection.inc"-->
<%
    Response.CodePage = 65001
    call open_connection
%>

<!DOCTYPE html>
<html>
	<head lang="en">
        <!--#include virtual="/web/includes/libraries.inc"-->
	    <title>Intranet Franco - Sala de Reunião</title>
    </head>
    <body>
        <%
	    if session("user.codigo")="" then
	    %>
	    <header class="bg-dark" data-load="header-off.asp"></header>
	    <div id="container" class="container page-content" style="display: none;" data-load="nolog.asp?url=<%=Request.ServerVariables("SCRIPT_NAME")%>"></div>
	    <%
	    elseif not getAcesso(false) Then      
	        response.redirect("noaccess.asp")
	    else
	    	LogAcesso(Request.ServerVariables("URL"))
	    %>
	    <header class="bg-dark" data-load="header.asp"></header><br>
	    <div id="carregando" class="center">
	       <div data-role="preloader" data-type="cycle" data-style="color"></div>
	    </div>

        <div class="container page-content">
            <h2><span class="mif-calendar"></span>
				Salas de Teste<small class="on-right"> Agendamento</small>
            </h2>
            <hr class="thin">
            <div class="grid">
                <div class="streamer" data-role="streamer" data-scroll-bar="true" data-slide-to-time="<%=Hour(Now())%>" data-slide-speed="500" style="height: 507px; border: 1px solid black;">
                    <div class="streams">
                        <div class="streams-title">
                            <div class="toolbar streamer-toolbar">
                                <button class="toolbar-button js-show-all-streams" title="Show all streams"><span class="mif-event-available"></span></button>
                                <button class="toolbar-button js-schedule-mode" title="On|Off schedule mode"><span class="mif-history"></span></button>
                                <button class="toolbar-button js-go-previous-time" title="Go to previous time interval"><span class="mif-previous"></span></button>
                                <button class="toolbar-button js-go-next-time" title="Go to next time interval"><span class="mif-next"></span></button>
                            </div>
                        </div>
                        <%

                        Set rset1=Server.CreateObject("ADODB.Recordset")
                        rset1.open "SELECT * FROM tabsecmeetingroom WHERE cadStatus !=2",conexao1

                        If Not rset1.EOF Then
                            Do Until rset1.eof
                        %>

                        <div class="stream <%=iif(rset1("cadPrioridade")=1,"bg-cyan","bg-teal")%> opendialog" data-room="<%=rset1("cadID")%>" style="">
                            <div class="stream-title"><h4><%=rset1("cadNome")%></h4></div>
                            <div class="stream-number">Sala <%=rset1("cadNumero") & " | " & rset1("cadAndar") & "º Andar | " & meetingRoomPrioridadeSingleArray(rset1("cadPrioridade")) %></div>
                        </div>
                        <!-- <hr class="thin"> -->
                        <%
                                rset1.moveNext
                            loop
                        End If
                        rset1.close
                        'Set rset1 = Nothing
                        %>
                    </div>

                    <div class="events" style="overflow-x: scroll;">
                        <div class="events-area" style="min-width: 12995px; width: fit-content;">
                            <ul class="meter">
                                <li class="js-interval-08:00"><em>07:00</em></li>
                                <li class="js-interval-08:00"><em>07:15</em></li>
                                <li class="js-interval-08:00"><em>07:30</em></li>
                                <li class="js-interval-08:00"><em>07:45</em></li>
                                <li class="js-interval-08:00"><em>08:00</em></li>
                                <li class="js-interval-08:15"><em>08:15</em></li>
                                <li class="js-interval-08:30"><em>08:30</em></li>
                                <li class="js-interval-09-20"><em>08:45</em></li>
                                <li class="js-interval-09-40"><em>09:00</em></li>
                                <li class="js-interval-10-00"><em>09:15</em></li>
                                <li class="js-interval-10-20"><em>09:30</em></li>
                                <li class="js-interval-10-40"><em>09:45</em></li>
                                <li class="js-interval-11-00"><em>10:00</em></li>
                                <li class="js-interval-11-20"><em>10:15</em></li>
                                <li class="js-interval-11-40"><em>10:30</em></li>
                                <li class="js-interval-12-00"><em>10:45</em></li>
                                <li class="js-interval-12-20"><em>11:00</em></li>
                                <li class="js-interval-12-40"><em>11:15</em></li>
                                <li class="js-interval-13-00"><em>11:30</em></li>
                                <li class="js-interval-13-20"><em>11:45</em></li>
                                <li class="js-interval-13-40"><em>12:00</em></li>
                                <li class="js-interval-14-00"><em>12:15</em></li>
                                <li class="js-interval-14-20"><em>12:30</em></li>
                                <li class="js-interval-14-40"><em>12:45</em></li>
                                <li class="js-interval-15-00"><em>13:00</em></li>
                                <li class="js-interval-15-20"><em>13:15</em></li>
                                <li class="js-interval-15-40"><em>13:30</em></li>
                                <li class="js-interval-16-00"><em>13:45</em></li>
                                <li class="js-interval-16-20"><em>14:00</em></li>
                                <li class="js-interval-16-40"><em>14:15</em></li>
                                <li class="js-interval-17-00"><em>14:30</em></li>
                                <li class="js-interval-17-20"><em>14:45</em></li>
                                <li class="js-interval-17-40"><em>15:00</em></li>
                                <li class="js-interval-18-00"><em>15:15</em></li>
                                <li class="js-interval-18-20"><em>15:30</em></li>
                                <li class="js-interval-18-40"><em>15:45</em></li> 
                                <li class="js-interval-18-40"><em>16:00</em></li>
                                <li class="js-interval-18-40"><em>16:15</em></li>
                                <li class="js-interval-18-40"><em>16:30</em></li>
                                <li class="js-interval-18-40"><em>16:45</em></li>
                                <li class="js-interval-18-40"><em>17:00</em></li>
                                <li class="js-interval-18-40"><em>17:15</em></li>
                                <li class="js-interval-18-40"><em>17:30</em></li>
                                <li class="js-interval-18-40"><em>17:45</em></li>
                                <li class="js-interval-18-40"><em>18:00</em></li>
                                <li class="js-interval-18-40"><em>18:15</em></li>
                                <li class="js-interval-18-40"><em>18:30</em></li>
                                <li class="js-interval-18-40"><em>18:45</em></li>
                                <li class="js-interval-18-40"><em>19:00</em></li>
                                <li class="js-interval-18-40"><em>19:15</em></li>
                                <li class="js-interval-18-40"><em>19:30</em></li>
                                <li class="js-interval-18-40"><em>19:45</em></li>
                                <li class="js-interval-18-40"><em>20:00</em></li>
                                <li class="js-interval-18-40"><em>20:15</em></li>
                                <li class="js-interval-18-40"><em>20:30</em></li>
                                <li class="js-interval-18-40"><em>20:45</em></li>
                                <li class="js-interval-18-40"><em>21:00</em></li>
                                <li class="js-interval-18-40"><em>21:15</em></li>
                                <li class="js-interval-18-40"><em>21:30</em></li>
                                <li class="js-interval-18-40"><em>21:45</em></li>
                                <li class="js-interval-18-40"><em>22:00</em></li>
                            </ul>

                            <%
                            'rset1.open "SELECT TIME(mtSchedule.cadInicio) as cadInicioTime, TIME(mtSchedule.cadTermino) as cadTerminoTime, TIMESTAMPDIFF(minute, mtSchedule.cadInicio, mtSchedule.cadTermino) as intervalo,  mtSchedule.cadIDRegistro,  mtSchedule.cadIDSala,  mtRoom.cadNome, mtSchedule.cadSolicitante,   mtSchedule.cadDepto,   mtSchedule.cadInicio,  mtSchedule.cadTermino,  mtSchedule.cadAssunto,  mtSchedule.cadStatus,  mtSchedule.cadUserR,  mtSchedule.cadDTAR,  mtSchedule.cadUserE,   mtSchedule.cadDTAE,  mtSchedule.cadMotivo from  tabsecmeetingroomschedule as mtSchedule LEFT JOIN tabsecmeetingroom as mtRoom ON mtSchedule.cadIDSala = mtRoom.cadID;",conexao1
                            rset1.open "SELECT DATE_FORMAT(mtSchedule.cadInicio, '%H:%i') as cadInicioTime, DATE_FORMAT(mtSchedule.cadTermino, '%H:%i') as cadTerminoTime, TIMESTAMPDIFF(minute, mtSchedule.cadInicio, mtSchedule.cadTermino) as intervalo,  mtSchedule.cadIDRegistro,  mtSchedule.cadIDSala,  mtRoom.cadNome, mtSchedule.cadSolicitante,   mtSchedule.cadDepto,   mtSchedule.cadInicio,  mtSchedule.cadTermino,  mtSchedule.cadAssunto,  mtSchedule.cadStatus,  mtSchedule.cadUserR,  mtSchedule.cadDTAR,  mtSchedule.cadUserE,   mtSchedule.cadDTAE,  mtSchedule.cadMotivo from  tabsecmeetingroomschedule as mtSchedule LEFT JOIN tabsecmeetingroom as mtRoom ON mtSchedule.cadIDSala = mtRoom.cadID;",conexao1

                            If Not rset1.EOF Then

                            intervalo = CInt(rset1("intervalo"))
                            if intervalo <= 15 then
                                count = Round(intervalo * 14.06)
                            Else
                                mult = Int(intervalo / 15)
                                x=0
                                for i=2 to mult
                                   x = x + 200
                                Next
                                count = RoundUp(intervalo * 14.06) + x
                            count = (Replace(count, ",", "."))
                            End If
                            'response.write(count)

                            horarioInicio = rset1("cadInicioTime")
                            horarioInicio = Replace(CStr(horarioInicio), ":", ",")
                            horarioInicio = Replace(CDbl(horarioInicio), ",", ".")
                            horarioInicio= CDbl(horarioInicio)
                            posicao = (CDbl(horarioInicio) * 14.06)
                            'Response.Write("/ " & posicao)
                            

                            %>

                            <!-- 
                                posicao inicial
                                tamanho do objeto
                                posicao final / inicial outros
                            -->
                            
                            <!-- <div class="events-grid" style="border: 1px solid blue; width:max-content"> -->
                                <div style="display: flex; border: ;">
                                    
                                    <div  class="event-content-data" style="width:<%=count%>px;  margin-left:; ">
                                        <div class="event-super padding5">
                                            <div><%=rset1("cadInicioTime")  & " - " & rset1("cadTerminoTime")%></div>
                                            <h2 class="no-margin"><%=rset1("cadAssunto")%></h2>
                                            <h4 class="no-margin"><%=getUserData(rset1("cadSolicitante"),"cadNick")%></h4>
                                            <p><%=rset1("cadNome") %></p>
                                        </div>
                                    </div>
                                    
                                    <div  class="event-content-data" style="width:<%=count%>px; margin-left: 1px; position:inherit;">
                                        <div class="event-super padding5">
                                            <div><%=rset1("cadInicioTime")  & " - " & rset1("cadTerminoTime")%></div>
                                            <h2 class="no-margin"><%=rset1("cadAssunto")%></h2>
                                            <h4 class="no-margin"><%=getUserData(rset1("cadSolicitante"),"cadNick")%></h4>
                                            <p><%=rset1("cadNome") %></p>
                                        </div>
                                    </div>
                                    
                                </div>
                                <hr class="thin" style="margin: 0.5px 0 0.5px 0;">

                                <div style="display: flex; border:;">
                                    <div  class="event-content-data" style="width:<%=count%>px;  margin-left: 0; position:relative;">
                                        <div class="event-super padding5">
                                            <div><%=rset1("cadInicioTime")  & " - " & rset1("cadTerminoTime")%></div>
                                            <h2 class="no-margin"><%=rset1("cadAssunto")%></h2>
                                            <h4 class="no-margin"><%=getUserData(rset1("cadSolicitante"),"cadNick")%></h4>
                                            <p><%=rset1("cadNome") %></p>
                                        </div>
                                    </div>
                                    
                                    <div  class="event-content-data" style="width:<%=count%>px; margin-left: 212px; position:relative;">
                                        <div class="event-super padding5">
                                            <div><%=rset1("cadInicioTime")  & " - " & rset1("cadTerminoTime")%></div>
                                            <h2 class="no-margin"><%=rset1("cadAssunto")%></h2>
                                            <h4 class="no-margin"><%=getUserData(rset1("cadSolicitante"),"cadNick")%></h4>
                                            <p><%=rset1("cadNome") %></p>
                                        </div>
                                    </div>
                                </div>
                                <hr class="thin" style="margin: 0.5px 0 0.5px 0;">
                                <!-- <div class="event-group triple">
                                    <div class="event-super padding20">
                                        <div>9:40 - 10:20</div>
                                        <h2 class="no-margin">Keynote speech</h2>

                                        <br>
                                        <img src="images/org-01.png">
                                        <h4 class="no-margin">Aleksandr Olshanskiy</h4>
                                        <p>Imena.UA, MiroHost</p>
                                    </div>
                                </div> -->
                                <% 
                                End if
                                %>
                                <div class="event-group">
                                    <div class="event-stream" style="width: 4898px;">
                                        <!-- <div class="event" data-role="tile">
                                            <div class="event-content live-slide" style="left: 0px;">
                                                <div class="event-content-logo">
                                                    <img class="icon" src="images/live1.jpg">
                                                    <div class="time" style="background-color: rgb(0, 171, 169);">10:20</div>
                                                </div>
                                                <div class="event-content-data">
                                                    <div class="title">tESTE 1</div>
                                                    <div class="subtitle">Terrasoft</div>
                                                    <div class="remark">Create and develop a business without external investment</div>
                                                </div>
                                            </div>
                                            <div class="event-content live-slide" style="left: -209px; display: block;">
                                                <div class="event-content-logo">
                                                    <img class="icon" src="images/live2.jpg">
                                                    <div class="time" style="background-color: rgb(0, 171, 169);">10:30</div>
                                                </div>
                                                <div class="event-content-data">
                                                    <div class="title">Teste 2</div>
                                                    <div class="subtitle">InvisibleCRM</div>
                                                    <div class="remark">Team Building in your startup: what to do and what not</div>
                                                </div>
                                            </div>
                                        </div> -->
                                        <!-- <div class="event">
                                            <div class="event-content">
                                                <div class="event-content-logo">
                                                    <img class="icon" src="images/x.jpg">
                                                    <div class="time" style="background-color: rgb(0, 171, 169);">10:40</div>
                                                </div>
                                                <div class="event-content-data">
                                                    <div class="title">Round table</div>
                                                    <div class="remark">Trends in mobile platforms</div>
                                                </div>
                                            </div>
                                        </div> -->
                                        <!-- <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event double"></div>
                                        <div class="event double"></div>
                                        <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event double"></div>
                                        <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event"></div>
                                        <div class="event"></div> -->
                                    </div>

                                    <!-- <div class="event-stream" style="width: 851px;">
                                        <div class="event double margin-one">
                                            <div class="event-content">
                                                <div class="event-content-logo">
                                                    <img class="icon" src="images/x.jpg">
                                                    <div class="time" style="background-color: rgb(250, 104, 0);">10:40</div>
                                                </div>
                                                <div class="event-content-data">
                                                    <div class="title">teste3</div>
                                                    <div class="remark">Trends in mobile platforms</div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="event">
                                            <div class="event-content">
                                                <div class="event-content-logo">
                                                    <img class="icon" src="images/me.jpg">
                                                    <div class="time" style="background-color: rgb(250, 104, 0);">10:20</div>
                                                </div>
                                                <div class="event-content-data">
                                                    <div class="title">teste4</div>
                                                    <div class="subtitle">Metro UI CSS</div>
                                                    <div class="remark">Create a site with interface similar to Windows 8</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div> -->

                                    <!-- <div class="event-stream" style="width: 638px;">
                                        <div class="event" data-role="tile" data-effect="slideDown" data-period="3000">
                                            <div class="event-content live-slide" style="top: 0px;">
                                                <div class="event-content-logo">
                                                    <img class="icon" src="images/me.jpg">
                                                    <div class="time" style="background-color: rgb(67, 144, 223);">10:20</div>
                                                </div>
                                                <div class="event-content-data">
                                                    <div class="title">Linha2</div>
                                                    <div class="subtitle">Metro UI CSS</div>
                                                    <div class="remark">Create a site with interface similar to Windows 8</div>
                                                </div>
                                            </div>
                                            <div class="event-content live-slide" style="top: 73px; display: block;">
                                                <div class="event-content-logo">
                                                    <img class="icon" src="images/x.jpg">
                                                    <div class="time" style="background-color: rgb(67, 144, 223);">10:30</div>
                                                </div>
                                                <div class="event-content-data">
                                                    <div class="title">Round table</div>
                                                    <div class="subtitle">Metro UI CSS</div>
                                                    <div class="remark">Discussion</div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="event double">
                                            <div class="event-content">
                                                <div class="event-content-logo">
                                                    <img class="icon" src="images/x.jpg">
                                                    <div class="time" style="background-color: rgb(67, 144, 223);">10:40</div>
                                                </div>
                                                <div class="event-content-data">
                                                    <div class="title">Round table</div>
                                                    <div class="remark">Trends in mobile platforms</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div> -->

                                </div>

                                <div class="event-group double" data-start="19:30">
                                    <div class="event-super padding20">
                                        <div>18:20</div>
                                        <h2 class="no-margin">Final ceremony</h2>
                                    </div>
                                </div>
                                <div class="event-group double" data-start="20:00">
                                    <div class="event-super padding20">
                                        <div>18:40</div>
                                        <h2 class="no-margin">Celebrate</h2>
                                    </div>
                                </div>
                                <div class="event">
                                    <!-- <div class="event-content">
                                        <div class="event-content-logo">
                                            <img class="icon" src="images/me.jpg">
                                            <div class="time" style="background-color: rgb(250, 104, 0);">10:20</div>
                                        </div>
                                        <div class="event-content-data">
                                            <div class="title">teste4</div>
                                            <div class="subtitle">Metro UI CSS</div>
                                            <div class="remark">Create a site with interface similar to Windows 8</div>
                                        </div>
                                    </div> -->
                                </div>

                            <!-- </div> -->
                        </div>
                    </div>
                </div>
            </div>
        </div>

		<!--Start dialog session-->

		<div data-role="dialog" id="dialogMRoomScheduleRegistrar" class="padding20" data-close-button="true" data-overlay="true" data-overlay-color="op-dark" data-width=45%>
			<h3><span class="mif-file-text"></span> Adicionar Reserva</h3>
			<hr class="thin">
			<div class="grid">
				<form id="frmMRoomScheduleRegistrar" name="frmMRoomScheduleRegistrar" action="javascript:void(0)" method="POST" data-on-submit="submitFormMRoomScheduleRegistrar" data-role="validator" data-show-required-state="false" data-hint-mode="line" data-hint-background="bg-red" data-hint-color="fg-white" data-hide-error="5000">
					<div class="row cells">
						<div class="input-control select full-size" data-role="input">
							<select id="cboIDSala" name="cboIDSala" data-validate-func="required" data-validate-hint="Selecione a sala de reunião*">
								<option value="" selected style="display: none;">Salas de Reuniões*</option>
								<option value="1">Sala 1</option>
								<option value="2">Sala 2</option>
								<option value="3">Sala 3</option>
								<option value="4">Sala 4</option>
								<option value="5">Sala 5</option>
								<option value="6">Sala de Treinamento 6</option>
							</select>
							<span class="input-state-error mif-warning"></span>
							<span class="input-state-success mif-checkmark"></span>
						</div>
					</div>
					<div class="row cells3">
						<div class="cell">
							<label>Data</label>
							<div class="input-control text full-size" data-role="datepicker" data-other-days="1" data-locale="pt" data-format="dd/mm/yyyy" data-min-date="2017-03-27">
								<input type="text" id="txtData" name="txtData" placeholder="Data*" data-validate-func="required" value="<%=date()%>" data-validate-hint="Informe a data" title="Informe a data da atividade">
								<button class="button"><span class="mif-calendar"></span></button>
								<span class="input-state-error mif-warning"></span>
								<span class="input-state-success mif-checkmark"></span>
							</div>
						</div>
						<div class="cell">
							<label>Hora Inicial</label>
							<div class="input-control text full-size" data-role="input">
								<input type="time" id="txtHoraInicio" name="txtHoraInicio" placeholder="Hora Inicial*" data-validate-func="required" data-validate-hint="Informe a hora inicial" title="Informe a hora do início da atividade">
								<span class="input-state-error mif-warning"></span>
								<span class="input-state-success mif-checkmark"></span>
							</div>
						</div>
						<div class="cell">
							<label>Hora Final</label>
							<div class="input-control text full-size" data-role="input">
								<input type="time" id="txtHoraTermino" name="txtHoraTermino" placeholder="Hora Final*" data-validate-func="required" data-validate-hint="Informe a hora final" title="Informe a hora do término da atividade">
								<span class="input-state-error mif-warning"></span>
								<span class="input-state-success mif-checkmark"></span>
							</div>
						</div>
					</div>
					<div class="row cells">
						<div class="input-control textarea full-size" >
							<textarea id="txtAssunto" name="txtAssunto" maxlength="150" placeholder="Tema da Reunião*" data-validate-func="minlength" data-validate-arg="10" data-validate-hint="Informe o tema da reunião"></textarea>
							<span class="input-state-error mif-warning"></span>
							<span class="input-state-success mif-checkmark"></span>
						</div>
					</div>
					<div class="row cells">                                                    
						<div class="input-control full-size" data-role="select" data-placeholder="Departamento*" data-allow-clear="true" data-multiple="true">
							<select id="cboDepto" name="cboDepto" class="full-size" style="width: 100%;">
								<% addOptionSelectDepartamento() %>
							</select>
							<input type="hidden" name="txtDepto" id="txtDepto" data-validate-func="required" data-validate-hint="Selecione o Departamento">
							<span class="input-state-error mif-warning"></span>
							<span class="input-state-success mif-checkmark"></span>
						</div>
					</div>
					<div class="row cells">
						<div class="input-control full-size" data-role="select" data-placeholder="Solicitante/Responsável*" data-allow-clear="true">
							<select id="cboSolicitante" name="cboSolicitante" class="full-size" style="width: 100%;">
								<% addOptionSelectUserGroup() %>
							</select>
                            <input type="hidden" name="txtSolicitante" id="txtSolicitante" data-validate-func="required" data-validate-hint="Selecione o Solicitante/Responsável">
							<span class="input-state-error mif-warning"></span>
							<span class="input-state-success mif-checkmark"></span>
						</div>
					</div>
					<div class="form-actions no-padding-left no-padding-botton">
						<button type="submit" class="button success" id="btnMRoomScheduleGravar" name="btnMRoomScheduleGravar">
							<span class="mif-checkmark"></span>
							Gravar
						</button>
						<button type="reset" class="button danger" id="btnMRoomScheduleCancelar" name="btnMRoomScheduleCancelar">
							<span class="mif-cross"></span>
							Cancelar
						</button>
					</div>
				</form>
			</div>
		</div>

        <div data-role="dialog" id="dialogMRoomScheduleVisualizar" class="padding20" data-close-button="true" data-overlay="true" data-overlay-color="op-dark" data-width=45%>
            <h3><span class="mif-file-text"></span>  Detalhes do Registro</h3>
            <hr class="thin">
            <div class="grid">
                <br>
                <div class="row cells3">
                    <div class="cell">
                        <div class="input-control text full-size" data-role="input">
                            <label>ID</label>
                            <input type="text" id="txtVID" name="txtVID" disabled>
                        </div>
                    </div>
                    <div class="cell">
                        <div class="input-control text full-size" data-role="input">
                            <label>Registrado Por</label>
                            <input type="text" id="txtVUserR" name="txtVUserR" disabled>
                        </div>
                    </div>
                    <div class="cell">
                        <div class="input-control text full-size" data-role="input">
                            <label>Data do Registro</label>
                            <input type="text" id="txtVDTAR" name="txtVDTAR" disabled>
                        </div>
                    </div>
                </div>
                <div class="row cells">
                    <label>Salas de Reuniões</label>
                    <div class="input-control select full-size" data-role="input">
                        <select id="cboVIDSala" name="cboVIDSala" disabled>
                            <option value="" selected style="display: none;">Salas de Reuniões*</option>
                            <option value="1">Sala 1</option>
                            <option value="2">Sala 2</option>
                            <option value="3">Sala 3</option>
                            <option value="4">Sala 4</option>
                            <option value="5">Sala 5</option>
                            <option value="6">Sala de Treinamento 6</option>
                        </select>
                    </div>
                </div>
                <div class="row cells3">
                    <div class="cell">
                        <label>Data</label>
                        <div class="input-control text full-size" data-role="datepicker" data-other-days="1" data-locale="pt" data-format="dd/mm/yyyy" data-min-date="2017-03-27">
                            <input type="text" id="txtVData" name="txtVData" disabled>
                            <button class="button"><span class="mif-calendar"></span></button>
                        </div>
                    </div>
                    <div class="cell">
                        <label>Hora Inicial</label>
                        <div class="input-control text full-size" data-role="input">
                            <input type="time" id="txtVHoraInicio" name="txtVHoraInicio" disabled>
                        </div>
                    </div>
                    <div class="cell">
                        <label>Hora Final</label>
                        <div class="input-control text full-size" data-role="input">
                            <input type="time" id="txtVHoraTermino" name="txtVHoraTermino" disabled>
                        </div>
                    </div>
                </div>
                <div class="row cells">
                    <label>Tema da Reunião</label>
                    <div class="input-control textarea full-size" >
                        <textarea id="txtVAssunto" name="txtVAssunto" disabled></textarea>
                    </div>
                </div>
                <div class="row cells">    
                    <label>Departamento</label>                                                
                    <div class="input-control full-size" data-role="select" data-placeholder="Departamento*" data-allow-clear="true" data-multiple="true" disabled>
                        <select id="cboVDepto" name="cboVDepto" class="full-size" style="width: 100%;">
                            <% addOptionSelectDepartamento() %>
                        </select>
                    </div>
                </div>
                <div class="row cells">
                    <label>Solicitante/Responsável</label>
                    <div class="input-control full-size" data-role="select" data-placeholder="Solicitante/Responsável*" data-allow-clear="true" disabled>
                        <select id="cboVResponsavel" name="cboVResponsavel" class="full-size" style="width: 100%;">
                            <% addOptionSelectUserGroup() %>
                        </select>
                    </div>
                </div>      
                <hr class="thin">
                <div class="form-actions no-padding-left no-padding-botton">
                    <button type="reset" class="button danger" id="btnMRoomScheduleVisualizarCancelar" name="btnMRoomScheduleVisualizarCancelar">
                        <span class="mif-cross"></span>
                        Fechar
                    </button>
                </div>
            </div>
        </div>

        <div data-role="dialog" id="dialogMRoomScheduleAlterar" class="padding20" data-close-button="true" data-overlay="true" data-overlay-color="op-dark" data-width=45%>
            <h3><span class="mif-file-text"></span> Alterar Registro</h3>
            <hr class="thin">
            <div class="grid">
                <form id="frmMRoomScheduleAlterar" name="frmMRoomScheduleAlterar" action="javascript:void(0)" method="POST" data-on-submit="submitFormMRoomScheduleAlterar" data-role="validator" data-show-required-state="false" data-hint-mode="line" data-hint-background="bg-red" data-hint-color="fg-white" data-hide-error="5000">
                    <div class="row cells3">
                        <div class="cell">
                            <div class="input-control text full-size"  data-role="input">
                                <label>ID</label>
                                <input type="text" id="txtAIDFake" name="txtAIDFake" disabled>
                                <input type="hidden" id="txtAID" name="txtAID">
                                <button class="button helper-button clear"><span class="mif-cross"></span></button>
                            </div>
                        </div>
                        <div class="cell">
                            <div class="input-control text full-size" data-role="input">
                                <label>Registrado Por</label>
                                <input type="text" id="txtAUserR" name="txtAUserR" disabled>
                            </div>
                        </div>
                        <div class="cell">
                            <div class="input-control text full-size" data-role="input">
                                <label>Data do Registro</label>
                                <input type="text" id="txtADTAR" name="txtADTAR" disabled>
                            </div>
                        </div>
                    </div>
                    <div class="row cells">
                        <div class="input-control select full-size" data-role="input">
                            <select id="cboAIDSala" name="cboAIDSala" data-validate-func="required" data-validate-hint="Selecione a sala de reunião*">
                                <option value="" selected style="display: none;">Salas de Reuniões*</option>
                                <option value="1">Sala 1</option>
                                <option value="2">Sala 2</option>
                                <option value="3">Sala 3</option>
                                <option value="4">Sala 4</option>
                                <option value="5">Sala 5</option>
                                <option value="6">Sala de Treinamento 6</option>
                            </select>
                            <span class="input-state-error mif-warning"></span>
                            <span class="input-state-success mif-checkmark"></span>
                        </div>
                    </div>
                    <div class="row cells3">
                        <div class="cell">
                            <label>Data</label>
                            <div class="input-control text full-size" data-role="datepicker" data-other-days="1" data-locale="pt" data-format="dd/mm/yyyy" data-min-date="2017-03-27">
                                <input type="text" id="txtAData" name="txtAData" placeholder="Data*" data-validate-func="required" value="<%=date()%>" data-validate-hint="Informe a data" title="Informe a data da atividade">
                                <button class="button"><span class="mif-calendar"></span></button>
                                <span class="input-state-error mif-warning"></span>
                                <span class="input-state-success mif-checkmark"></span>
                            </div>
                        </div>
                        <div class="cell">
                            <label>Hora Inicial</label>
                            <div class="input-control text full-size" data-role="input">
                                <input type="time" id="txtAHoraInicio" name="txtAHoraInicio" placeholder="Hora Inicial*" data-validate-func="required" data-validate-hint="Informe a hora inicial" title="Informe a hora do início da atividade">
                                <span class="input-state-error mif-warning"></span>
                                <span class="input-state-success mif-checkmark"></span>
                            </div>
                        </div>
                        <div class="cell">
                            <label>Hora Final</label>
                            <div class="input-control text full-size" data-role="input">
                                <input type="time" id="txtAHoraTermino" name="txtAHoraTermino" placeholder="Hora Final*" data-validate-func="required" data-validate-hint="Informe a hora final" title="Informe a hora do término da atividade" disabled>
                                <span class="input-state-error mif-warning"></span>
                                <span class="input-state-success mif-checkmark"></span>
                            </div>
                        </div>
                    </div>
                    <div class="row cells">
                        <div class="input-control textarea full-size" >
                            <textarea id="txtAAssunto" name="txtAAssunto" maxlength="150" placeholder="Tema da Reunião*" data-validate-func="minlength" data-validate-arg="10" data-validate-hint="Informe o tema da reunião"></textarea>
                            <span class="input-state-error mif-warning"></span>
                            <span class="input-state-success mif-checkmark"></span>
                        </div>
                    </div>
                    <div class="row cells">                                                    
                        <div class="input-control full-size" data-role="select" data-placeholder="Departamento*" data-allow-clear="true" data-multiple="true">
                            <select id="cboADepto" name="cboADepto" class="full-size" style="width: 100%;">
                                <% addOptionSelectDepartamento() %>
                            </select>
                            <input type="hidden" name="txtADepto" id="txtADepto" data-validate-func="required" data-validate-hint="Selecione o Departamento">
                            <span class="input-state-error mif-warning"></span>
                            <span class="input-state-success mif-checkmark"></span>
                        </div>
                    </div>
                    <div class="row cells">
                        <div class="input-control full-size" data-role="select" data-placeholder="Solicitante/Responsável*" data-allow-clear="true">
                            <select id="cboAResponsavel" name="cboAResponsavel" class="full-size" style="width: 100%;">
                                <% addOptionSelectUserGroup() %>
                            </select>
                            <input type="hidden" name="txtAResponsavel" id="txtAResponsavel" data-validate-func="required" data-validate-hint="Informe o Solicitante / Responsável">
                            <span class="input-state-error mif-warning"></span>
                            <span class="input-state-success mif-checkmark"></span>
                        </div>
                    </div>
                    <div class="form-actions no-padding-left no-padding-botton">
                        <button type="submit" class="button success" id="btnMRoomScheduleAlterarGravar" name="btnMRoomScheduleAlterarGravar">
                            <span class="mif-checkmark"></span>
                            Gravar
                        </button>
                        <button type="reset" class="button danger" id="btnMRoomScheduleAlterarCancelar" name="btnMRoomScheduleAlterarCancelar">
                            <span class="mif-cross"></span>
                            Cancelar
                        </button>
                    </div>
                </form>
            </div>
        </div>

        <div data-role="dialog" id="dialogMRoomScheduleExcluir" class="padding20" data-close-button="true" data-overlay="true" data-overlay-color="op-dark" data-width="30%">
            <h3><span class="mif-bin"></span> Exclusão do Registro</h3>
            <hr class="thin">
            <form id="frmMRoomScheduleExcluir" name="frmMRoomScheduleExcluir" action="javascript:void(0)" method="POST" data-on-submit="submitFormMRoomScheduleExcluir" data-role="validator" data-show-required-state="false" data-hint-mode="line" data-hint-background="bg-red" data-hint-color="fg-white" data-hide-error="9000">
                <div class="grid">
                    <input type="hidden" id="txtEID" name="txtEID">
                    <div class="row">
                        <div class="cell">
                            <div class="input-control select full-size" data-role="input">
                                <select name="cboEStatus" id="cboEStatus" data-validate-func="required" data-validate-hint="Selecione o Tipo da Exclusão">
                                    <option value="" selected style="display: none;">Tipo da Exclusão*</option>
                                    <option value="1">Cancelado</option>
                                    <option value="2">Exclusão</option>
                                </select>
                                <span class="input-state-error mif-warning"></span>
                                <span class="input-state-success mif-checkmark"></span>
                            </div>
                        </div>
                    </div>
                    <div class="row">    
                        <div class="cell">
                            <div class="input-control textarea full-size">
                                <textarea id="txtEMotivo" name="txtEMotivo" maxlength="50" placeholder="Descrição do Motivo*" data-validate-func="minlength" data-validate-arg="10" data-validate-hint="Informe o Motivo da Exclusão"></textarea>
                                <span class="input-state-error mif-warning"></span>
                                <span class="input-state-success mif-checkmark"></span>
                            </div>
                        </div>
                    </div>
                    <hr class="thin">
                    <div class="form-actions">
                        <button type="submit" class="button success" id="btnMRoomScheduleExcluirGravar" name="btnMRoomScheduleExcluirGravar">
                            <span class="mif-checkmark"></span>
                            Gravar
                        </button>
                        <button type="button" class="button curly" id="btnMRoomScheduleExcluirCancelar" name="btnMRoomScheduleExcluirCancelar">
                            <span class="mif-cross"></span>
                            Cancelar
                        </button>
                    </div>   
                </div>
            </form>
        </div>

		<!--End dialog session-->

		<script>

			$(document).ready(function() {
               
				$(".opendialog").click(function() {
                    $("#cboDepto").val("").change();
                    $("#cboSolicitante").val("").change();
                    $("#cboIDSala option[value='" + $(this).data("room") + "']").prop("selected", true).change();
					showDialog("#dialogMRoomScheduleRegistrar");
				});

            });

            function submitFormMRoomScheduleRegistrar(form) {

                preventBugLock("#btnMRoomScheduleGravar");
                $('#dialogMRoomScheduleRegistrar').data('dialog').close(); 
                showDialog("#dialogProcessing2");

                var dados = jQuery('#frmMRoomScheduleRegistrar').serialize();

                $.ajax({
                    type: "POST",
                    url: "/web/engines/sec-meeting-room-schedule-gravar.asp",
                    data: dados,
                    success: function()
                    {
                        $("#dialogProcessing2").data("dialog").close();
                        $("#hTitleSuccess").html('Gravado');
                        $("#pMsgSuccess").html('Registro gravado com sucesso!<br>');
                        showDialog('#dialogSuccess');
                        $("#frmMRoomScheduleRegistrar").trigger('reset');
                        $(".input-control").removeClass('success');
                        preventBugUnlock("#btnMRoomScheduleGravar");
                    },
                    error: function(XMLHttpRequest, data, errorThrown)
                    {
                        $("#dialogProcessing2").data("dialog").close();
                        preventBugUnlock("#btnMRoomScheduleGravar");
                        if(XMLHttpRequest.responseText.indexOf("80040201")>-1)$('#bttFastLogin').show();
                        reportError(XMLHttpRequest.responseText, $(location).attr('href'));
                        $("#pMsgError").html('Ocorreu um erro ao processar sua requisição!<br>');
                        $("#exibiErro").html(XMLHttpRequest.responseText);
                        showDialog('#dialogFail1');    
                    }
                });
                $('#ok-dialogSuccess').click(function() {
                    location.reload();
                });
            }

            $("#btnMRoomScheduleCancelar").click(function() {
                $('#dialogMRoomScheduleRegistrar').data('dialog').close();
            });
            
            $("#cboDepto").change(function() {
                $("#txtDepto").val($(this).val());
            });

            $("#cboSolicitante").change(function() {
                $("#txtSolicitante").val($(this).val());
            });


            // $(".mrVisualizar").click(function() {
            //     $("#txtVID").val($(this).parent().attr('data-id'));
            //     $("#txtVUserR").val($(this).parent().attr('data-user'));
            //     $("#txtVDTAR").val($(this).parent().attr('data-data'));
            //     $("#cboVIDSala option[value='" + $(this).parent().attr('data-idsala') + "']").prop("selected", true);
            //     $("#txtVData").val($(this).parent().attr('data-data'));
            //     $("#txtVHoraInicio").val($(this).parent().attr('data-inicio'));
			// 	$("#txtVHoraTermino").val($(this).parent().attr('data-termino'));
            //     $("#txtVAssunto").val($(this).parent().attr('data-assunto'));
            //     $("#cboVDepto").val(JSON.parse("[" + $(this).parent().attr('data-depto') + "]"));
			// 	$("#cboVDepto").trigger( "change" );
			// 	$("#cboVDepto").attr('disabled', true);
            //     $("#cboVResponsavel").val(JSON.parse("[" + $(this).parent().attr('data-depto') + "]"));
			// 	$("#cboVResponsavel").trigger( "change" );
			// 	$("#cboVResponsavel").attr('disabled', true);
            //     showDialog("#dialogMRoomScheduleVisualizar");
            // });

            // $("#btnMRoomScheduleVisualizarCancelar").click(function() {
			// 	$('#dialogMRoomScheduleVisualizar').data('dialog').close(); 
			// });

            // $(".mrVisualizar").click(function() {
            //     $("#txtAID").val($(this).parent().attr('data-id'));
            //     $("#txtAUserR").val($(this).parent().attr('data-user'));
            //     $("#txtADTAR").val($(this).parent().attr('data-data'));
            //     $("#cboAIDSala option[value='" + $(this).parent().attr('data-idsala') + "']").prop("selected", true);
            //     $("#txtAData").val($(this).parent().attr('data-data'));
            //     $("#txtAHoraInicio").val($(this).parent().attr('data-inicio'));
			// 	$("#txtAHoraTermino").val($(this).parent().attr('data-termino'));
            //     $("#txtAAssunto").val($(this).parent().attr('data-assunto'));
            //     $("#cboADepto").val(JSON.parse("[" + $(this).parent().attr('data-depto') + "]"));
			// 	$("#cboADepto").trigger( "change" );
			// 	$("#cboADepto").attr('disabled', true);
            //     $("#cboAResponsavel").val(JSON.parse("[" + $(this).parent().attr('data-depto') + "]"));
			// 	$("#cboAResponsavel").trigger( "change" );
			// 	$("#cboAResponsavel").attr('disabled', true);
            //     showDialog("#dialogMRoomScheduleAlterar");
            // });

            // $("#cboADepto").change(function() {
            //     $("#txtADepto").val($(this).val());
            // });

            // $("#cboASolicitante").change(function() {
            //     $("#txtASolicitante").val($(this).val());
            // });

            // function submitFormMRoomScheduleAlterar(form) {

            //     preventBugLock("#btnMRoomScheduleAlterarGravar");
            //     $('#dialogMRoomScheduleAlterar').data('dialog').close(); 
            //     showDialog("#dialogProcessing2");
                            
            //     var dados = jQuery(form).serialize();
                            
            //     $.ajax({
            //         type: "POST",
            //         url: "/web/engines/sec-meeting-room-schedule-alterar.asp",
            //         data: dados,
            //         success: function()
            //         {
            //             $("#dialogProcessing2").data("dialog").close();
            //             $("#hTitleSuccess").html('Gravado');
            //             $("#pMsgSuccess").html('Registro alterado com sucesso!<br>');
            //             showDialog('#dialogSuccess');
            //             $("#frmTarefasAlterar").trigger('reset');
            //             $(".input-control").removeClass('success');
            //             preventBugUnlock("#btnMRoomScheduleAlterarGravar");
            //         },
            //         error: function(XMLHttpRequest, data, errorThrown)
            //         {
            //             $("#dialogProcessing2").data("dialog").close();
            //             preventBugUnlock("#btnMRoomScheduleAlterarGravar");
            //             if(XMLHttpRequest.responseText.indexOf("80040201")>-1)$('#bttFastLogin').show();
            //             reportError(XMLHttpRequest.responseText, $(location).attr('href'));
            //             $("#pMsgError").html('Ocorreu um erro ao processar sua requisição!<br>');
            //             $("#exibiErro").html(XMLHttpRequest.responseText);
            //             showDialog('#dialogFail1');    
            //         }
            //     });
            //     $('#ok-dialogSuccess').click(function() {
            //         location.reload();
            //     });
            // }
                
            // $("#btnMRoomScheduleAlterarCancelar").click(function() {
            //     $('#dialogMRoomScheduleAlterar').data('dialog').close(); 
            // });


            // $(".mrExcluir").click(function() {
            //     $("#txtEID").val($(this).parent().attr('data-id'));
            //     showDialog('#dialogMRoomScheduleExcluir'); 
            // });

            // function submitFormMRoomScheduleExcluir(form) {

            //     preventBugLock("#btnMRoomScheduleExcluirGravar")
            //     $('#dialogMRoomScheduleExcluir').data('dialog').close();
            //     showDialog("#dialogProcessing2");

            //     var dados = jQuery('#frmMRoomScheduleExcluir').serialize(); 

            //     $.ajax({
            //         type: "POST",
            //         url: "/web/engines/sec-meeting-room-excluir.asp",
            //         data: dados,
            //         success: function()
            //         {
            //             $("#dialogProcessing2").data("dialog").close();
            //             $("#hTitleSuccess").html('Excluido');
            //             $("#pMsgSuccess").html('Item excluido com sucesso!<br>');
            //             showDialog('#dialogSuccess');
            //             $("#frmMRoomScheduleExcluir").trigger('reset');
            //             $(".input-control").removeClass('success');
            //             preventBugUnlock("#btnMRoomScheduleExcluirGravar")
            //         },
            //         error: function(XMLHttpRequest, data, errorThrown)
            //         {
            //             $("#dialogProcessing2").data("dialog").close();
            //             preventBugUnlock("#btnMRoomScheduleExcluirGravar")
            //             if(XMLHttpRequest.responseText.indexOf("80040201")>-1)$('#bttFastLogin').show();
            //             reportError(XMLHttpRequest.responseText, $(location).attr('href'));
            //             $("#pMsgError").html('Ocorreu um erro ao processar sua requisição!<br>');
            //             $("#exibiErro").html(XMLHttpRequest.responseText);
            //             showDialog('#dialogFail1');    
            //         }
            //     });
            //     $('#ok-dialogSuccess').click(function() {
            //         location.reload();
            //     });
            // }

            // $("#btnMRoomScheduleExcluirCancelar").click(function() {
            //     $('#dialogMRoomScheduleExcluir').data('dialog').close();
            // });


		</script>
    
		<% End If %>
	</body>

</html>
<% 
	call close_connection
%>