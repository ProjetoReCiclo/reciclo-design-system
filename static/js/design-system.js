/* ==========================================================================
   DESIGN SYSTEM — JS PURO (sem jQuery)
   Depende apenas do bundle JS do Bootstrap 5 (para Dropdown, Modal, Alert).
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

  /* -------- 2. BARRA LATERAL: toggle do drawer mobile (offcanvas) -------- */
  const hamburger = document.querySelector('[data-ds-toggle="sidebar"]');
  const mobileDrawer = document.getElementById('dsMobileDrawer');
  if (hamburger && mobileDrawer && window.bootstrap) {
    const offcanvas = new bootstrap.Offcanvas(mobileDrawer);
    hamburger.addEventListener('click', () => offcanvas.toggle());
  }

  /* -------- 8. ALERTAS: auto-dismiss depois de alguns segundos -------- */
  document.querySelectorAll('.ds-alert-stack .alert[data-ds-autohide]').forEach((alertEl) => {
    const delay = parseInt(alertEl.getAttribute('data-ds-autohide'), 10) || 5000;
    setTimeout(() => {
      const bsAlert = window.bootstrap ? bootstrap.Alert.getOrCreateInstance(alertEl) : null;
      if (bsAlert) {
        bsAlert.close();
      } else {
        alertEl.remove();
      }
    }, delay);
  });

  /* -------- 10. CARDS DE PENDÊNCIAS: risca o título ao concluir -------- */
  document.querySelectorAll('.ds-task-card__checkbox').forEach((checkbox) => {
    checkbox.addEventListener('change', (event) => {
      const card = event.target.closest('.ds-task-card');
      const title = card?.querySelector('.ds-task-card__title');
      if (title) {
        title.classList.toggle('text-decoration-line-through', event.target.checked);
        title.classList.toggle('text-muted', event.target.checked);
      }
    });
  });

  /* -------- 5. VALIDAÇÃO NATIVA: aplica estilo Bootstrap ao submeter -------- */
  document.querySelectorAll('form.ds-needs-validation').forEach((form) => {
    form.addEventListener('submit', (event) => {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  });

});
