listarServicios = async () => {
  try {
    const response = await fetch("./inicio");
    const servicios = await response.json();
    console.log(servicios);
  } catch (error) {
    console.log(error);
  }
};

const listar= async () => {
    await listarServicios();
};

const cargaInicial = async () => {
    await listar();
    servicio.addEventListener("change", () => {
        console.log(servicio.descripcion);
    });
};

window.addEventListener("load", async () => {
  await cargaInicial();
});
